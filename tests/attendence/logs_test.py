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
        self.lg.Logs()

