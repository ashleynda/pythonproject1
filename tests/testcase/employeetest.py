import unittest
from tests.employee import Employee


class TestDiaryFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.employee = Employee(1, "Ashley", "Department")

    def test_that_calculates_salary(self):
        self.employee.calculate_salary(20)
        self.assertEqual(200, self.employee.get_number_of_salary())

    def test_that_can_assign_department(self):
        self.employee.assign_department("Engineering")
        self.assertEqual("Engineering", self.employee.assign_department("Engineering"))

    def test_that_can_print_employee_details(self):
        self.assertEqual("1 Ashley Department", self.employee.employee_details())