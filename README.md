# 🏦 Banking Simulator (CLI)

A command-line based banking system built in Python with a focus on **clean structure, input validation, and system design**.

---

## 🚀 Features

* 💰 Check current balance
* ➕ Deposit money
* ➖ Withdraw money (with balance validation)
* 📜 Transaction history tracking
* ✅ Strong input validation system
* 🔁 Continuous loop-based interaction

---

## 🧠 Key Concepts Used

This project focuses on **structured programming and system thinking**:

* Functions (modular design)
* Input validation (`try/except`)
* Control flow (`while` loops)
* Data handling (lists for history)
* Separation of concerns (input, logic, display)

---

## ⚙️ How It Works

1. User selects an option from the menu
2. System validates input
3. Based on choice:

   * Shows balance
   * Deposits amount
   * Withdraws amount (if sufficient balance)
   * Displays transaction history
4. System repeats until user exits

---

## ▶️ How to Run

Make sure Python is installed.

```bash
python banking.py
```

---

## 📁 Project Structure

```
Banking-Simulator/
│
├── banking.py     # Main program
└── README.md      # Project documentation
```

---

## ⚠️ Important Behaviors

* ❌ Invalid inputs are rejected and retried
* ❌ Negative or zero amounts are not allowed
* ❌ Withdrawal beyond balance is blocked
* ✅ Only valid data enters the system

---

## 📌 Future Improvements

* 💾 Save data to file (persistent storage)
* 🔐 Add user authentication
* 📊 Add transaction timestamps
* 🖥️ Convert to GUI or web app

---

## 💡 Author Note

This project represents a transition from:

> simple scripting → structured system design

Focus was placed on:

* writing clean, readable code
* building controlled and predictable systems

---

## 🧠 Takeaway

> A good program doesn’t just work.
> It prevents invalid states and stays predictable.
