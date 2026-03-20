class User:
    def __init__(self, name, login, password):
        self.name = name
        self._login = login
        self._password = password
        self._access = 1

    def show_info(self):
        print(f'Name: {self.name}, Login: {self.login}')

    def change_password(self):
        if (input("Input your old password:\n") == self.password):
            self.password = input("Input new password:\n")
        else:
            print("Wrong password. Try again later")

class SuperUser(User):
    def __init__(self, name, login, password, access, status):
        super().__init__(name, login, password, access)
        self._status = status

    def show_info(self):
        print(f'Name: {self.name}, Login: {self.login}, Status: {self.status}')

    
user1 = User("Petya", "ZOLOFT", "00000")
user2 = User("Sasha", "WANNACRY", "66666")
user3 = User("Misha", "qwerty", "12332")
admin = SuperUser("Momo", "momewo", "12345", 2, "admin")
god = SuperUser("Sunny", "root", "10101", 3, "godmod")


