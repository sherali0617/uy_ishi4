import os
os.system("cls")

class Student:
    def __init__(self, name: str, talaba_id: str):
        self.name = name
        self.talaba_id = talaba_id
        self.__baholar = []
        print(f"Yangi talaba yaratildi: {self.name}, ID: {self.talaba_id}")

    def add_grade(self, baho: int):
        if 0 <= baho <= 100:
            self.__baholar.append(baho)
            print(f"{baho} bahosi qo'shildi")
        else:
            print("Xato: Noto'g'ri baho")

    def calculate_average(self) -> float:
        if not self.__baholar:
            return 0.0
        return sum(self.__baholar) / len(self.__baholar)

    def get_status(self) -> str:
        avg = self.calculate_average()
        if avg >= 90:
            return "A'lo"
        elif avg >= 80:
            return "Yaxshi"
        elif avg >= 70:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"



student = Student("Nodira", "S123")
student.add_grade(85)
student.add_grade(90)

print(student.calculate_average())
print(student.get_status())

student.add_grade(150)






