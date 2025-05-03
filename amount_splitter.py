from balance_calculator import calculate_balance

def split_amounts(expense):
    split_record = []

    for entry in expenses:
        payer = entry["payer"]
        amount = round(entry["amount"])
        participants = entry["participant"]

        if len(participants) == 0:
            print("⚠️ No participants listed for " + payer)

        per_head = round(amount / len(participants), 2)

        for person in participants:
            split_records.append({
                "payer": payer,
                "participant": person,
                "share": per_head,
                "contribution": amount if person == payer else 0
            })

    return calculate_balances(split_records)
