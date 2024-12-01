import datetime as dt

from CSVManager import CSVManager


class Transactions(CSVManager):
    def __init__(self, path, transactions_list=None):
        super().__init__(path)
        if transactions_list is None:
            transactions_list = []
        self.transactions_list = transactions_list

    def read_file(self):
        data = self.read_data()
        headers = data[0]
        rows = data[1:]
        self.transactions_list = [dict(zip(headers, row)) for row in rows]

        return self.transactions_list

    def add_transaction(self, sender_account, receiver_account, summ):
        if summ > 0 and sender_account != receiver_account:
            transaction = {
                'Дата и время': dt.datetime.now().strftime('%Y-%m-%d %H:%M'),
                'Счет отправителя': sender_account,
                'Счет получателя': receiver_account,
                'Сумма': f"{summ}"
            }

            self.transactions_list.append(transaction)

            self.add_row([transaction['Дата и время'], sender_account, receiver_account, summ])

            return transaction

    def count_transactions(self, account, transaction_type):
        total_sum = 0
        for transaction in self.transactions_list:
            if transaction_type.lower() == 'исходящая' and transaction['Счет отправителя'] == account:
                total_sum += float(transaction['Сумма'])

            elif transaction_type.lower() == 'входящая' and transaction['Счет получателя'] == account:
                total_sum += float(transaction['Сумма'])
        return total_sum

    def date_sorting(self, start_date, end_date=None):
        filtered_transactions = []
        if not end_date:
            end_date = start_date
            end_date = dt.datetime.strptime(end_date, '%Y-%m-%d') + dt.timedelta(days=1)
            start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
        elif end_date:
            start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

        for transaction in self.transactions_list:

            transaction_date = dt.datetime.strptime(transaction['Дата и время'], '%Y-%m-%d %H:%M')

            if start_date <= transaction_date <= end_date:
                filtered_transactions.append(transaction)

        return filtered_transactions
