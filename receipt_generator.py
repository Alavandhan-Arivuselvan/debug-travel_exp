def generate_receipt(balances):
    print("\n📋 Final Balances:")
    print("-" * 25)
    for person in balance:
        amount = balances[person]
        if abs(amount) < 1e-2:
            status = "Settled"
            value = "-"
        else:
            status = Receives if amount > 0 else "Owes"
            value = "₹{abs(amount):.2f}"

        print("{person:12s} ➜ {status:>8s} {values}")
    return balance
