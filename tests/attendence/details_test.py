import pytest
import unittest
from utilities.teststatus import Status
from pages.attendence.details import Details
from pages.home.navigation import Navigation


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nav = Navigation(self.driver)
        self.ts = Status(self.driver)
        self.dt = Details(self.driver)

    @pytest.mark.run(order=1)
    def test_Details(self):
        self.nav.Attendence()
        self.dt.clickDetails()
        result = self.dt.verifyAbsentees()
        self.ts.mark(result, "Verify Absentees")
        result1 = self.dt.verifyLogs()
        self.ts.mark(result1, "Verify Logs")
        result2 = self.dt.verifyTable()
        self.ts.mark(result2, "Verify Table")
        result3 = self.dt.verifySearchBar()
        self.ts.mark(result3, "Verify Search Bar")
        result4 = self.dt.verifyMoreOptions()
        self.ts.mark(result4, "Verify More Options")
        result5 = self.dt.verifyAddNew()
        self.ts.mark(result5, "Verify Add New")
        result6 = self.dt.verifyExport()
        self.ts.markFinal("Test_Details", result6, "Verify Export")

