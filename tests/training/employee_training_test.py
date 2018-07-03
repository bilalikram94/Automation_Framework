import pytest
import unittest
from pages.training.employee_training import Training


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestEmployeeTraining(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.et = Training(self.driver)

    @pytest.mark.run(order=1)
    def test_EmployeeTraining(self):
        self.et.EmployeeTrainingSmoke()