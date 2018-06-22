from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _login_link = "Login"  # By Link-Text
    _email_field = "el1"  # By ID
    _password_field = "el4"  # By ID
    _login_button = "//input[@type='submit']"  # By Xpath
    _login_success = ".logo-cubix"  # By CSS Selector
    _failed_login = ".alert-dismissible"  # By CSS Selector
    _user_image = ".user-image"  # By CSS Selector
    _logout_button = "Logout"  # By LinkText
    _logout_success_text = ".alert-dismissible" # By CSS Selector

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_button, locatorType='xpath')
        self.util.sleep(3)

    def verifyLogin(self):
        result = self.isElementPresent(self._login_success, locatorType='css')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._failed_login, locatorType='css')
        return result

    def verifyLoginFailed1(self):
        result = self.isElementPresent(self._email_field)
        return result

    def userImage(self):
        self.elementClick(self._user_image, locatorType='css')
        self.util.sleep(2)

    def logoutButton(self):
        self.elementClick(self._logout_button, locatorType='link')
        self.util.sleep(2)

    def verifyLogoutSuccess(self):
        time.sleep(2)
        getText = self.getText(self._login_button, locatorType='xpath')
        # getText1 = str(getText)
        result = self.util.verifyTextContains("Email", getText)
        return result

    def login(self, email='', password=''):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def logout(self):
        self.userImage()
        self.logoutButton()
        # self.verifyLogoutSuccess()
