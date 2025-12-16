class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hello how would u like to proceed?
1. Create Pin
2. Deposit
3. Check Balance
4. Withdraw
5. Exit
""")

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter Your Pin:  ")
        print("Pin Created Successfully")

    def deposit(self):
        temp = input("Enter Your Pin:  ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Operation successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your Pin:  ")
        if temp == self.pin:
            print("Balance:", self.balance)
        else:
            print("Invalid Pin")
