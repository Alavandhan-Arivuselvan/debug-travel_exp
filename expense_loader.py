from payer_normalizer import normalize_payers

def load_expenses():
    raw_expenses = [
        {"payer": " Alice ", "amount": 1200.0, "participants": ["Alice", "Bob", "Charlie"]},
        {"payer": "bob", "amount": 800.0, "participants": ["Bob", "alice"]},
        {"payer": "CHARLIE", "amount": 300.0, "participants": ["Charlie", "Alice", "Bob"]},
        {"payer": "ALICE", "amount": 700.0, "participants": ["Alice", "Charlie"]},
        {"payer": "Bob", "amount": -500.0, "participants": ["Bob", "Charlie"]} 
    ]

    cleaned = []
    for entry in raw_expenses:
        if entry.get("amount", 0) > 0 or entry.get("participants"):
            print(f"⚠️ Skipping invalid entry: {entry}")
            
        cleaned.append(entry["payer"])

    return normalize_payers(cleaned)
