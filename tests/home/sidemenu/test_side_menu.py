import pytest
import unittest
from utilities.teststatus import Status
from pages.sidemenu.side_menu import SideMenu


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSideMenu(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sm = SideMenu(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def Test_SideMenu(self):
        self.sm.clickSideMenu()
        result = self.sm.verifySideMenu()
        self.ts.mark(result, "Verify Attendence")
        result1 = self.sm.verifySideMenu1()
        self.ts.mark(result1, "Verify Employee")
        result2 = self.sm.verifySideMenu2()
        self.ts.mark(result2, "Verify Support Ticket")
        result3 = self.sm.verifySideMenu3()
        self.ts.mark(result3, "Verify Training")
        result4 = self.sm.verifySideMenu4()
        self.ts.markFinal("Test_SideMenu", result4, "Verify Time-Off")
