from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class SideMenu(BasePage):
    log = cl.customLogger(logging.DEBUG)
    #  Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
    _employee = 'Employees'  # By Link
    _support_ticket = 'Support Tickets'  # By Link
    _time_off = 'Time Off'  # By Link
    _training = 'Training'  # By Link
    _logs = "Logs"  # By Link
    _detail = "Detail"  # By Link
    _absentee = "Absentees"  # By Link
    _more_options = ".advance-btn"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS

    all_results = {}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickSideMenu(self):
        self.elementClick(self._side_menu, locatorType='xpath')
        self.util.sleep(3)

    def verifySideMenu(self):
        result = self.isElementPresent(self._attendence, locatorType='link')
        return result

    def verifySideMenu1(self):
        result = self.isElementPresent(self._employee, locatorType='link')
        return result

    def verifySideMenu2(self):
        result = self.isElementPresent(self._support_ticket, locatorType='link')
        return result

    def verifySideMenu3(self):
        result = self.isElementPresent(self._training, locatorType='link')
        return result

    def verifySideMenu4(self):
        result = self.isElementPresent(self._time_off, locatorType='link')
        return result



