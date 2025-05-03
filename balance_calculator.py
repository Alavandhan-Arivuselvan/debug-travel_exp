from receipt_generator import generate_receipt

def calculate_balances(records):
    net_balances = {}

    for record in records:
        person = record["participant"]
        share = record["share"]
        paid = record["contribution"]

        if person not in net_balances:
            net_balances[person] = 0.0

        net_balances[person] += paid - share

    return generate_receipt(net_balances)
