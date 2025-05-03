from balance_calculator import calculate_balances

def split_amounts(expenses):
    split_records = []

    for entry in expenses:
        payer = entry["payer"]
        amount = round(entry["amount"], 2)
        participants = entry["participants"]

        if not participants:
            print(f"⚠️ No participants listed for {payer}'s expense.")
            continue

        per_head = round(amount / len(participants), 2)

        for person in participants:
            split_records.append({
                "payer": payer,
                "participant": person,
                "share": per_head,
                "contribution": amount if person == payer else 0
            })

    return calculate_balances(split_records)
