import time
import pytest
import unittest
from utilities.teststatus import Status
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase, LoginPage):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

        """
        Need to verify two verification points
        1 fails, code will not go to the next verification point
        If assert fails, it stops current test execution and moves to the next test method.
        """

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login("", "")
        result = self.lp.verifyLoginFailed1()
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=2)
    def test_invalidLogin2(self):
        # self.util.sleep(2)
        self.lp.login("admin", "")
        result = self.lp.verifyLoginFailed1()
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=3)
    def test_invalidLogin3(self):
        # self.util.sleep(2)
        self.lp.login("", "admin123")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=4)
    def test_validLogin(self):
        self.lp.login("", "")
        result = self.lp.verifyLogin()
        self.ts.markFinal("test_validLogin", result, "Login was Successful")

    @pytest.mark.run(order=5)
    def test_validlogout(self):
        self.lp.logout()
        result = self.lp.verifyLogoutSuccess()
        self.ts.markFinal("test_validLogout", result, "Logout successful")
