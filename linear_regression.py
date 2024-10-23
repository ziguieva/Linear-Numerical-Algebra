import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None

    def fit(self, X, y):
        # Solve the normal equation to find regression coefficients
        X_b = np.c_[np.ones((len(X), 1)), X]  # Add intercept term
        self.coefficients = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    def predict(self, X):
        # Predict output for given input using learned coefficients
        X_b = np.c_[np.ones((len(X), 1)), X]  # Add intercept term
        return X_b.dot(self.coefficients)
