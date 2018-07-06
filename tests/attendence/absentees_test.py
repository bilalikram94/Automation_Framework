import pytest
import unittest
from pages.attendence.absentees import Absentees


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestAbsentees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abs = Absentees(self.driver)

    @pytest.mark.run(order=1)
    def test_Absentees(self):
        self.abs.absenteesSmoke()

    @pytest.mark.run(order=2)
    def test_AbsenteesText(self):
        self.abs.AbsenteesText()
