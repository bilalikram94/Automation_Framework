import pytest
import unittest
from pages.employees.employees import Employees


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Employees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.emp = Employees(self.driver)

    @pytest.mark.run(order=1)
    def test_Employees(self):
        self.emp.EmployeesSmoke()
