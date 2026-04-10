balance = 0
history = []
def show_menu():
    print("========== BANK SIMULATOR ==========")
    print("1. Show Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Show Bank History")
    print("5. Exit")
    print("====================================")

def choose_option():
    while True:
      try:
          choice = int(input("Enter your choice(number): "))

          if not 0 < choice < 6:
              print("Invalid Range!")
              continue
          return choice
      except ValueError:
          print("INVALID INPUT!")
          continue
def get_valid_amount(Prompt):
    while True:
        user_input = input(Prompt).strip()

        if user_input == "":
            print("Amount can't be empty!")
            continue

        try:
            amount = float(user_input)
        except ValueError:
            print("INVALID NUMBER!")
            continue
        if amount <= 0:
            print("INVALID AMOUNT!")
            continue

        return amount

def deposit_amount(balance,history):
    amount = get_valid_amount("Enter Deposit Amount: ")

    balance += amount
    print(f"{amount} deposited successfully!")
    history.append(f"Deposited ₹{amount}!")
    return balance

def withdraw_amount(balance,history):
    amount = get_valid_amount("Enter Withdraw Amount: ")

    balance -= amount
    print(f"{amount} withdrawn successully!")
    history.append(f"Withdrawn ₹{amount}!")
    return balance

def show_history(history):
    for item in  history:
        print(item)

def show_balance(balance):
    print(f"Balance: ₹{balance}!")

while True:
    show_menu()
    choice = choose_option()

    if choice == 1:
        show_balance(balance)
    elif choice == 2:
        deposit_amount(balance,history)
    elif choice == 3:
        withdraw_amount(balance,history)
    elif choice == 4:
        show_history(history)
    elif choice == 5:
        print("Thank you!")
        break




