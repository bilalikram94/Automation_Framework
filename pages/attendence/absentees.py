from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Absentees(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
    _logs = "Logs"  # By Link
    _details = "Detail"  # By Link
    _absentees = "Absentees"  # By Link
    _more_options = "[data-toggle='collapse']"  # By CSS
    _search_bar = "#basic_search [type]"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS
    _table = "tbody [role='row']:nth-of-type(1) .sorting_1"  # By CSS
    results = []

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickAbsentees(self):
        self.elementClick(self._absentees, locatorType='link')

    def verifyLog(self):
        result = self.isElementPresent(self._logs, locatorType='link')
        self.stat.mark(result, "Verify Logs")
        # self.results.append(result)

    def verifyDetails(self):
        result1 = self.isElementPresent(self._details, locatorType='link')
        self.stat.mark(result1, "Verify Details")
        # self.results.append(result)

    def verifyMoreOptions(self):
        result2 = self.isElementPresent(self._more_options, locatorType='css')
        self.stat.mark(result2, "Verify More Options")

    def verifySearchBar(self):
        result3 = self.isElementPresent(self._search_bar, locatorType='css')
        self.stat.mark(result3, "Verify Search Bar")

    def verifyAddBtn(self):
        result4 = self.isElementPresent(self._add_new, locatorType='css')
        self.stat.mark(result4, "Verify Add Button")

    def verifyTable(self):
        self.util.sleep(3)
        result6 = self.isElementPresent(self._table, locatorType='css')
        self.stat.markFinal("Test_Absentees", result6, "Verify Table")

    def absenteesSmoke(self):
        self.clickAbsentees()
        self.verifyLog()
        self.verifyDetails()
        self.verifyMoreOptions()
        self.verifySearchBar()
        self.verifyAddBtn()
        self.waitForElement(self._table, locatorType='css')
        self.verifyTable()


