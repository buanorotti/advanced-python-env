class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age

    def introduce(self) -> str:
        return f"Hello, my name is {self.name}. I am {self._age} years old."

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 1:
            raise ValueError("Age must be greater than zero.")
        self._age = age


class Student(Person):
    def __init__(self, name: str, age: int, major: str) -> None:
        super().__init__(name, age)
        self.major = major

    def introduce(self) -> str:
        base_info = super().introduce()
        return f"{base_info} My major is {self.major}."


def main() -> None:
    person = Person("Alex", 30)
    student = Student("Dana", 18, "Computer Science")

    people: list[Person] = [person, student]
    for p in people:
        print(p.introduce())

    student.set_age(19)
    print(f"Updated student age: {student.get_age()}")


if __name__ == "__main__":
    main()
