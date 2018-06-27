from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class Logs(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
    _logs = "Logs"  # By Link
    _details = "Detail"  # By Link
    _absentees = "Absentees"  # By Link
    _more_options = "[data-toggle='collapse']"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS
    _search_bar = "#basic_search [type]"  # By CSS
    _table_elements = "tbody [role='row']:nth-of-type(1) .sorting_1"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyLogs(self):
        result = self.isElementPresent(self._logs, locatorType='link')
        return result

    def verifyDetails(self):
        result = self.isElementPresent(self._details, locatorType='link')
        return result

    def verifyAbsentees(self):
        result = self.isElementPresent(self._absentees, locatorType='link')
        return result

    def verifyMoreOptions(self):
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def verifyAddBtn(self):
        result = self.isElementPresent(self._add_new, locatorType='css')
        return result

    def verifySearchBar(self):
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def verifyTable(self):
        time.sleep(3)
        result = self.isElementPresent(self._table_elements, locatorType='css')
        return result
