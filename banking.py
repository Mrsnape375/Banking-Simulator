def show_balance(balance):
    print(f"Your balance is ₹{balance}")
def deposit():
    amount=float(input("Enter the amount to be deposited...  "))
    if amount < 0:
        print("You have to deposit atleast ₹1")
        return 0
    else:
        return amount
def withdraw(balance):
    amount=float(input("Enter the amount to be withdrawn...  "))
    if amount > balance:
        print("Insufficient balance!")
        return 0
    elif amount < 0:
        print("You have to withdraw atleast ₹1")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
       print("--------BANKING SIMULATOR--------")
       print("1.Balance")
       print("2.Deposit")
       print("3.Withdraw")
       print("4.Exit")
       choices=str(input("Enter your choice...      "))
       if choices == '1':
           show_balance(balance)
       elif choices == '2':
           balance += deposit()
       elif choices == '3':
           balance -= withdraw(balance)
       elif choices == '4':
           is_running = False
           print("Thank you for visiting our bank!")
       else:
           print("Invalid choice entered...")
if __name__ == '__main__':
    main()


