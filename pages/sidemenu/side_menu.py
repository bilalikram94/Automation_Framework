from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class SideMenu(BasePage):
    log = cl.customLogger(logging.DEBUG)
    #  Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
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

    def verifyAttendence(self):
        result = self.isElementPresent(self._attendence, locatorType='link')
        self.stat.mark(result, "Verify Attendence")

    def verifyEmployee(self):
        result1 = self.isElementPresent(self._employee, locatorType='link')
        self.stat.mark(result1, "Verify Employee")

    def verifySupportTicket(self):
        result2 = self.isElementPresent(self._support_ticket, locatorType='link')
        self.stat.mark(result2, "Verify Support Ticket")

    def verifyTraining(self):
        result3 = self.isElementPresent(self._training, locatorType='link')
        self.stat.mark(result3, "Verify Training")

    def verifyTimeOff(self):
        result4 = self.isElementPresent(self._time_off, locatorType='link')
        self.stat.markFinal("Test_Side Menu", result4, "Verify Time Off")

    def SideMenuSmoke(self):
        self.clickSideMenu()
        self.verifyAttendence()
        self.verifyEmployee()
        self.verifySupportTicket()
        self.verifyTraining()
        self.verifyTimeOff()



