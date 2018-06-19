import time
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, LoginPage)
        self.ts = TestStatus(self.driver, TestStatus)
        """
        Need to verify two verification points
        1 fails, code will not go to the next verification point
        If assert fails, it stops current test execution and moves to the next test method.
        """

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_ValidLogin", result2, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        time.sleep(3)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login was successful")

    @pytest.mark.run(order=3)
    def test_validlogout(self):
        self.lp.Logout()
        result = self.lp.verifySuccessfulLogout()
        self.ts.markFinal("test_validLogout", result, "Logout was not successful")
