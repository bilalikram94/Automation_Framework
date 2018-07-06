import pytest
import unittest
from pages.attendence.details import Details


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.dt = Details(self.driver)

    @pytest.mark.run(order=1)
    def test_Details(self):
        self.dt.DetailsSmoke()

    @pytest.mark.run(order=2)
    def test_DetailsText(self):
        self.dt.DetailsVerifyText()