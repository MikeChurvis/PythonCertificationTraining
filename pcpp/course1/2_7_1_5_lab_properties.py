class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, _):
        raise AccountException("Account number cannot be changed.")

    @account_number.deleter
    def account_number(self):
        if self.__balance > 0:
            raise AccountException("Cannot delete a non-empty account.")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise AccountException("Account balance cannot be negative.")

        if abs(new_balance - self.__balance) > 100_000:
            print("Transaction value greater than 100,000 detected.")

        self.__balance = new_balance


if __name__ == '__main__':
    def main():
        print('create account')
        acc = BankAccount(1)

        print('set account balance to 1000')
        acc.balance = 1000

        try:
            print('set account balance to -200')
            acc.balance = -200
        except AccountException as e:
            print(e)

        try:
            print('change account number')
            acc.account_number = 2
        except AccountException as e:
            print(e)

        print('deposit 1 million into account')
        acc.balance += 1_000_000

        try:
            print('delete account')
            del acc.account_number
        except AccountException as e:
            print(e)


    main()
