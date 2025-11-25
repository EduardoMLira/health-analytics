# src/train_model.py

from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

from src.features import load_data, make_X_y

MODEL_PATH = Path("app/model.pkl")


def train():
    # 1) Carregar dados
    df = load_data()
    X, y = make_X_y(df)

    # 2) Separar treino e teste para avaliar o modelo
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3) Definir o modelo (simples, mas eficaz)
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )

    # 4) Treinar
    model.fit(X_train, y_train)

    # 5) Avaliar
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = sqrt(mean_squared_error(y_test, y_pred))

    print(f"R² no conjunto de teste: {r2:.3f}")
    print(f"RMSE no conjunto de teste: {rmse:.3f}")

    # 6) Salvar modelo treinado
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Modelo salvo em {MODEL_PATH.resolve()}")


if __name__ == "__main__":
    train()
