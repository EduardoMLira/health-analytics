# src/features.py

from pathlib import Path
import pandas as pd

# caminho para o dataset limpo já usado no projeto
DATA_PATH = Path("data/processed/saude_limpo.csv")

# colunas que serão usadas como "features" (entradas do modelo)
FEATURES = [
    "idade",
    "imc",
    "exercicios_semana",
    "min_exercicio_dia",
    "passos_dia",
    "calorias_dia",
    "frutas_por_dia",
    "verduras_por_dia",
]

# coluna alvo (o que queremos prever)
TARGET = "autoavaliacao_saude"


def load_data() -> pd.DataFrame:
    """
    Carrega o dataset limpo do caminho padrão.
    """
    df = pd.read_csv(DATA_PATH)
    return df


def make_X_y(df: pd.DataFrame):
    """
    Separa o DataFrame em X (features) e y (alvo),
    removendo linhas com valores ausentes nas colunas usadas.
    """
    cols_needed = FEATURES + [TARGET]
    df_clean = df.dropna(subset=cols_needed).copy()

    X = df_clean[FEATURES]
    y = df_clean[TARGET]

    return X, y
