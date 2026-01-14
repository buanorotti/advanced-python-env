class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__owner = owner
        self.__balance = float(balance)

    def deposit(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += value

    def withdraw(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Amount must be positive.")
        if value > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= value

    def get_balance(self) -> float:
        return round(self.__balance, 2)

    def get_owner(self) -> str:
        return self.__owner


def main() -> None:
    account = BankAccount("Damir", 1000)

    print(f"Owner: {account.get_owner()}")
    print(f"Balance: {account.get_balance()}")

    account.deposit(500)
    print(f"After deposit: {account.get_balance()}")

    account.withdraw(300)
    print(f"After withdrawal: {account.get_balance()}")


if __name__ == "__main__":
    main()
