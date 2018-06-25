import pytest
import unittest
from utilities.teststatus import Status
from pages.home.login_page import LoginPage
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
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
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/logincredentials.csv"))
    @unpack
    def test_invalidLogin(self, email, password):
        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed1()
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/validlogin.csv"))
    @unpack
    def test_validLogin(self, email, password):
        self.lp.login(email, password)
        result = self.lp.verifyLogin()
        self.ts.markFinal("test_validLogin", result, "Login was Successful")

    @pytest.mark.run(order=3)
    def test_validlogout(self):
        self.lp.logout()
        result = self.lp.verifyLogoutSuccess()
        self.ts.markFinal("test_validLogout", result, "Logout successful")
