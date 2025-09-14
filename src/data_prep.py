# src/data_prep.py
import pandas as pd
from pathlib import Path

RAW_PATH = 'data/raw/saude.csv'
PROCESSED_PATH = 'data/processed/saude_limpo.csv'

def carregar_raw(path=RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)

def _recalcular_imc(df: pd.DataFrame) -> pd.Series:
    imc = (df['peso_kg'] / (df['altura_m']**2)).round(1)
    return imc

def limpar_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'id' in df.columns:
        df = df.drop_duplicates(subset=['id'])
    if {'peso_kg','altura_m'}.issubset(df.columns):
        df['imc'] = _recalcular_imc(df)
    rules = (
        (df['altura_m'].between(1.40, 2.10)) &
        (df['peso_kg'].between(35, 200)) &
        (df['calorias_dia'].between(800, 6000)) &
        (df['pressao_sistolica'].between(90, 220)) &
        (df['pressao_diastolica'].between(60, 140)) &
        (df['colesterol_total'].between(100, 400)) &
        (df['glicemia_jejum'].between(60, 300)) &
        (df['passos_dia'].between(500, 30000))
    )
    df = df[rules]
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(exclude='number').columns
    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())
    for c in cat_cols:
        if df[c].isna().any():
            df[c] = df[c].fillna(df[c].mode().iloc[0])
    if 'categoria_imc' in df.columns:
        def cat_imc(x):
            if x < 18.5: return 'baixo_peso'
            if x < 25: return 'normal'
            if x < 30: return 'sobrepeso'
            return 'obesidade'
        df['categoria_imc'] = df['imc'].apply(cat_imc)
    return df

def salvar_processed(df: pd.DataFrame, path=PROCESSED_PATH) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path

if __name__ == "__main__":
    raw = carregar_raw()
    clean = limpar_df(raw)
    out = salvar_processed(clean)
    print(f"Processado em: {out} — shape: {clean.shape}")
