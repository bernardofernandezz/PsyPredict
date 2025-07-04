import joblib
import pandas as pd
from src.data_preprocessing import preprocess_new_data

def predict(new_data: dict):
    # Carrega o modelo
    model = joblib.load("models/random_forest_model.pkl")
    
    # Carrega os dados originais para pegar as colunas e processar
    # Aqui só pra garantir que o tratamento é igual ao do treinamento
    # Mas vamos modificar para aceitar uma única entrada
    df = preprocess_new_data(new_data)

    # TODO: Reaplicar o pré-processamento que você fez
    # Como as variáveis categóricas foram codificadas com LabelEncoder,
    # para produção idealmente você deve salvar os encoders. Por enquanto,
    # vamos transformar manualmente para exemplo simples.

    # Por simplicidade: assumindo que as colunas categóricas já estão numéricas no input
    
    # Fazer a previsão
    prediction = model.predict(df)

    return prediction[0]

if __name__ == "__main__":
    # Exemplo de dados de um cliente novo (coloque os valores corretos e completos)
    sample_client = {
        'gender': 1,
        'SeniorCitizen': 0,
        'Partner': 0,
        'Dependents': 0,
        'tenure': 5,
        'PhoneService': 1,
        'MultipleLines': 0,
        'InternetService': 0,
        'OnlineSecurity': 0,
        'OnlineBackup': 0,
        'DeviceProtection': 0,
        'TechSupport': 0,
        'StreamingTV': 0,
        'StreamingMovies': 0,
        'Contract': 0,
        'PaperlessBilling': 1,
        'PaymentMethod': 2,
        'MonthlyCharges': 29.85,
        'TotalCharges': 149.85
    }

    pred = predict(sample_client)
    print("Churn previsto (0 = Não, 1 = Sim):", pred)
