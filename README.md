🩺 Health Analytics IMC — Análise de Dados de Saúde (IMC, Exercícios e Alimentação)

Aluno: Eduardo Lira
Disciplina: Projeto de Análise de Dados (AC1 / AC2 / AC3 / Prova Final)

📊 Visão Geral do Projeto

Este projeto tem como objetivo analisar dados de saúde simulados relacionados a:

IMC

Hábitos alimentares

Exercícios físicos

Pressão arterial

Colesterol e glicemia

Autoavaliação de saúde

Utilizando Python, Pandas, Matplotlib, Scikit-Learn e Streamlit, o projeto evolui em etapas até chegar a um dashboard interativo com predição baseada em Machine Learning.

Entrega	Foco Principal	Resultado
AC1	Limpeza e exploração inicial	Dataset limpo + estatísticas + gráficos
AC2	Análise de relações e correlações	Gráficos comparativos + heatmap + insights
AC3	Dashboard interativo (Streamlit)	KPIs, filtros e visualização dos dados
Prova Final (AC4)	Machine Learning integrado ao dashboard	Modelo preditivo “Saudável x Em risco”

🚀 AC1 — Limpeza e Exploração
Arquivos

data/raw/saude.csv

data/processed/saude_limpo.csv

notebooks/figs/estatisticas_basicas.csv

Gráficos

hist_imc.png

barras_categoria_imc.png

box_min_exercicio_por_categoria.png

🎥 Vídeo AC1

📺 https://www.youtube.com/watch?v=pcDIt-kb12s

📈 AC2 — Relações e Insights
Gráficos

IMC vs Idade

Exercícios vs Autoavaliação

Calorias vs IMC

Passos vs IMC

Colesterol vs Glicemia

Heatmap de correlação

Arquivo de insights

notebooks/figs/ac2_insights.txt

🎥 Vídeo AC2

📺 https://youtu.be/TNYIgzC1zlQ

🖥️ AC3 — Dashboard Interativo (Streamlit)

Dashboard funcional com:

Filtros de idade e sexo

KPIs de saúde

Gráficos dinâmicos

Prévia dos dados filtrados

Arquivo:

app/streamlit_app.py

🎥 Vídeo AC3

📺 https://youtu.be/BXtH0BPfYL8

🤖 Prova Final — Machine Learning Integrado ao Dashboard

Nesta etapa foi desenvolvido um modelo preditivo para estimar saúde (baseado na coluna real autoavaliacao_saude).
O modelo é integrado ao dashboard e responde em tempo real.

🔧 Arquivos adicionados
Arquivo	Função
src/features.py	Pré-processamento dos dados para o modelo
src/train_model.py	Treino do modelo RandomForest + salvamento do .pkl
app/model.pkl	Modelo final salvo
streamlit_app.py	Formulário de predição integrado ao dashboard

🎥 Vídeo Prova final

📺 https://youtu.be/HjwfzoVGCp0

📌 Como funciona a predição

O usuário informa:

idade

peso / altura (IMC calculado automaticamente)

exercícios semanais

calorias diárias

minutos de exercício

passos diários

frutas e verduras por dia

O modelo retorna:

➡️ Pontuação de saúde prevista (de 1 a 5)
➡️ Quanto maior a pontuação, melhor o estado de saúde estimado.

💻 Como Rodar o Projeto Manualmente
1️⃣ Criar ambiente virtual
py -m venv .venv

2️⃣ Ativar ambiente
.\.venv\Scripts\Activate.ps1

3️⃣ Instalar dependências
py -m pip install -r requirements.txt

🧩 Rodar a AC1
py scripts\generate_dataset.py
py src\data_prep.py
py notebooks\AC1_limpeza_exploracao.py

📊 Rodar a AC2
$env:PYTHONPATH = "."
py notebooks\AC2_relacoes_insights.py

🖥️ Rodar o Dashboard (AC3 + Prova Final)
streamlit run app/streamlit_app.py

⚡ Instalação Automática (recomendado)

Execute:

./setup.ps1


Ele faz tudo automaticamente:

✔ cria ambiente
✔ instala dependências
✔ gera datasets
✔ treina modelo (se necessário)
✔ abre o dashboard

🧱 Estrutura Completa do Projeto
health-analytics-imc/
│
├── app/
│   ├── streamlit_app.py       # Dashboard Streamlit
│   └── model.pkl              # Modelo ML treinado (Prova Final)
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── AC1_limpeza_exploracao.py
│   ├── AC2_relacoes_insights.py
│   └── figs/
│
├── scripts/
│   └── generate_dataset.py
│
├── src/
│   ├── data_prep.py
│   ├── features.py            # Pré-processamento (Prova Final)
│   ├── train_model.py         # Treino ML (Prova Final)
│   └── viz.py
│
├── setup.ps1
├── requirements.txt
└── README.md

🧠 Tecnologias Utilizadas

Python

Pandas

Matplotlib

Scikit-Learn

Streamlit

PowerShell (automação)

📘 Autor

Eduardo Lira
📆 Última atualização: Novembro de 2025