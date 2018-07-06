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
        return result

    def verifyDetails(self):
        result = self.isElementPresent(self._details, locatorType='link')
        return result

    def verifyMoreOptions(self):
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def verifySearchBar(self):
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def verifyAddBtn(self):
        result = self.isElementPresent(self._add_new, locatorType='css')
        return result

    def verifyTable(self):
        self.util.sleep(3)
        result = self.isElementPresent(self._table, locatorType='css')
        return result

    def absenteesSmoke(self):
        self.nav.Attendence()
        self.clickAbsentees()
        result = self.verifyLog()
        self.stat.mark(result, "Verify Logs")
        result1 = self.verifyDetails()
        self.stat.mark(result1, "Verify Details")
        result2 = self.verifyMoreOptions()
        self.stat.mark(result2, "Verify More Options")
        result3 = self.verifySearchBar()
        self.stat.mark(result3, "Verify Search Bar")
        result4 = self.verifyAddBtn()
        self.stat.mark(result4, "Verify Add Button")
        self.waitForElement(self._table, locatorType='css')
        result5 = self.verifyTable()
        self.stat.markFinal("Test_Absentees", result5, "Verify Table")

    def verifyTextLogs(self):
        text = self.getText(self._logs, locatorType='link')
        result = self.util.verifyTextContains(self._text_logs, text)
        return result

    def verifyTextDetails(self):
        text = self.getText(self._details, locatorType='link')
        result = self.util.verifyTextContains(self._text_details, text)
        return result

    def verifyTextAbsentees(self):
        text = self.getText(self._absentees, locatorType='link')
        result = self.util.verifyTextContains(self._text_absentees, text)
        return result

    def verifyTextDepartment(self):
        text = self.getText(self._department, locatorType='css')
        result = self.util.verifyTextContains(self._text_department, text)
        return result

    def verifyTextName(self):
        text = self.getText(self._name, locatorType='css')
        result = self.util.verifyTextContains(self._text_name, text)
        return result

    def verifyTextPhone1(self):
        text = self.getText(self._phone1, locatorType='css')
        result = self.util.verifyTextContains(self._text_phone1, text)
        return result

    def verifyTextPhone2(self):
        text = self.getText(self._phone2, locatorType='css')
        result = self.util.verifyTextContains(self._text_phone2, text)
        return result

    def AbsenteesText(self):
        result = self.verifyTextLogs()
        self.stat.mark(result, "Verify Text Logs")
        result1 = self.verifyTextDetails()
        self.stat.mark(result1, "Verify Text Details")
        result2 = self.verifyTextAbsentees()
        self.stat.mark(result2, "Verify Text Absentees")
        result3 = self.verifyTextDepartment()
        self.stat.mark(result3, "Verify Text Department")
        result4 = self.verifyTextName()
        self.stat.mark(result4, "Verify Text Name")
        result5 = self.verifyTextPhone1()
        self.stat.mark(result5, "Verify Text Phone 1")
        result6 = self.verifyTextPhone2()
        self.stat.markFinal("Test_Text Absentees", result6, "Verify Text Phone 2")