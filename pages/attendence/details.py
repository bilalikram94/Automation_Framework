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

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        self.nav.Details()
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

    def DetailsVerifyText(self, _text_day, _text_date, _text_time_in, _text_time_out, _text_time_spent, _text_break_time, _text_work_time, _text_absentees, _text_details, _text_logs, _text_add_new, _text_export):
        text = self.getText(self._day, locatorType='css')
        result = self.util.verifyTextContains(_text_day, text)
        self.stat.mark(result, "Verify Text Day ")
        text1 = self.getText(self._date, locatorType='css')
        result1 = self.util.verifyTextContains(_text_date, text1)
        self.stat.mark(result1, "Verify Text Date")
        text2 = self.getText(self._time_in, locatorType='css')
        result2 = self.util.verifyTextContains(_text_time_in, text2)
        self.stat.mark(result2, "Verify Text Time In")
        text3 = self.getText(self._time_out, locatorType='css')
        result3 = self.util.verifyTextContains(_text_time_out, text3)
        self.stat.mark(result3, "Verify Text Time Out")
        text4 = self.getText(self._time_spent, locatorType='css')
        result4 = self.util.verifyTextContains(_text_time_spent, text4)
        self.stat.mark(result4, "Verify Text Time Spent")
        text5 = self.getText(self._break_time, locatorType='css')
        result5 = self.util.verifyTextContains(_text_break_time, text5)
        self.stat.mark(result5, "Verify Text Break Time")
        text6 = self.getText(self._work_time, locatorType='css')
        result6 = self.util.verifyTextContains(_text_work_time, text6)
        self.stat.mark(result6, "Verify Text Work Time")
        text7 = self.getText(self._absentees, locatorType='link')
        result7 = self.util.verifyTextContains(_text_absentees, text7)
        self.stat.mark(result7, "Verify Text Absentees")
        text8 = self.getText(self._details, locatorType='link')
        result8 = self.util.verifyTextContains(_text_details, text8)
        self.stat.mark(result8, "Verify Text Details")
        text9 = self.getText(self._logs, locatorType='link')
        result9 = self.util.verifyTextContains(_text_logs, text9)
        self.stat.mark(result9, "Verify Text Logs")
        text10 = self.getText(self._add_new, locatorType='css')
        result10 = self.util.verifyTextContains(_text_add_new, text10)
        self.stat.mark(result10, "verify Text Add New")
        text11 = self.getText(self._export, locatorType='css')
        result11 = self.util.verifyTextContains(_text_export, text11)
        self.stat.mark(result11, "Verify Text Export")