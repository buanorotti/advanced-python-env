class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self._salary = salary

    def get_salary(self) -> float:
        return self._salary

    def get_role(self) -> str:
        return "Employee"


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus_rate: float = 0.1) -> None:
        super().__init__(name, salary)
        self.bonus_rate = bonus_rate

    def get_role(self) -> str:
        return "Manager"

    def calculate_bonus(self) -> float:
        return self._salary * self.bonus_rate


def print_employee_info(staff: list[Employee]) -> None:
    for emp in staff:
        print(f"{emp.name} | Role: {emp.get_role()} | Salary: {emp.get_salary()}")


def main() -> None:
    employee = Employee("Aruzhan", 250000)
    manager = Manager("Timur", 400000, bonus_rate=0.2)

    print_employee_info([employee, manager])
    print("Manager bonus:", manager.calculate_bonus())


if __name__ == "__main__":
    main()
