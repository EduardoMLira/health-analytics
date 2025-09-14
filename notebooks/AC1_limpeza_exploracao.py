# notebooks/AC1_limpeza_exploracao.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path('notebooks/figs').mkdir(parents=True, exist_ok=True)

df = pd.read_csv('data/processed/saude_limpo.csv')

desc = df.describe(include='all')
desc.to_csv('notebooks/figs/estatisticas_basicas.csv')
print(desc.select_dtypes('number'))

plt.figure()
df['imc'].plot(kind='hist', bins=30, title='Distribuição do IMC')
plt.xlabel('IMC')
plt.tight_layout()
plt.savefig('notebooks/figs/hist_imc.png', dpi=130)

plt.figure()
df['categoria_imc'].value_counts().plot(kind='bar', title='Categorias de IMC')
plt.xlabel('Categoria'); plt.ylabel('Contagem')
plt.tight_layout()
plt.savefig('notebooks/figs/barras_categoria_imc.png', dpi=130)

plt.figure()
df.boxplot(column='min_exercicio_dia', by='categoria_imc')
plt.title('Min de exercício/dia por Categoria IMC')
plt.suptitle('')
plt.xlabel('Categoria'); plt.ylabel('Minutos')
plt.tight_layout()
plt.savefig('notebooks/figs/box_min_exercicio_por_categoria.png', dpi=130)

print("\nFiguras salvas em notebooks/figs/")
