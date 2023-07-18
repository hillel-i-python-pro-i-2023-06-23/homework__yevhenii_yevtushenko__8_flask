from typing import NamedTuple, Iterator

from faker import Faker


class User(NamedTuple):
    name: str
    email: str

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_raw_dict(cls, raw_data: dict) -> "User":
        return cls(
            name=raw_data["name"],
            email=raw_data["email"],
        )


def generate_user() -> NamedTuple:
    faker = Faker()
    return User(
        name=faker.first_name(),
        email=faker.email()
    )


def generate_users(count: int) -> Iterator[User]:
    for _ in range(count):
        yield generate_user()
