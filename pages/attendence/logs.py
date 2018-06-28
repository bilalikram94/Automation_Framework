from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.teststatus import Status
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
        self.ts = Status(self.driver)

    def verifyLogs(self):
        result = self.isElementPresent(self._logs, locatorType='link')
        self.ts.mark(result, "Verify Logs")

    def verifyDetails(self):
        result1 = self.isElementPresent(self._details, locatorType='link')
        self.ts.mark(result1, "Verify Details")

    def verifyAbsentees(self):
        result2 = self.isElementPresent(self._absentees, locatorType='link')
        self.ts.mark(result2, "VerifyAbsentees")

    def verifyMoreOptions(self):
        result3 = self.isElementPresent(self._more_options, locatorType='css')
        self.ts.mark(result3, "Verify More Options")

    def verifyAddBtn(self):
        result4 = self.isElementPresent(self._add_new, locatorType='css')
        self.ts.mark(result4, "Verify Add Button")

    def verifySearchBar(self):
        result5 = self.isElementPresent(self._search_bar, locatorType='css')
        self.ts.mark(result5, "Verify Search Bar")

    def verifyTable(self):
        time.sleep(3)
        result6 = self.isElementPresent(self._table_elements, locatorType='css')
        self.ts.markFinal("Test_Logs", result6, "Verify Table")

    def Logs(self):
        self.verifyLogs()
        self.verifyAbsentees()
        self.verifyDetails()
        self.verifyAbsentees()
        self.verifyMoreOptions()
        self.verifyAddBtn()
        self.verifySearchBar()
        self.verifyTable()