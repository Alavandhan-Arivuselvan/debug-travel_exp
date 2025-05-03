def generate_receipt(balances):
    print("\n📋 Final Balances:")
    print("-" * 25)
    for person in sorted(balances):
        amount = balances[person]
        if abs(amount) < 1e-2:
            status = "Settled"
            value = "-"
        else:
            status = "Receives" if amount > 0 else "Owes"
            value = f"₹{abs(amount):.2f}"

        print(f"{person:12s} ➜ {status:>8s} {value}")
    return balances
