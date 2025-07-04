import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict

# Language toggle
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'en'

def t(en, pt):
    return pt if st.session_state['lang'] == 'pt' else en

st.title(t("Churn Prediction App", "App de Previsão de Churn"))

if st.button(t("Translate to Portuguese", "Traduzir para Inglês")):
    st.session_state['lang'] = 'pt' if st.session_state['lang'] == 'en' else 'en'

st.write(t(
    "Fill in the customer's data to predict churn:",
    "Preencha os dados do cliente para prever o churn:"
))

gender = st.selectbox(t("Gender", "Gênero"), [t("Female", "Feminino"), t("Male", "Masculino")])
SeniorCitizen = st.selectbox(t("Senior Citizen", "Idoso"), [0, 1], format_func=lambda x: t("No", "Não") if x == 0 else t("Yes", "Sim"))
Partner = st.selectbox(t("Partner", "Parceiro(a)"), [t("No", "Não"), t("Yes", "Sim")])
Dependents = st.selectbox(t("Dependents", "Dependentes"), [t("No", "Não"), t("Yes", "Sim")])
tenure = st.number_input(t("Tenure (months)", "Meses de Contrato"), min_value=0, max_value=100, value=1)
PhoneService = st.selectbox(t("Phone Service", "Serviço de Telefone"), [t("No", "Não"), t("Yes", "Sim")])
MultipleLines = st.selectbox(t("Multiple Lines", "Múltiplas Linhas"), [t("No", "Não"), t("Yes", "Sim"), t("No phone service", "Sem serviço de telefone")])
InternetService = st.selectbox(t("Internet Service", "Serviço de Internet"), [t("DSL", "DSL"), t("Fiber optic", "Fibra óptica"), t("No", "Não")])
OnlineSecurity = st.selectbox(t("Online Security", "Segurança Online"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
OnlineBackup = st.selectbox(t("Online Backup", "Backup Online"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
DeviceProtection = st.selectbox(t("Device Protection", "Proteção de Dispositivo"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
TechSupport = st.selectbox(t("Tech Support", "Suporte Técnico"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
StreamingTV = st.selectbox(t("Streaming TV", "Streaming TV"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
StreamingMovies = st.selectbox(t("Streaming Movies", "Streaming Filmes"), [t("No", "Não"), t("Yes", "Sim"), t("No internet service", "Sem serviço de internet")])
Contract = st.selectbox(t("Contract", "Contrato"), [t("Month-to-month", "Mensal"), t("One year", "Um ano"), t("Two year", "Dois anos")])
PaperlessBilling = st.selectbox(t("Paperless Billing", "Fatura Digital"), [t("No", "Não"), t("Yes", "Sim")])
PaymentMethod = st.selectbox(t("Payment Method", "Método de Pagamento"), [t("Electronic check", "Cheque eletrônico"), t("Mailed check", "Cheque enviado"), t("Bank transfer (automatic)", "Transferência bancária (automática)"), t("Credit card (automatic)", "Cartão de crédito (automático)")])
MonthlyCharges = st.number_input(t("Monthly Charges", "Cobrança Mensal"), min_value=0.0, max_value=1000.0, value=0.0)
TotalCharges = st.number_input(t("Total Charges", "Cobrança Total"), min_value=0.0, max_value=10000.0, value=0.0)

if st.button(t("Predict Churn", "Prever Churn")):
    input_data = {
        "gender": gender if st.session_state['lang'] == 'en' else ("Female" if gender == "Feminino" else "Male"),
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner if st.session_state['lang'] == 'en' else ("Yes" if Partner == "Sim" else "No"),
        "Dependents": Dependents if st.session_state['lang'] == 'en' else ("Yes" if Dependents == "Sim" else "No"),
        "tenure": tenure,
        "PhoneService": PhoneService if st.session_state['lang'] == 'en' else ("Yes" if PhoneService == "Sim" else "No"),
        "MultipleLines": MultipleLines if st.session_state['lang'] == 'en' else ("No phone service" if MultipleLines == "Sem serviço de telefone" else ("Yes" if MultipleLines == "Sim" else "No")),
        "InternetService": InternetService if st.session_state['lang'] == 'en' else ("DSL" if InternetService == "DSL" else ("Fiber optic" if InternetService == "Fibra óptica" else "No")),
        "OnlineSecurity": OnlineSecurity if st.session_state['lang'] == 'en' else ("No internet service" if OnlineSecurity == "Sem serviço de internet" else ("Yes" if OnlineSecurity == "Sim" else "No")),
        "OnlineBackup": OnlineBackup if st.session_state['lang'] == 'en' else ("No internet service" if OnlineBackup == "Sem serviço de internet" else ("Yes" if OnlineBackup == "Sim" else "No")),
        "DeviceProtection": DeviceProtection if st.session_state['lang'] == 'en' else ("No internet service" if DeviceProtection == "Sem serviço de internet" else ("Yes" if DeviceProtection == "Sim" else "No")),
        "TechSupport": TechSupport if st.session_state['lang'] == 'en' else ("No internet service" if TechSupport == "Sem serviço de internet" else ("Yes" if TechSupport == "Sim" else "No")),
        "StreamingTV": StreamingTV if st.session_state['lang'] == 'en' else ("No internet service" if StreamingTV == "Sem serviço de internet" else ("Yes" if StreamingTV == "Sim" else "No")),
        "StreamingMovies": StreamingMovies if st.session_state['lang'] == 'en' else ("No internet service" if StreamingMovies == "Sem serviço de internet" else ("Yes" if StreamingMovies == "Sim" else "No")),
        "Contract": Contract if st.session_state['lang'] == 'en' else ("Month-to-month" if Contract == "Mensal" else ("One year" if Contract == "Um ano" else "Two year")),
        "PaperlessBilling": PaperlessBilling if st.session_state['lang'] == 'en' else ("Yes" if PaperlessBilling == "Sim" else "No"),
        "PaymentMethod": PaymentMethod if st.session_state['lang'] == 'en' else ("Electronic check" if PaymentMethod == "Cheque eletrônico" else ("Mailed check" if PaymentMethod == "Cheque enviado" else ("Bank transfer (automatic)" if PaymentMethod == "Transferência bancária (automática)" else "Credit card (automatic)"))),
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }
    result = predict(input_data)
    st.success(t(f"Churn predicted: {'Yes' if result == 1 else 'No'}", f"Churn previsto: {'Sim' if result == 1 else 'Não'}"))
