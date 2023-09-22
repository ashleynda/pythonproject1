class Employee:

    def __init__(self, id, name, department):
        self.hourly_rate = 10
        self.number_of_hours_worked = 0
        self.__id = id
        self.name = name
        self.department = department

    def calculate_salary(self, number_of_hours_worked):
        number_of_hours_worked *= self.hourly_rate
        self.number_of_hours_worked = number_of_hours_worked

    def get_number_of_salary(self):
        return self.number_of_hours_worked

    def assign_department(self, department):
        self.department = department
        return self.department

    def employee_details(self):
        return  f'{self.__id} {self.name} {self.department}'





