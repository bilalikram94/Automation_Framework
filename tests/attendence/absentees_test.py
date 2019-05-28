import pytest
import unittest
from pages.attendence.absentees import Absentees
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestAbsentees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abs = Absentees(self.driver)

    @pytest.mark.run(order=1)
    def test_Absentees(self):
        self.abs.absenteesSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/absenteesText.csv"))
    @unpack
    def test_AbsenteesText(self, _text_absentees, _text_details, _text_logs, _text_department, _text_name, _text_phone1,
                           _text_phone2):
        self.abs.AbsenteesText(_text_absentees, _text_details, _text_logs, _text_department, _text_name, _text_phone1,
                               _text_phone2)
