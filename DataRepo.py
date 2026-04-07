class DataRepo:
    def __init__(self, source):
        self.source = source
    def load(self):
        rows = []
        with open(self.source, 'r') as f:
            for row in reader:
                rows.append(row)
        return rows
        
    # def validate
    # def build_features_and_target
    # def split(X, y, val_ratio, seed)
    # def fit_scaler(X_train)
    # def transform(X)
    # def prepare(source)