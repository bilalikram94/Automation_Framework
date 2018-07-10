import pytest
import unittest
from pages.training.employee_training import Training
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestEmployeeTraining(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.et = Training(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/employeeTrainingText.csv"))
    @unpack
    def test_EmployeeTraining(self, page_title,emp_train,train_eval,trainers,train_events,train_assess,add_train,train_type,table_title,train_frm,train_to,actions):
        self.et.EmployeeTrainingSmoke(page_title,emp_train,train_eval,trainers,train_events,train_assess,add_train,train_type,table_title,train_frm,train_to,actions)