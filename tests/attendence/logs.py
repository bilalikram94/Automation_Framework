import pytest
import unittest
from utilities.teststatus import Status
from pages.attendence.logs import Logs
from pages.home.navigation import Navigation


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = Logs(self.driver)
        self.ts = Status(self.driver)
        self.nav = Navigation(self.driver)

    @pytest.mark.run(order=1)
    def test_Logs(self):
        self.nav.Attendence()
        result = self.lg.verifyAbsentees()
        self.ts.mark(result, "VerifyAbsentees")
        result1 = self.lg.verifyLogs()
        self.ts.mark(result1, "Verify Logs")
        result2 = self.lg.verifyDetails()
        self.ts.mark(result2, "Verify Details")
        result3 = self.lg.verifyMoreOptions()
        self.ts.mark(result3, "Verify More Options")
        result4 = self.lg.verifyAddBtn()
        self.ts.mark(result4, "Verify Add Button")
        result5 = self.lg.verifySearchBar()
        self.ts.mark(result5, "Verify Search Bar")
        result6 = self.lg.verifyTable()
        self.ts.markFinal("Test_Logs", result6, "Verify Table")
