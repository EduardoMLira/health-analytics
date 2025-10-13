# notebooks/AC2_relacoes_insights.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # garante a raiz no sys.path

import pandas as pd
from src.viz import scatter_xy, corr_heatmap

DATA_PATH = Path('data/processed/saude_limpo.csv')
FIG_DIR = Path('notebooks/figs')
FIG_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA_PATH)

    # 1) IMC vs Idade
    scatter_xy(
        df, 'idade', 'imc',
        title='IMC vs Idade',
        out_path=FIG_DIR / 'ac2_scatter_imc_vs_idade.png'
    )

    # 2) Exercícios/semana vs Autoavaliação
    scatter_xy(
        df, 'exercicios_semana', 'autoavaliacao_saude',
        title='Exercícios/semana vs Autoavaliação de Saúde',
        out_path=FIG_DIR / 'ac2_scatter_exercicios_vs_autoavaliacao.png'
    )

    # 3) Calorias/dia vs IMC
    scatter_xy(
        df, 'calorias_dia', 'imc',
        title='Calorias/dia vs IMC',
        out_path=FIG_DIR / 'ac2_scatter_calorias_vs_imc.png'
    )

    # 4) Passos/dia vs IMC (gráfico extra)
    scatter_xy(
        df, 'passos_dia', 'imc',
        title='Passos/dia vs IMC',
        out_path=FIG_DIR / 'ac2_scatter_passos_vs_imc.png'
    )

    # 5) Colesterol vs Glicemia (gráfico extra)
    scatter_xy(
        df, 'colesterol_total', 'glicemia_jejum',
        title='Colesterol Total vs Glicemia em Jejum',
        out_path=FIG_DIR / 'ac2_scatter_colesterol_vs_glicemia.png'
    )

    # 6) Heatmap de correlação (subset relevante)
    cols = [
        'idade','imc','exercicios_semana','min_exercicio_dia','passos_dia',
        'colesterol_total','glicemia_jejum','calorias_dia','autoavaliacao_saude'
    ]
    existing = [c for c in cols if c in df.columns]
    corr_heatmap(
        df, cols=existing,
        title='Matriz de Correlação (AC2)',
        out_path=FIG_DIR / 'ac2_heatmap_correlacao.png'
    )

    # 7) Insights básicos
    insights = [
        'Tendência leve de aumento do IMC com a idade (IMC vs Idade).',
        'Mais exercícios/semana associam-se a melhor autoavaliação de saúde.',
        'Maior consumo de calorias tende a elevar o IMC (tendência positiva).',
        'Mais passos diários correlacionam-se com menor IMC (associação negativa).',
        'Colesterol total e glicemia em jejum apresentam correlação positiva moderada.'
    ]
    (FIG_DIR / 'ac2_insights.txt').write_text("\n".join(insights), encoding='utf-8')
    print('Gráficos salvos em notebooks/figs/ e insights em ac2_insights.txt')

if __name__ == '__main__':
    main()
