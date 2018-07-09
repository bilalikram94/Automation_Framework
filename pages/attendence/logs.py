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
    _drop_down = "[name='department']"  # By CSS
    _name = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(1)"  # By CSS
    _date_time = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(2)"  # By CSS
    _status = ".dataTables_scrollHeadInner [align='center']"  # By CSS

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

    def verifyDropDown(self):
        self.elementClick(self._more_options)
        result = self.isElementPresent(self._drop_down, locatorType='css')
        return result

    def LogsSmoke(self):
        self.nav.Attendence()
        self.waitForElement(self._table_elements, locatorType='css')
        result = self.verifyLogs()
        self.stat.mark(result, "Verify Logs")
        result1 = self.verifyAbsentees()
        self.stat.mark(result1, "VerifyAbsentees")
        result2 = self.verifyDetails()
        self.stat.mark(result2, "Verify Details")
        result3 = self.verifyMoreOptions()
        self.stat.mark(result3, "Verify More Options")
        result4 = self.verifyAddBtn()
        self.stat.mark(result4, "Verify Add Button")
        result5 = self.verifySearchBar()
        self.stat.mark(result5, "Verify Search Bar")
        result6 = self.verifyTable()
        self.stat.mark(result6, "Verify Table")
        result7 = self.verifyDropDown()
        self.stat.markFinal("Test_Logs", result7, "Verify Drop Down")

    def LogsText(self, _text_name, _text_add_new, _text_date_time, _text_status, _text_absentees, _text_details, _text_logs):
        text = self.getText(self._name, locatorType='css')
        result = self.util.verifyTextContains(_text_name, text)
        self.stat.mark(result, "Verify Text Name")
        text1 = self.getText(self._add_new, locatorType='css')
        result1 = self.util.verifyTextContains(_text_add_new, text1)
        self.stat.mark(result1, "Verify Text Add New")
        text2 = self.getText(self._date_time, locatorType='css')
        result2 = self.util.verifyTextContains(_text_date_time, text2)
        self.stat.mark(result2, "Verify Text Date Time")
        text3 = self.getText(self._status, locatorType='css')
        result3 = self.util.verifyTextContains(_text_status, text3)
        self.stat.mark(result3, "verify Text Status")
        text4 = self.getText(self._absentees, locatorType='link')
        result4 = self.util.verifyTextContains(_text_absentees, text4)
        self.stat.mark(result4, "Verify Text Absentees")
        text5 = self.getText(self._details, locatorType='link')
        result5 = self.util.verifyTextContains(_text_details, text5)
        self.stat.mark(result5, "Verify Text Details")
        text6 = self.getText(self._logs, locatorType='link')
        result6 = self.util.verifyTextContains(_text_logs, text6)
        self.stat.markFinal("Test_Log Text", result6, "Verify Text Logs")
