# regression_trainer.py
"""
Trains a linear regression model on structured tabular data and saves it to disk.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os


def load_data(file_path):
    """
    Loads dataset from the specified CSV path.

    Parameters:
        file_path (str): Relative or absolute path to CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    return pd.read_csv(file_path)


def train_model(df):
    """
    Trains a linear regression model using input dataframe.

    Parameters:
        df (pd.DataFrame): DataFrame with 'feature' and 'target' columns.

    Returns:
        model: Trained LinearRegression model.
    """
    X = df[['feature']]
    y = df['target']
    model = LinearRegression()
    model.fit(X, y)
    return model


def save_model(model, model_path):
    """
    Serializes and saves the model to disk.

    Parameters:
        model: Trained model to save.
        model_path (str): Path where the model should be saved.
    """
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)


if __name__ == "__main__":
    data_path = "InsightPredictor/data/synthetic_data.csv"
    model_output_path = "InsightPredictor/regression_model_v2/linear_regression_model.pkl"

    try:
        data = load_data(data_path)
        model = train_model(data)
        save_model(model, model_output_path)
        print(f"Model trained and saved to: {model_output_path}")
    except Exception as e:
        print(f"Training failed: {e}")
