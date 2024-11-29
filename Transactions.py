import csv
from datetime import datetime
from itertools import count

from CSVManager import CSVManager


class Transactions(CSVManager):
    def __init__(self, path, transactions_dict=None):
        super().__init__(path)
        if transactions_dict is None:
            transactions_dict = []
        self.transactions_dict = transactions_dict

    def read_file(self):
        data = self.read_data()
        headers = data[0]
        rows = data[1:]
        self.transactions_dict = [dict(zip(headers, row)) for row in rows]

        return self.transactions_dict

    def add_transaction(self, sender_account, receiver_account, summ):
        if summ > 0 and sender_account != receiver_account:
            transaction = {
                'Дата и время': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'Счет отправителя': sender_account,
                'Счет получателя': receiver_account,
                'Сумма': f"{summ}"
            }

            self.transactions_dict.append(transaction)

            self.add_row([transaction['Дата и время'], sender_account, receiver_account, summ])

            return transaction

    def count_transactions(self, account):
        counter = 0
        for transaction in self.transactions_dict:
            if transaction['Счет отправителя'] == account:
                counter -= float(transaction['Сумма'])
            elif transaction['Счет получателя'] == account:
                counter += float(transaction['Сумма'])
        return f'Денег на счете клиента {account}: \n {counter}'

    def date_sorting(self, start_date, end_date):
        filtered_transactions = []

        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

        for transaction in self.transactions_dict:

            transaction_date = datetime.strptime(transaction['Дата и время'], '%Y-%m-%d %H:%M')

            if transaction_date >= start_date and transaction_date <= end_date:
                filtered_transactions.append(transaction)

        return filtered_transactions
