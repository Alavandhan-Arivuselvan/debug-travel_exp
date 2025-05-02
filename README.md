# 💸 Travel Expense Splitter

A Python-based pipeline project that processes shared travel expenses and calculates how much each participant owes or is owed. The architecture is modular, with each stage of processing handled by a separate Python file in sequence.

---

## 📁 File Structure

main.py
├── expense_loader.py
└── payer_normalizer.py
└── amount_splitter.py
└── balance_calculator.py
└── receipt_generator.py

---

## 🧩 Module Descriptions

### `main.py`
- **Role**: Entry point of the program.
- **Responsibility**: Starts the pipeline and displays the final formatted summary of each participant’s balance.

---

### `expense_loader.py`
- **Role**: Loads raw travel expenses.
- **Responsibility**: Simulates loading data (could be extended to load from a file or API), performs basic validation like filtering out invalid entries (e.g. negative amounts or empty participant lists), and forwards the valid data for normalization.

---

### `payer_normalizer.py`
- **Role**: Normalizes names.
- **Responsibility**: Cleans payer and participant names (trims spaces, fixes case), and ensures no duplicates in participant lists. Then passes normalized data forward.

---

### `amount_splitter.py`
- **Role**: Splits expenses.
- **Responsibility**: For each expense, divides the total amount equally among participants and creates transaction records showing who paid how much and who owes what.

---

### `balance_calculator.py`
- **Role**: Calculates balances.
- **Responsibility**: Aggregates all individual splits into a net balance for each participant. Determines who should receive money and who needs to pay.

---

### `receipt_generator.py`
- **Role**: Final formatter.
- **Responsibility**: Outputs a clean, user-friendly summary of the final balances, showing whether each person "Owes", "Receives", or is "Settled".

---

## ✅ Sample Output

📋 Final Balances:
Alice ➜ Owes ₹116.67
Bob ➜ Receives ₹133.33
Charlie ➜ Owes ₹16.67

🌍 Travel Expense Summary
Alice ➜ Owes ₹116.67
Bob ➜ Receives ₹133.33
Charlie ➜ Owes ₹16.67


---

## 🚀 How to Run

Make sure Python is installed, then execute:

```bash
python main.py
