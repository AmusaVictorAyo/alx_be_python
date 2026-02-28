class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self.account_balance:.2f}")