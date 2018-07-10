import pytest
import unittest
from pages.sidemenu.side_menu import SideMenu
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
"""
when using pytest the test cases must start with test_("testname") and the test must start with small 't' otherwise 
the test will not be collected 
"""


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestSideMenu(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sm = SideMenu(self.driver)

    @pytest.mark.run(order=1)
    def test_SideMenu(self):
        self.sm.SideMenuSmoke()

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/sidemenuText.csv"))
    @unpack
    def test_SideMenu1(self, _text_attendance, _text_employee, _text_support_ticket, _text_training, _text_time_off):
        self.sm.SideMenuText(_text_attendance, _text_employee, _text_support_ticket, _text_training, _text_time_off)