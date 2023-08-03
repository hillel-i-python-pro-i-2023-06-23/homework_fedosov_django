from typing import Type, NamedTuple, Iterator
from faker import Faker

class User(NamedTuple):
    user_login: str
    email: str
    password: str

    def __str__(self):
        return f"{self.user_login} - {self.email} - {self.password}"

def generate_user_data() -> User:
    fake = Faker()
    user_login = fake.user_name()
    email = user_login + str('@example.com')
    password = fake.password()
    return User(
        user_login,
        email,
        password,

    )

def check_unique_user(user, unique_users_list):
    return user not in unique_users_list


def generate_users_data(amount: int) -> Iterator[User]:
    unique_users = set()
    count_range = 0
    while count_range < amount:
        unique_users.add(generate_user_data().user_login)
        next_user = generate_user_data()
        if check_unique_user(next_user, unique_users):
            count_range += 1
            yield next_user



print(generate_users_data(10))