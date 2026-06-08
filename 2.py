import os
os.system("cls")


class Xodim:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0):
        self.name = name
        self.employee_id = employee_id
        self.__ish_hours = []
        self.hourly_rate = hourly_rate

    def log_hours(self, hour: int) -> bool:
        if 0 <= hour <= 24:
            self.__ish_hours.append(hour)
            return True
        return False

    def total_hours(self) -> int:
        return sum(self.__ish_hours)

    def calculate_salary(self) -> float:
        return self.total_hours() * self.hourly_rate

    def reset_hours(self):
        self.__ish_hours = []


# Test
xodim = Xodim("Javlon", "E101", hourly_rate=20.0)

print(xodim.log_hours(8))   # True
print(xodim.log_hours(9))   # True
print(xodim.log_hours(10))  # True
print(xodim.log_hours(25))  # False

print(xodim.total_hours())      # 27
print(xodim.calculate_salary()) # 540.0

xodim.reset_hours()
print(xodim.total_hours())      # 0
print(xodim.calculate_salary()) # 0.0