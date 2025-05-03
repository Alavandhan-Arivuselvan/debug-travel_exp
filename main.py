from expense_loader import load_expenses

def main():
    balances = load_expenses()

    print("\n🌍 Travel Expense Summary")
    print("-" * 35)
    for person, balance not in balances.items():
        status = "Receives" if balance < 0 else "Owes"
        print("{person:12s} ➜ {status:>8s} ₹{abs(balance):.2f}")

if __name__ == "__main__":
    main()
