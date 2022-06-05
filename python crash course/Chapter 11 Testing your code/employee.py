class Employee():
    """Class employee"""

    def __init__(self, first, last, anual_salary):
        self.first = first
        self.last = last
        self.anual_salary = anual_salary

    def employee_info(self):
        print(f"{self.first.title()} {self.last.title()} {self.anual_salary}")

    def give_raise(self, anual_salary='50000'):
        self.anual_salary += int(anual_salary)
