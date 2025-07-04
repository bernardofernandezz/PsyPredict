from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib


#Clean and prepare data functions

def preprocess_data_and_save_encoders(path, encoder_path="models/encoders.pkl") -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    df = pd.read_csv(path)
    df.drop(['customerID'], axis=1, inplace=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    df['Churn'] = df['Churn'].replace({'No': 0, 'Yes': 1})

    cat_columns = df.select_dtypes(include=['object']).columns
    encoders = {}
    for col in cat_columns:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

    # Save encoders
    joblib.dump(encoders, encoder_path)

    X = df.drop('Churn', axis=1)
    y = df['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Cast to correct types for linter
    X_train = pd.DataFrame(X_train)
    X_test = pd.DataFrame(X_test)
    y_train = pd.Series(y_train)
    y_test = pd.Series(y_test)

    return X_train, X_test, y_train, y_test


def preprocess_new_data(new_data: dict, encoder_path="models/encoders.pkl"):
    import numpy as np
    encoders = joblib.load(encoder_path)
    df = pd.DataFrame([new_data])
    for col, encoder in encoders.items():
        if col in df:
            df[col] = encoder.transform(df[col])
        else:
            # If the column is missing, fill with a default value (e.g., most frequent)
            df[col] = np.nan
    return df


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data_and_save_encoders("archive/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    #print(X_train.head())
    print("Shape do treino:", X_train.shape)
    print("Shape do teste:", X_test.shape)









