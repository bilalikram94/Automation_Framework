import pytest
import unittest
from pages.sidemenu.side_menu import SideMenu
"""
when using pytest the test cases must start with test_("testname") and the test must start with small 't' otherwise 
the test will not be collected 
"""


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSideMenu(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sm = SideMenu(self.driver)

    @pytest.mark.run(order=1)
    def test_SideMenu(self):
        self.sm.SideMenuSmoke()

    @pytest.mark.run(order=2)
    def test_SideMenuText(self):
        self.sm.SideMenuText()
