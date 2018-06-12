from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _login_success = "//*[@id='navbar']//span[text()='User Settings']"
    _failed_login = ".alert-danger"
    _user_settings = "User Settings"
    _logout = "Log Out"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self, _login_success):

        result = self.isElementPresent(_login_success, locatorType="xpath")
        return result

    # def clearFields(self):
    #     emailField = self.getElement(locator=self._email_field)
    #     emailField.clear()
    #     passwordField = self.getElement(locator=self._password_field)
    #     passwordField.clear()

    def verifyLoginFailed(self, _failed_login):
        result = self.isElementPresent(_failed_login, "css")
        return result

    def verifyTitle(self):

        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False

    def clickUserSettings(self, _user_settings):
        result = self.elementClick(_user_settings, "link")

    def clickLogOut(self, _logout):
        result = self.elementClick(_logout, "link")
        return result

    def verifySuccessfulLogout(self):
        self.clickUserSettings()
        self.clickLogOut()
