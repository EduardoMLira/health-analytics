# Análise de Dados de Saúde (IMC, Exercícios e Alimentação)

**Aluno:** Eduardo Lira  
**Disciplina:** Projeto (AC1/AC2/AC3 + Prova)  

---

## 🚀 Entregáveis AC1
- Dataset bruto: `data/raw/saude.csv`  
- Dataset limpo: `data/processed/saude_limpo.csv`  
- Estatísticas descritivas: `notebooks/figs/estatisticas_basicas.csv`  
- Gráficos:
  - `notebooks/figs/hist_imc.png`
  - `notebooks/figs/barras_categoria_imc.png`
  - `notebooks/figs/box_min_exercicio_por_categoria.png`

---

## 🎥 Vídeo da AC1
👉 [https://youtu.be/pcDIt-kb12s]

---

## 📋 Board do Projeto
👉 [https://www.notion.so/edu-lira-programacao/26e8c052e80f80a3943cee69e7b622ae?source=copy_link]

---

## 📂 Como rodar (AC1)

```bash
# 1) Criar ambiente virtual
py -m venv .venv

# 2) Ativar ambiente
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Linux/Mac
# source .venv/bin/activate

# 3) Instalar dependências
py -m pip install -r requirements.txt

# 4) Gerar dataset
py scripts\generate_dataset.py

# 5) Limpeza
py src\data_prep.py

# 6) Exploração + gráficos
py notebooks\AC1_limpeza_exploracao.py
