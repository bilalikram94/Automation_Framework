import pytest
import unittest
from pages.employees.employees import Employees
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
from utilities.teststatus import Status


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestEmployees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.emp = Employees(self.driver)
        self.stat = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_Employees(self):
        self.emp.EmployeesSmoke()