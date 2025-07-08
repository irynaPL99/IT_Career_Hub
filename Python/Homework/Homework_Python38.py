'''Task 1. Банковский счёт
Создайте класс BankAccount, описывающий банковский счёт.
Объект должен хранить имя владельца и текущий баланс.
Реализуйте методы:
-пополнение счёта
-снятие средств
-отображение баланса
При попытке снять больше, чем есть на счёте,
операция не должна выполняться.
Продумайте, какие поля и методы следует скрыть от внешнего доступа,
а какие оставить открытыми.
'''

'''Task 2. История операций
Доработайте класс BankAccount.
Каждая операция пополнения и снятия должна сохраняться в историю.
История должна быть доступна через property history только для чтения.
История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).
'''
print("\n Task 1. Банковский счёт")
class BankAccount:
    def __init__(self, name_owner : str, current_balance: float):
        self.name_owner = name_owner
        self._current_balance = current_balance # чтобы нельзя было напрямую менять извне.
        self._history = []  # скрытое поле для истории операций (чтобы нельзя было перезаписать.)

     # Строковое представление: (username: Alice, password: 1234, num: 1)
    #def __str__(self):
    #    return f"account info: {self.name_owner}, Current balance: {self._current_balance}, history: {self._history}"

    def show_balance(self):
        print(f"Current balance: {self._current_balance:.2f}")

    def _valide_amount(self, amount: float) -> bool:
        """Check if amount is a valid positive number """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return True

    def add_deposit(self, amount: float):
        self._valide_amount(amount)
        self._current_balance += amount
        self._history.append(f"Deposit: {amount:.2f}")

    def withdraw_deposit(self, amount):
        self._valide_amount(amount)
        if amount > self._current_balance:
            raise ValueError("Not enough funds.")
        self._current_balance -= amount
        self._history.append(f"Withdraw: {amount:.2f}")


    # История должна быть доступна через property history только для чтения.
    @property
    def history_print(self):
        return self._history.copy()

# main code
account = BankAccount("Alica", 150)
account.show_balance()

# Deposit
try:
    account.add_deposit(-1.0) # "Error: Amount must be positive."
except Exception as e:
    print("Error:", e)
account.show_balance()

try:
    account.add_deposit(1.0)
except Exception as e:
    print("Error:", e)
account.show_balance()


# withdraw_deposit
try:
    account.withdraw_deposit(200.0) # "Error: Not enough funds."
except Exception as e:
    print("Error:", e)
account.show_balance()

try:
    account.withdraw_deposit(100.0)
except Exception as e:
    print("Error:", e)

account.show_balance()

#print(account)
print("\nOperation history:")
for operation in account.history_print:
    print("\t" + operation)
