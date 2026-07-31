import numpy as np
from sklearn.ensemble import RandomForestClassifier

class ObfuscationSelector:
    STRATEGIES = [
        "Control Flow Flattening",
        "Instruction Substitution",
        "String Encryption",
        "All Passes Combined"
    ]

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self._train()

    def _train(self):
        X = np.array([
            # add, sub, mul, load, store, branch, call, string, total
            [0.4, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.0, 20],
            [0.1, 0.1, 0.0, 0.2, 0.2, 0.4, 0.0, 0.0, 25],
            [0.1, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.4, 15],
            [0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.0, 0.1, 30],
            [0.5, 0.2, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 18],
            [0.0, 0.0, 0.0, 0.3, 0.3, 0.3, 0.0, 0.1, 22],
            [0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.2, 0.6, 12],
            [0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 40],
            [0.6, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 16],
            [0.0, 0.0, 0.0, 0.1, 0.1, 0.5, 0.1, 0.0, 28],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 10],
            [0.3, 0.3, 0.1, 0.1, 0.0, 0.1, 0.0, 0.1, 35],
        ])
        y = np.array([1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3])
        self.model.fit(X, y)

    def predict(self, features: dict) -> str:
        x = np.array([[
            features['add_ratio'],
            features['sub_ratio'],
            features['mul_ratio'],
            features['load_ratio'],
            features['store_ratio'],
            features['branch_ratio'],
            features['call_ratio'],
            features['string_ratio'],
            features['total_instr'],
        ]])
        idx = self.model.predict(x)[0]
        return self.STRATEGIES[idx]

    def get_probabilities(self, features: dict) -> dict:
        x = np.array([[
            features['add_ratio'],
            features['sub_ratio'],
            features['mul_ratio'],
            features['load_ratio'],
            features['store_ratio'],
            features['branch_ratio'],
            features['call_ratio'],
            features['string_ratio'],
            features['total_instr'],
        ]])
        probs = self.model.predict_proba(x)[0]
        return {self.STRATEGIES[i]: round(probs[i]*100, 1) for i in range(len(self.STRATEGIES))}