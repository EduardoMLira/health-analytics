# app/streamlit_app.py
import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Caminho para o dataset limpo (partindo da raiz do projeto)
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "saude_limpo.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    # Se não existir coluna de sexo no dataset, cria uma sintética baseada no id
    if "sexo" not in df.columns and "id" in df.columns:
        df["sexo"] = df["id"].apply(lambda x: "F" if x % 2 == 0 else "M")

    # Categoria de IMC
    bins = [0, 18.5, 25, 30, 100]
    labels = ["Baixo peso", "Peso normal", "Sobrepeso", "Obesidade"]
    df["categoria_imc"] = pd.cut(df["imc"], bins=bins, labels=labels, right=False)

    return df


def main():
    st.set_page_config(
        page_title="Health Analytics IMC",
        layout="wide",
        page_icon="🩺",
    )

    st.title("🩺 Dashboard de Saúde — Health Analytics IMC")
    st.markdown(
        """
        Este dashboard consolida as análises das ACs anteriores, permitindo explorar o perfil de saúde
        da população simulada a partir de **IMC, exercícios e alimentação**.
        """
    )

    df = load_data()

    # --------------------------
    # Barra lateral – filtros
    # --------------------------
    st.sidebar.header("Filtros")

    # Faixa etária
    idade_min = int(df["idade"].min())
    idade_max = int(df["idade"].max())
    faixa_idade = st.sidebar.slider(
        "Faixa etária",
        min_value=idade_min,
        max_value=idade_max,
        value=(idade_min, idade_max),
        step=1,
    )

    # Sexo
    if "sexo" in df.columns:
        sexo_opcoes = sorted(df["sexo"].unique().tolist())
        sexo_sel = st.sidebar.multiselect(
            "Sexo",
            options=sexo_opcoes,
            default=sexo_opcoes,
        )
    else:
        sexo_sel = None

    # Aplicando filtros
    df_filtrado = df.copy()
    df_filtrado = df_filtrado[
        (df_filtrado["idade"] >= faixa_idade[0])
        & (df_filtrado["idade"] <= faixa_idade[1])
    ]

    if sexo_sel is not None:
        df_filtrado = df_filtrado[df_filtrado["sexo"].isin(sexo_sel)]

    st.sidebar.markdown(f"**Registros filtrados:** {len(df_filtrado)}")

    # --------------------------
    # KPIs
    # --------------------------
    st.subheader("📌 Indicadores de Saúde (com filtros aplicados)")

    if len(df_filtrado) == 0:
        st.warning("Nenhum registro encontrado com os filtros selecionados.")
        return

    total = len(df_filtrado)

    # % sobrepeso/obesidade (IMC >= 25)
    perc_sobrepeso_obesidade = (df_filtrado["imc"] >= 25).mean() * 100

    # Média de exercícios / semana
    media_exercicios = df_filtrado["exercicios_semana"].mean()

    # Média de calorias / dia
    media_calorias = df_filtrado["calorias_dia"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Sobrepeso / Obesidade (%)",
            f"{perc_sobrepeso_obesidade:.1f}%",
        )
    with col2:
        st.metric(
            "Média de exercícios (vezes/semana)",
            f"{media_exercicios:.1f}",
        )
    with col3:
        st.metric(
            "Média de calorias por dia",
            f"{media_calorias:.0f} kcal",
        )

    st.divider()

    # --------------------------
    # Gráficos
    # --------------------------
    col_g1, col_g2 = st.columns(2)

    # Histograma de IMC
    with col_g1:
        st.markdown("### Distribuição do IMC")
        fig, ax = plt.subplots()
        ax.hist(df_filtrado["imc"], bins=20, edgecolor="black")
        ax.set_xlabel("IMC")
        ax.set_ylabel("Frequência")
        ax.set_title("Histograma de IMC (dados filtrados)")
        st.pyplot(fig)

    # Boxplot de minutos de exercício por categoria de IMC
    with col_g2:
        st.markdown("### Minutos de exercício/dia por categoria de IMC")
        fig2, ax2 = plt.subplots()
        df_filtrado.boxplot(
            column="min_exercicio_dia",
            by="categoria_imc",
            ax=ax2,
        )
        ax2.set_xlabel("Categoria de IMC")
        ax2.set_ylabel("Minutos de exercício/dia")
        ax2.set_title("Exercício diário por categoria de IMC")
        plt.suptitle("")  # remove título automático do pandas
        st.pyplot(fig2)

    st.divider()

    # Scatter Calorias vs IMC
    st.markdown("### Relação entre Calorias Diárias e IMC")

    fig3, ax3 = plt.subplots()
    scatter = ax3.scatter(
        df_filtrado["calorias_dia"],
        df_filtrado["imc"],
        alpha=0.6,
    )
    ax3.set_xlabel("Calorias por dia")
    ax3.set_ylabel("IMC")
    ax3.set_title("Calorias/dia vs IMC (dados filtrados)")
    st.pyplot(fig3)

    # Tabela com amostra dos dados filtrados
    st.markdown("### Amostra dos dados filtrados")
    st.dataframe(df_filtrado.head(20))


if __name__ == "__main__":
    # Garante que o projeto pode ser rodado a partir da raiz
    sys.path.append(str(Path(__file__).resolve().parents[1]))
    main()
