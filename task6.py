from datetime import datetime

class Account:
    def __init__(self, name: str, initial_balance: float = 0.0):
        self.name = name
        self.balance = initial_balance
        self.operations = []
        
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.operations.append({
                'type': 'Deposit',
                'amount': amount,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print(f"Пополнено на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")
    
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return
        
        if amount <= self.balance:
            self.balance -= amount
            self.operations.append({
                'type': 'Withdrawal',
                'amount': amount,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print(f"Снято {amount}. Текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств на счете.")
    
    def get_operations_history(self):
        if not self.operations:
            print("История транзакций пуста.")
        else:
            print("История транзакций:")
            for operation in self.operations:
                print(f"{operation['date']} | {operation['type']} | {operation['amount']}")


account = Account("Ivan Doronin", 1000.0)

account.deposit(500.0)
account.withdraw(200.0)
account.deposit(300.0)
account.get_operations_history()
