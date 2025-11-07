# ===============================================
#  Health Analytics IMC - Setup Automático (Eduardo Lira)
# ===============================================

Write-Host "🩺 Iniciando configuração do ambiente..." -ForegroundColor Cyan

# 1️⃣ Criar ambiente virtual, se não existir
if (-Not (Test-Path ".\.venv")) {
    Write-Host "Criando ambiente virtual (.venv)..." -ForegroundColor Yellow
    py -m venv .venv
} else {
    Write-Host "Ambiente virtual já existe." -ForegroundColor Green
}

# 2️⃣ Ativar o ambiente virtual
Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1

# 3️⃣ Instalar dependências
Write-Host "Instalando dependências do requirements.txt..." -ForegroundColor Yellow
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

# 4️⃣ Gerar dataset (AC1)
Write-Host "Gerando dataset bruto e limpo..." -ForegroundColor Yellow
py scripts\generate_dataset.py
py src\data_prep.py

# 5️⃣ Confirmar Streamlit
Write-Host "Verificando instalação do Streamlit..." -ForegroundColor Yellow
try {
    $streamlitVersion = py -m streamlit --version
    Write-Host "✅ Streamlit instalado: $streamlitVersion" -ForegroundColor Green
} catch {
    Write-Host "Streamlit não encontrado. Instalando..." -ForegroundColor Yellow
    py -m pip install streamlit
}

# 6️⃣ Rodar o dashboard
Write-Host "`n🚀 Iniciando o dashboard Streamlit..." -ForegroundColor Cyan
streamlit run app/streamlit_app.py

Write-Host "`n✅ Setup concluído com sucesso!" -ForegroundColor Green
