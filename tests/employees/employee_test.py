import pytest
import unittest
from pages.employees.employees import Employees
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestEmployees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.emp = Employees(self.driver)

    @pytest.mark.run(order=1)
    def test_Employees(self):
        self.emp.EmployeesSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/employeepagetext.csv"))
    @unpack
    def test_TextEmployee(self, newemployeetext, nametext, designation, department, location, status):
        self.emp.verifyTextEmployee(newemployeetext, nametext, designation, department, location, status)