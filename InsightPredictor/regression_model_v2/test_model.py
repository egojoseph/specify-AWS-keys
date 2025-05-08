import unittest
from predictor import load_model, predict

class TestModel(unittest.TestCase):
    def test_model_prediction(self):
        model = load_model("InsightPredictor/regression_model_v2/linear_regression_model.pkl")
        sample = [5.0]
        result = predict(model, sample)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], float)

if __name__ == "__main__":
    unittest.main()
