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
        self.dt.Details()

