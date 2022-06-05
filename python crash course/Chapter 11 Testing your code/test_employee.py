import unittest
from employee import Employee


class testEmployee(unittest.TestCase):
    """Test the Employee class"""

    def setUp(self):
        """parameters of the unittest"""
        self.other_employee = Employee('Fabian', 'Suchett', 50000)

    def test_give_default_raise(self):
        """Test the default value of give_rise method"""
        self.other_employee.give_raise()
        self.assertEqual(100000, self.other_employee.anual_salary)

    def test_gice_curstom_raise(self):
        """Test the custom value of give_rise method"""
        self.other_employee.give_raise(60000)
        self.assertEqual(110000, self.other_employee.anual_salary)


if __name__ == '__main__':
    unittest.main()
