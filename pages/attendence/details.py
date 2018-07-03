from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Details(BasePage):
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
    _export = "[name='export']"  # By CSS
    _table = "tbody tr:nth-of-type(1) .text-left"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickDetails(self):
        self.elementClick(self._details, locatorType='link')

    def verifyLogs(self):
        result = self.isElementPresent(self._logs, locatorType='link')
        self.stat.mark(result, "Verify Logs")

    def verifyAbsentees(self):
        result1 = self.isElementPresent(self._absentees, locatorType='link')
        self.stat.mark(result1, "Verify Absentees")

    def verifySearchBar(self):
        result2 = self.isElementPresent(self._search_bar, locatorType='css')
        self.stat.mark(result2, "Verify Search Bar")

    def verifyMoreOptions(self):
        result3 = self.isElementPresent(self._more_options, locatorType='css')
        self.stat.mark(result3, "Verify More Options")

    def verifyAddNew(self):
        result4 = self.isElementPresent(self._add_new, locatorType='css')
        self.stat.mark(result4, "Verify Add New")

    def verifyExport(self):
        result5 = self.isElementPresent(self._export, locatorType='css')
        self.stat.mark(result5, "Verify Export")

    def verifyTable(self):
        result6 = self.isElementPresent(self._table, locatorType='css')
        self.stat.markFinal("Test_Details", result6, "Verify Table")

    def Details(self):
        self.clickDetails()
        self.verifyLogs()
        self.verifyAbsentees()
        self.verifySearchBar()
        self.verifyMoreOptions()
        self.verifyExport()
        self.verifyAddNew()
        self.verifyTable()
