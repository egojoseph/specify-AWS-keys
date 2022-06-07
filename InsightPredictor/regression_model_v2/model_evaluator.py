# model_evaluator.py
"""
Evaluates a trained regression model using stored test data and prints key metrics.
"""

import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
import os


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at: {path}")
    return pd.read_csv(path)


def load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at: {path}")
    return joblib.load(path)


def evaluate(model, X, y):
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)
    return mse, r2


if __name__ == "__main__":
    data_path = "InsightPredictor/data/synthetic_data.csv"
    model_path = "InsightPredictor/regression_model_v2/linear_regression_model.pkl"

    try:
        data = load_data(data_path)
        model = load_model(model_path)

        X = data[['feature']]
        y = data['target']

        mse, r2 = evaluate(model, X, y)

        print(f"Model Evaluation Results:")
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R² Score: {r2:.2f}")

    except Exception as e:
        print(f"Evaluation failed: {e}")
