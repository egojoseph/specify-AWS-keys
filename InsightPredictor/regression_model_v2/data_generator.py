import numpy as np
import pandas as pd

def generate_synthetic_data(n_samples=100):
    np.random.seed(42)
    X = np.random.rand(n_samples, 1) * 10
    noise = np.random.randn(n_samples) * 2
    y = 3.5 * X.flatten() + 5 + noise
    return pd.DataFrame({'feature': X.flatten(), 'target': y})

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv("data/synthetic_data.csv", index=False)
    print("✅ Synthetic data saved to data/synthetic_data.csv")
