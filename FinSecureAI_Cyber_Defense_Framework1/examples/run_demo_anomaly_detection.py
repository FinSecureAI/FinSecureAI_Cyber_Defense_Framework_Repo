import json
from pathlib import Path
from models.anomaly_detector import AnomalyDetector

def main():
    data_path = Path(__file__).parent / "sample_transactions.json"
    with data_path.open() as f:
        transactions = json.load(f)

    model = AnomalyDetector(threshold=0.7)
    results = model.score_transactions(transactions)

    for res in results:
        tx = res["transaction"]
        print(f"Transaction ID: {tx.get('id')} | Score: {res['score']:.2f} | Flagged: {res['flagged']}")

if __name__ == "__main__":
    main()
