from CSVManager import CSVManager

class Users(CSVManager):
    def __init__(self, path):
        super().__init__(path)
        self.users = self.read_users()

    def read_users(self):
        data = self.read_data()
        if data:
            header = data[0]
            users_data = []
            for i in data[1:]:
                user_dict = dict(zip(header, i))
                users_data.append(user_dict)
            return users_data
        else:
            return []

    def save_users(self):
        if self.users:
            header = list(self.users[0].keys())
            data_to_save = [header]
            for user in self.users:
                data_to_save.append(list(user.values()))
            self.overwrite_file(data_to_save)

    def find_user(self, search_term, search_field="Имя"):
        found = []
        for user in self.users:
            if user.get(search_field) == search_term:
                found.append(user)
        return found

    def filter_by_age(self, min_age):
        filtered = []
        for user in self.users:
            age = int(user['Возраст'])
            if age >= min_age:
                filtered.append(user)
        return filtered

    def add_user(self, name, surname, email, age):
        new_user = {'Имя': name, 'Фамилия': surname, 'Электронная почта': email, 'Возраст': str(age)}
        self.users.append(new_user)
        self.save_users()