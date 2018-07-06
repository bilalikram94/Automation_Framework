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
    _day = "thead tr .text-center:nth-of-type(1)"  # By CSS
    _date = "thead tr .text-center:nth-of-type(2)"  # By CSS
    _time_in = "thead tr .text-center:nth-of-type(3)"  # By CSS
    _time_out = "thead tr .text-center:nth-of-type(4)"  # By CSS
    _time_spent = "thead tr .text-center:nth-of-type(5)"  # By CSS
    _break_time = "thead tr .text-center:nth-of-type(6)"  # By CSS
    _work_time = "thead tr .text-center:nth-of-type(7)"  # By CSS
    _text_day = "day"  # Text
    _text_date = "date"  # Text
    _text_time_in = "time in"  # Text
    _text_time_out = "time out"  # Text
    _text_time_spent = "time spent"  # Text
    _text_break_time = "break time"  # Text
    _text_work_time = "work time"  # Text
    _text_absentees = "absentees"  # Text
    _text_details = "details"  # Text
    _text_logs = "logs"  # Text
    _text_add_new = "add new"  # Text
    _text_export = "export"  # Text

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    def verifyTextAddNew(self):
        text = self.getText(self._add_new, locatorType='css')
        result = self.util.verifyTextContains(self._text_add_new, text)
        return result

    def verifyTextExport(self):
        text = self.getText(self._export, locatorType='css')
        result = self.util.verifyTextContains(self._text_export, text)
        return result

    def verifyTextDay(self):
        text = self.getText(self._day, locatorType='css')
        result = self.util.verifyTextContains(self._text_day, text)
        return result

    def verifyTextDate(self):
        text = self.getText(self._date, locatorType='css')
        result = self.util.verifyTextContains(self._text_date, text)
        return result

    def verifyTextTimeIn(self):
        text = self.getText(self._time_in, locatorType='css')
        result = self.util.verifyTextContains(self._text_time_in, text)
        return result

    def verifyTextTimeOut(self):
        text = self.getText(self._time_out, locatorType='css')
        result = self.util.verifyTextContains(self._text_time_out, text)
        return result

    def verifyTextTimeSpent(self):
        text = self.getText(self._time_spent, locatorType='css')
        result = self.util.verifyTextContains(self._text_time_spent, text)
        return result

    def verifyTextBreakTime(self):
        text = self.getText(self._break_time, locatorType='css')
        result = self.util.verifyTextContains(self._text_break_time, text)
        return result

    def verifyTextWorkTime(self):
        text = self.getText(self._work_time, locatorType='css')
        result = self.util.verifyTextContains(self._text_work_time, text)
        return result

    def clickDetails(self):
        self.elementClick(self._details, locatorType='link')

    def verifyLogs(self):
        result = self.isElementPresent(self._logs, locatorType='link')
        return result

    def verifyAbsentees(self):
        result = self.isElementPresent(self._absentees, locatorType='link')
        return result

    def verifySearchBar(self):
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def verifyMoreOptions(self):
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def verifyAddNew(self):
        result = self.isElementPresent(self._add_new, locatorType='css')
        return result

    def verifyExport(self):
        result = self.isElementPresent(self._export, locatorType='css')
        return result

    def verifyTable(self):
        result = self.isElementPresent(self._table, locatorType='css')
        return result

    def DetailsSmoke(self):
        self.nav.Attendence()
        self.clickDetails()
        result = self.verifyLogs()
        self.stat.mark(result, "Verify Details")
        result1 = self.verifyAbsentees()
        self.stat.mark(result1, "Verify Absentees")
        result2 = self.verifySearchBar()
        self.stat.mark(result2, "Verify Search Bar")
        result3 = self.verifyMoreOptions()
        self.stat.mark(result3, "Verify More Options")
        result4 = self.verifyExport()
        self.stat.mark(result4, "Verify Export")
        result5 = self.verifyAddNew()
        self.stat.mark(result5, "Verify Add New")
        result6 = self.verifyTable()
        self.stat.markFinal("Test_Details Smoke", result6, "Verify Table")

    def DetailsVerifyText(self):
        result = self.verifyTextLogs()
        self.stat.mark(result, "Verify Text Logs")
        result1 = self.verifyTextDetails()
        self.stat.mark(result1, "Verify Text Details")
        result2 = self.verifyTextAbsentees()
        self.stat.mark(result2, "Verify Text Absentees")
        result3 = self.verifyTextAddNew()
        self.stat.mark(result3, "Verify Text Add New")
        result4 = self.verifyTextExport()
        self.stat.mark(result4, "Verify Text Export")
        result5 = self.verifyTextDay()
        self.stat.mark(result5, "Verify Text Day")
        result6 = self.verifyTextDate()
        self.stat.mark(result6, "Verify Text Date")
        result7 = self.verifyTextTimeIn()
        self.stat.mark(result7, "Verify Text Time In")
        result9 = self.verifyTextTimeOut()
        self.stat.mark(result9, "Verify Text Time Out")
        result10 = self.verifyTextTimeSpent()
        self.stat.mark(result10, "Verify Text Time Spent")
        result11 = self.verifyTextBreakTime()
        self.stat.mark(result11, "Verify Text Break Time")
        result12 = self.verifyTextWorkTime()
        self.stat.markFinal("Test_Details Text Verify", result12, "Verify Text Work Time")