# scripts/generate_dataset.py
import numpy as np, pandas as pd
from pathlib import Path

def main():
    np.random.seed(42)
    N = 1200

    idade = np.random.randint(18, 75, size=N)
    sexo = np.random.choice(['M','F'], size=N, p=[0.48, 0.52])
    altura = np.round(np.random.normal(1.70, 0.1, size=N), 2)
    altura = np.clip(altura, 1.45, 2.05)
    peso = np.round(np.random.normal(75, 15, size=N), 1)
    peso = np.clip(peso, 40, 160)
    imc = np.round(peso / (altura**2), 1)

    def cat_imc(x):
        if x < 18.5: return 'baixo_peso'
        if x < 25: return 'normal'
        if x < 30: return 'sobrepeso'
        return 'obesidade'

    categoria_imc = np.array([cat_imc(x) for x in imc])

    ex_semana = np.clip(np.random.poisson(3, size=N), 0, 7)
    min_ex_dia = np.clip(np.random.normal(35, 15, size=N).astype(int), 0, 120)
    passos = np.clip(np.random.normal(7500, 2500, size=N).astype(int), 500, 20000)

    frutas = np.clip(np.random.poisson(1.2, size=N), 0, 6)
    verduras = np.clip(np.random.poisson(1.0, size=N), 0, 6)
    calorias = np.clip(np.random.normal(2300, 500, size=N).astype(int), 1200, 4500)

    fumante = np.random.choice([0,1], size=N, p=[0.82, 0.18])
    alcool = np.clip(np.random.poisson(3, size=N), 0, 20)

    ps = np.clip(np.random.normal(122, 15, size=N).astype(int), 90, 200)
    pdiast = np.clip(np.random.normal(78, 10, size=N).astype(int), 60, 130)
    col = np.clip(np.random.normal(195, 35, size=N).astype(int), 120, 350)
    glic = np.clip(np.random.normal(96, 20, size=N).astype(int), 60, 220)

    auto = np.clip(np.round(np.random.normal(3.2, 0.9, size=N)), 1, 5).astype(int)

    df = pd.DataFrame({
        'id': np.arange(1, N+1),
        'idade': idade, 'sexo': sexo,
        'altura_m': altura, 'peso_kg': peso, 'imc': imc, 'categoria_imc': categoria_imc,
        'exercicios_semana': ex_semana, 'min_exercicio_dia': min_ex_dia, 'passos_dia': passos,
        'frutas_por_dia': frutas, 'verduras_por_dia': verduras, 'calorias_dia': calorias,
        'fumante': fumante, 'alcool_semana': alcool,
        'pressao_sistolica': ps,
        'pressao_diastolica': pdiast,
        'colesterol_total': col,
        'glicemia_jejum': glic,
        'autoavaliacao_saude': auto
    })

    cond = (
        (df['categoria_imc'] == 'normal') &
        ((df['exercicios_semana'] >= 3) | (df['passos_dia'] >= 8000)) &
        (df['pressao_sistolica'] < 140) & (df['pressao_diastolica'] < 90) &
        (df['colesterol_total'] < 240) & (df['glicemia_jejum'] < 126) &
        (df['fumante'] == 0)
    )
    df['label_saude'] = np.where(cond, 'saudavel', 'risco')

    Path('data/raw').mkdir(parents=True, exist_ok=True)
    out_path = Path('data/raw/saude.csv')
    df.to_csv(out_path, index=False)
    print(f"Dataset salvo em {out_path} — shape: {df.shape}")

if __name__ == "__main__":
    main()
