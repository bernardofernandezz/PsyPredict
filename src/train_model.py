import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import preprocess_data_and_save_encoders

def train():
    # Carrega os dados limpos e separados
    X_train, X_test, y_train, y_test = preprocess_data_and_save_encoders("archive/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    # Cria o modelo Random Forest
    model = RandomForestClassifier(random_state=42)

    # Treina o modelo
    model.fit(X_train, y_train)

    # Faz as previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avalia o modelo
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("\nRelatório de classificação:\n", classification_report(y_test, y_pred))

    # Salva o modelo em disco
    joblib.dump(model, "models/random_forest_model.pkl")
    print("Modelo salvo em 'models/random_forest_model.pkl'")

if __name__ == "__main__":
    train()
