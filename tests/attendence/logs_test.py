import pytest
import unittest
from pages.attendence.logs import Logs
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestLogs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = Logs(self.driver)

    @pytest.mark.run(order=1)
    def test_Logs(self):
        self.lg.LogsSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/logsText.csv"))
    @unpack
    def test_LogsText(self, _text_name, _text_add_new, _text_date_time, _text_status, _text_absentees, _text_details, _text_logs):
        self.lg.LogsText(_text_name, _text_add_new, _text_date_time, _text_status, _text_absentees, _text_details, _text_logs)

