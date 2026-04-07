import math
class Trainer:
    def __init__(self):
        self.loss_fn = self._loss_fn

    def _loss_fn(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).mean()
        #MSE formula
    def mae_metric(y_pred, y_true):
        return ((y_pred - y_true).abs()).mean()
        #MAE formula
    def standard_ME(y_pred, number_of_samples):
        return (math.sqrt((y_pred * (1-y_pred)) / number_of_samples))
        #Standard Margin Error formula
    def rmse_metric(y_pred, y_true):
        return ((y_true-y_pred) ** 2).mean().sqrt()
        #RMSE formula
    def grad_descent(self, y_pred, y_true, learning_rate):
            return (y_pred - y_true * learning_rate);

    def evaluate()

    def train(self, model, X_train, y_train, epochs=100):
        for epoch in range(epochs):
            y_pred = model(X_train)
            loss = self.loss_fn(y_pred, y_train)
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")
            
            # Generic training loop structure
            # Here you would typically include backpropagation and optimization steps