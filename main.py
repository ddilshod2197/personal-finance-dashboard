class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        else:
            self.attempts += 1
            if self.attempts == 3:
                print("Account blocked!")
                return False
            else:
                print("Incorrect PIN. Try again.")
                return False

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


atm = ATM(1234)
while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
    pin = input("Enter your PIN: ")
    if atm.check_pin(int(pin)):
        continue
```

Kodda biz ATM klassini yaratdik, unda hisob balansi, PIN kodi, urinishlar soni saqlanadi. `check_pin` metodida biz PINni tekshiramiz, agar xato bo'lsa urinishlar sonini oshiramiz va agar 3 marta xato kiritilsa hisob bloklanadi. `deposit`, `withdraw` va `check_balance` metodlarida biz hisobni o'zgartiramiz. Menyu bilan ishlash uchun while tsikl qo'ydim.
