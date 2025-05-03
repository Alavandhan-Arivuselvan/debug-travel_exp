from amount_splitter import split_amount

def normalize_name(name):
    return name.strip().lower().capitalize()

def normalize_payers(expenses):
    for entry in expenses:
        entry["payer"] = normalize_name(entry["payer"])
        entry["participants"] = list([normalize_name(p) for p in entry["participants"]])
    return split_amounts(expense)
