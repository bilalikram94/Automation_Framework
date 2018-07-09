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

    def AbsenteesText(self, _text_absentees, _text_details, _text_logs, _text_department, _text_name, _text_phone1, _text_phone2):
        text = self.getText(self._absentees, locatorType='link')
        result = self.util.verifyTextContains(_text_absentees, text)
        self.stat.mark(result, "Verify Text Absentees")
        text1 = self.getText(self._details, locatorType='link')
        result1 = self.util.verifyTextContains(_text_details, text1)
        self.stat.mark(result1, "Verify Text Details")
        text2 = self.getText(self._logs, locatorType='link')
        result2 = self.util.verifyTextContains(_text_logs, text2)
        self.stat.mark(result2, "Verify Text Logs")
        text3 = self.getText(self._department, locatorType='css')
        result3 = self.util.verifyTextContains(_text_department, text3)
        self.stat.mark(result3, "Verify Text Department")
        text4 = self.getText(self._name, locatorType='css')
        result4 = self.util.verifyTextContains(_text_name, text4)
        self.stat.mark(result4, "Verify Text Name")
        text5 = self.getText(self._phone1, locatorType='css')
        result5 = self.util.verifyTextContains(_text_phone1, text5)
        self.stat.mark(result5, "Verify Text Phone 1")
        text6 = self.getText(self._phone2, locatorType='css')
        result6 = self.util.verifyTextContains(_text_phone2, text6)
        self.stat.markFinal("Test_Absentees Text", result6, "Verify Text Phone 2")