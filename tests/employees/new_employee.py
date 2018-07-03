import pytest
import unittest
from pages.employees.new_employee import NewEmployee


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestNewEmployee(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nemp = NewEmployee(self.driver)

    @pytest.mark.run(order=1)
    def test_NewEmployee(self):
        self.nemp.NewEmployeeSmoke()
