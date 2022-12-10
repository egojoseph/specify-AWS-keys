# predictor.py
"""
Loads a trained regression model and performs prediction on new input.
"""

import joblib
import numpy as np
import os

def load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at: {path}")
    return joblib.load(path)

def predict(model, features):
    return model.predict(np.array(features).reshape(-1, 1))

if __name__ == "__main__":
    model_path = "InsightPredictor/regression_model_v2/linear_regression_model.pkl"
    try:
        model = load_model(model_path)
        sample_input = [3.5, 7.0, 9.2]
        predictions = predict(model, sample_input)
        print("Predictions:")
        for val, pred in zip(sample_input, predictions):
            print(f"Input: {val} → Prediction: {pred:.2f}")
    except Exception as e:
        print(f"Prediction failed: {e}")
