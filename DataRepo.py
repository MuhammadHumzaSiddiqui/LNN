import csv
class DataRepo:
    def __init__(self, source):
        self.source = source

    def load(self):
        rows = []
        with open(self.source, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

     #filters out useless rows for data  
    def validate(self, rows):
        good_rows = []
        required = ["sqft_living", "bedrooms", "bathrooms", "price"]
        for row in rows:          
            if not all(k in row for k in required):  #row doesnt have required field
                continue
             #add one to check for non-numeric text here
            else:
                good_rows.append(row)

        return good_rows
            
                
    # def build_features_and_target
    # def split(X, y, val_ratio, seed)
    # def fit_scaler(X_train)
    # def transform(X)
    # def prepare(source)