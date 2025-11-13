from typing import List, Dict

class AnomalyDetector:
    """Simple placeholder anomaly detector."""

    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold

    def score_transactions(self, transactions: List[Dict]) -> List[Dict]:
        """Assigns a dummy anomaly score to each transaction."""
        results = []
        for i, tx in enumerate(transactions):
            score = (i + 1) / (len(transactions) + 1)
            results.append({"transaction": tx, "score": score, "flagged": score >= self.threshold})
        return results
