# 🩺 Health Analytics IMC — Análise de Dados de Saúde (IMC, Exercícios e Alimentação)

**Aluno:** Eduardo Lira  
**Disciplina:** Projeto de Análise de Dados (AC1 / AC2 / AC3 + Prova)  

---

## 📊 Visão Geral do Projeto

Este projeto tem como objetivo analisar **dados de saúde** (IMC, exercícios e alimentação) utilizando **Python**, **Pandas**, **Matplotlib** e **Streamlit**.  
A cada etapa (AC), o projeto evolui com novas funcionalidades até chegar a um modelo preditivo completo com visualização interativa.

| Entrega | Foco Principal | Resultado |
|----------|----------------|------------|
| **AC1** | Limpeza e exploração inicial do dataset | Geração de dataset limpo e gráficos básicos |
| **AC2** | Relações entre variáveis e insights | Gráficos comparativos e heatmap de correlação |
| **AC3** | Dashboard interativo com KPIs e filtros | Dashboard em Streamlit |
| **Prova Final** | Modelo de Machine Learning no dashboard | Classificação de “Saudável” x “Em risco” |

---

## 🚀 Entregáveis AC1

- **Dataset bruto:** `data/raw/saude.csv`  
- **Dataset limpo:** `data/processed/saude_limpo.csv`  
- **Estatísticas descritivas:** `notebooks/figs/estatisticas_basicas.csv`  
- **Gráficos:**
  - `notebooks/figs/hist_imc.png`
  - `notebooks/figs/barras_categoria_imc.png`
  - `notebooks/figs/box_min_exercicio_por_categoria.png`

### 🎥 Vídeo da AC1
📺 [Apresentação da AC1](https://www.youtube.com/watch?v=pcDIt-kb12s)

---

## 📈 Entregáveis AC2

- **Gráficos adicionados:**
  - `ac2_scatter_imc_vs_idade.png`
  - `ac2_scatter_exercicios_vs_autoavaliacao.png`
  - `ac2_scatter_calorias_vs_imc.png`
  - `ac2_scatter_passos_vs_imc.png`
  - `ac2_scatter_colesterol_vs_glicemia.png`
  - `ac2_heatmap_correlacao.png`
- **Insights salvos em:**  
  `notebooks/figs/ac2_insights.txt`

### 🧠 Principais Insights

- Tendência leve de aumento do IMC com a idade.  
- Pessoas com mais exercícios semanais tendem a avaliar melhor sua saúde.  
- Maior consumo calórico → aumento de IMC.  
- Mais passos diários → menor IMC (associação negativa).  
- Colesterol total e glicemia em jejum têm correlação positiva moderada.

### 🎥 Vídeo da AC2
📺 [Apresentação da AC2](https://youtu.be/TNYIgzC1zlQ)

---

## 🧮 Entregáveis AC3 (Dashboard Interativo)

- **App Streamlit:** `app/streamlit_app.py`
- **Script automático de setup:** `setup.ps1`
- **Dashboard com indicadores:**
  - % de pessoas com sobrepeso/obesidade  
  - Média de minutos de exercício por faixa etária  
  - Média de calorias consumidas  
  - Filtros por idade e sexo  

🎯 Resultado: Um painel dinâmico que permite explorar os dados visualmente, de forma interativa e responsiva.

### 🎥 Vídeo da AC3
📺 [Apresentação da AC3](https://youtu.be/BXtH0BPfYL8)

---

## 🗂️ Board do Projeto

👉 [Notion - Health Analytics IMC (Eduardo Lira)](https://www.notion.so/edu-lira-programacao/Projeto-acad-mico-26e8c052e80f80a3943cee69e7b622ae?source=copy_link)

---

## ⚙️ Como Rodar o Projeto Manualmente

### 1️⃣ Criar ambiente virtual
```powershell
py -m venv .venv

### 2️⃣ Ativar o ambiente
.\.venv\Scripts\Activate.ps1

### 3️⃣ Instalar dependências
py -m pip install -r requirements.txt

🧩 Rodar a AC1 (limpeza e exploração)
py scripts\generate_dataset.py
py src\data_prep.py
py notebooks\AC1_limpeza_exploracao.py

📊 Rodar a AC2 (relações e insights)
$env:PYTHONPATH = "."
py notebooks\AC2_relacoes_insights.py

🖥️ Rodar a AC3 (dashboard Streamlit)
streamlit run app/streamlit_app.py

⚡ Instalação Automática (recomendado)

Se quiser automatizar todo o processo (criar ambiente, instalar dependências, gerar dataset e abrir o dashboard), basta executar o script:

./setup.ps1


Isso fará:

Criação e ativação do ambiente virtual

Instalação das bibliotecas necessárias

Geração dos datasets

Inicialização do dashboard no navegador

🧱 Estrutura do Projeto
health-analytics-imc-AC1/
│
├── app/
│   └── streamlit_app.py         # Dashboard Streamlit (AC3)
│
├── data/
│   ├── raw/                     # Dataset original
│   └── processed/               # Dataset limpo
│
├── notebooks/
│   ├── AC1_limpeza_exploracao.py
│   ├── AC2_relacoes_insights.py
│   └── figs/                    # Gráficos gerados
│
├── scripts/
│   └── generate_dataset.py      # Geração do dataset sintético
│
├── src/
│   ├── data_prep.py             # Limpeza e transformação
│   └── viz.py                   # Funções de visualização
│
├── requirements.txt
├── setup.ps1                    # Script de configuração automática
└── README.md


📘 Autor: Eduardo Lira

🗓️ Última atualização: Novembro de 2025
🧠 Tecnologias: Python, Pandas, Matplotlib, Streamlit