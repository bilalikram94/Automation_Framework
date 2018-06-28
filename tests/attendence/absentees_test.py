import pytest
import unittest
from pages.home.navigation import Navigation
from pages.attendence.absentees import Absentees


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nav = Navigation(self.driver)
        self.abs = Absentees(self.driver)

    @pytest.mark.run(order=1)
    def test_Absentees(self):
        self.nav.Attendence()
        self.abs.absentees()
