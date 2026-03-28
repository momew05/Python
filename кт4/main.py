class User:
    def __init__(self, name, login, password):
        super().__setattr__("name", name)
        super().__setattr__("_login", login)
        super().__setattr__("_password", password)
        super().__setattr__("_access", 1)

    def __setattr__(self, name, value):
        try: self.__setattr__(name, value)
        except: print(f"Неизвестное свойство {name}")
    
    def __getattr__(self, name): 
        try: self.__getattr__(name)
        except: print(f"Неизвестное свойство {name}")

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        print("Unable to change login")

    @property
    def password(self):
        return "*" * len(self._password)
    
    @password.setter
    def password(self, value):
        if (input("Input your old password:\n") == self._password):
            self._password = value
            print("Your password was changed")
        else:
            print("Wrong password. Try again later")
        
    @property
    def access(self):
        return self._access
    
    @access.setter
    def access(self):
        print("Access denied")

    def __gt__(self, other):
        return self.access > other.access
    def __lt__(self, other):
        return self.access < other.access
    def __eq__(self, other):
        return self.access == other.access

    def show_info(self):
        print(f'Name: {self.name}, Login: {self.login}')


class SuperUser(User):
    def __init__(self, name, login, password, access, status):
        super().__init__(name, login, password)
        object.__setattr__(self, "_access", access)
        object.__setattr__(self, "_status", status)

    @property
    def status(self):
        print("Access denied")

    @status.setter
    def status(self, value):
        self._status = value
    
    def show_info(self):
        print(f'Name: {self.name}, Login: {self._login}, Status: {self._status}')

    def change_access(self, user):
        a = input("Input your status\n")
        if a == self._status:
            user._access = int(input(f"Input access level for {user.login}\n"))
            print("Access was changed")
        else:
            print("Access denied")


user1 = User("Petya", "ZOLOFT", "00000")
user2 = User("Sasha", "WANNACRY", "66666")
user3 = User("Misha", "qwerty", "12332")
admin = SuperUser("Momo", "momewo", "12345", 2, "admin")
god = SuperUser("Sunny", "root", "10101", 3, "godmod")

user2.show_info()
god.show_info()
admin.login = "nogod"
print(user3.password)
print(user1 > god)
print(god == admin)
print(god > admin)
user1.grade = 10
print(admin.grade)
admin.change_access(user2)