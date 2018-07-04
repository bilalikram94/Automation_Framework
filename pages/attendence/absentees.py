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
    _department = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(1)"  # By CSS
    _name = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(2)"  # By CSS
    _phone1 = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(3)"  # By CSS
    _phone2 = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(4)"  # By CSS
    _text_absentees = "absentees"  # Text
    _text_details = "details"  # Text
    _text_logs = "logs"  # Text
    _text_department = "department"  # Text
    _text_name = "name"  # Text
    _text_phone1 = "phone 1"  # Text
    _text_phone2 = "phone 2"  # Text

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
        self.nav.Attendence()
        self.clickAbsentees()
        self.verifyLog()
        self.verifyDetails()
        self.verifyMoreOptions()
        self.verifySearchBar()
        self.verifyAddBtn()
        self.waitForElement(self._table, locatorType='css')
        self.verifyTable()

    def verifyTextLogs(self):
        text = self.getText(self._logs, locatorType='link')
        result = self.util.verifyTextContains(self._text_logs, text)
        self.stat.mark(result, "Verify Text Logs")

    def verifyTextDetails(self):
        text = self.getText(self._details, locatorType='link')
        result1 = self.util.verifyTextContains(self._text_details, text)
        self.stat.mark(result1, "Verify Text Details")

    def verifyTextAbsentees(self):
        text = self.getText(self._absentees, locatorType='link')
        result = self.util.verifyTextContains(self._text_absentees, text)
        self.stat.mark(result, "Verify Text Absentees")

    def verifyTextDepartment(self):
        text = self.getText(self._department, locatorType='css')
        result2 = self.util.verifyTextContains(self._text_department, text)
        self.stat.mark(result2, "Verify Text Department")

    def verifyTextName(self):
        text = self.getText(self._name, locatorType='css')
        result3 = self.util.verifyTextContains(self._text_name, text)
        self.stat.mark(result3, "Verify Text Name")

    def verifyTextPhone1(self):
        text = self.getText(self._phone1, locatorType='css')
        result4 = self.util.verifyTextContains(self._text_phone1, text)
        self.stat.mark(result4, "Verify Text Phone 1")

    def verifyTextPhone2(self):
        text = self.getText(self._phone2, locatorType='css')
        result5 = self.util.verifyTextContains(self._text_phone2, text)
        self.stat.markFinal("Test_Text Absentees", result5, "Verify Text Phone 2")

    def AbsenteesText(self):
        self.verifyTextLogs()
        self.verifyTextDetails()
        self.verifyTextAbsentees()
        self.verifyTextDepartment()
        self.verifyTextName()
        self.verifyTextPhone1()
        self.verifyTextPhone2()