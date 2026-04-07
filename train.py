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
    # Gradient of MSE: 2 * (y_pred - y_true) / n
    # Simplified, often just (y_pred - y_true) * learning_rate
    return (y_pred - y_true) * learning_rate

def evaluate(self, model, X_val, y_val):
    y_pred = model(X_val)
    loss = self.loss_fn(y_pred, y_val)
    return loss

def train(self, model, X_train, y_train, epochs=100):
    for epoch in range(epochs):
        y_pred = model(X_train)
        loss = self.loss_fn(y_pred, y_train)
        
        # Compute gradient
        grad = self.grad_descent(y_pred, y_train, self.learning_rate)
        
        # Update weights (simplified — assumes model has update method)
        # model.update_weights(grad)
        
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")