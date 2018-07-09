import pytest
import unittest
from pages.attendence.details import Details
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.dt = Details(self.driver)

    @pytest.mark.run(order=1)
    def test_Details(self):
        self.dt.DetailsSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/detailsText.csv"))
    @unpack
    def test_DetailsText(self, _text_day, _text_date, _text_time_in, _text_time_out, _text_time_spent, _text_break_time, _text_work_time, _text_absentees, _text_details, _text_logs, _text_add_new, _text_export):
        self.dt.DetailsVerifyText(_text_day, _text_date, _text_time_in, _text_time_out, _text_time_spent, _text_break_time, _text_work_time, _text_absentees, _text_details, _text_logs, _text_add_new, _text_export)