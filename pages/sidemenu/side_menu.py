from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class SideMenu(BasePage):
    log = cl.customLogger(logging.DEBUG)
    #  Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendance = "Attendance"  # By Link
    _employee = 'Employees'  # By Link
    _support_ticket = 'Support Tickets'  # By Link
    _time_off = 'Time Off'  # By Link
    _training = 'Training'  # By Link
    _logs = "Logs"  # By Link
    _detail = "Detail"  # By Link
    _absentee = "Absentees"  # By Link
    _more_options = ".advance-btn"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS
    _notifications = "//ul[@id='cd-primary-nav']/li[4]/a[@href='#']"  # By Xpath

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickSideMenu(self):
        self.elementClick(self._side_menu, locatorType='xpath')
        self.util.sleep(3)

    def verifyAttendance(self):
        result = self.isElementPresent(self._attendance, locatorType='link')
        return result

    def verifyEmployee(self):
        result = self.isElementPresent(self._employee, locatorType='link')
        return result

    def verifySupportTicket(self):
        result = self.isElementPresent(self._support_ticket, locatorType='link')
        return result

    def verifyTraining(self):
        result = self.isElementPresent(self._training, locatorType='link')
        return result

    def verifyTimeOff(self):
        result = self.isElementPresent(self._time_off, locatorType='link')
        return result

    def SideMenuSmoke(self):
        self.clickSideMenu()
        result = self.verifyAttendance()
        self.stat.mark(result, "Verify Attendence")
        result1 = self.verifyEmployee()
        self.stat.mark(result1, "Verify Employee")
        result2 = self.verifySupportTicket()
        self.stat.mark(result2, "Verify Support Ticket")
        result3 = self.verifyTraining()
        self.stat.mark(result3, "Verify Training")
        result4 = self.verifyTimeOff()
        self.stat.markFinal("Test_Side Menu", result4, "Verify Time Off")

    def SideMenuText(self, _text_attendance, _text_employee, _text_support_ticket, _text_training, _text_time_off):
        text = self.getText(self._attendance, locatorType='link')
        result = self.util.verifyTextContains(_text_attendance, text)
        self.stat.mark(result, "Verify Text Attendence")
        text1 = self.getText(self._employee, locatorType='link')
        result1 = self.util.verifyTextContains(_text_employee, text1)
        self.stat.mark(result1, "Verify Text Employee")
        text2 = self.getText(self._support_ticket, locatorType='link')
        result2 = self.util.verifyTextContains(_text_support_ticket, text2)
        self.stat.mark(result2, "Verify Text Support Ticket")
        text3 = self.getText(self._training, locatorType='link')
        result3 = self.util.verifyTextContains(_text_training, text3)
        self.stat.mark(result3, "Verify Text Training")
        text4 = self.getText(self._time_off, locatorType='link')
        result4 = self.util.verifyTextContains(_text_time_off, text4)
        self.stat.markFinal("Test_Logs Text", result4, "Verify Text Time Off")