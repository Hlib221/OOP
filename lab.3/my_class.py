class MyName:
    total_names = 0  # Class Variable

    def __init__(self, name=None):
        if name is None:
            self.name = self.anonymous_user().name
        else:
            self.name = name.capitalize()
        if not self.name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self):
        return f"My name is {self.name}"

    @property
    def my_email(self):
        return self.create_email()

    def create_email(self):
        return f"{self.name.lower()}@itcollege.lviv.ua"

    def change_email_domain(self, new_domain):
        if '@' in new_domain or not new_domain.isalpha():
            raise ValueError("Некоректний домен")
        self._email_domain = new_domain

    @property
    def full_name(self):
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def save_to_file(self, filename="users.txt"):
        with open(filename, "a") as f:
            f.write(self.full_name + "\n")

    def count_name_letters(self):
        return len(self.name)

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        return f"You say: {message}"