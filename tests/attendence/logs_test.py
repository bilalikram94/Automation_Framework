import pytest
import unittest
from utilities.teststatus import Status
from pages.attendence.logs import Logs


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = Logs(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_Logs(self):
        self.lg.LogsSmoke()

    @pytest.mark.run(order=2)
    def test_LogsText(self):
        self.lg.LogsText()
