from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Navigation(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    # locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
    _employee = 'Employees'  # By Link
    _support_ticket = 'Support Tickets'  # By Link
    _time_off = 'Time Off'  # By Link
    _training = 'Training'  # By Link
    _new_employees = "New Employee"  # By Link
    _details = "Detail"  # By Link

    def Attendence(self):
        self.elementClick(self._side_menu, locatorType='xpath')
        self.elementClick(self._attendence, locatorType='link')

    def Employee(self):
        self.elementClick(self._side_menu, locatorType='xpath')
        self.elementClick(self._employee, locatorType='link')

    def SupportTicket(self):
        self.elementClick(self._side_menu, locatorType='xpath')
        self.elementClick(self._support_ticket, locatorType='link')

    def TimeOff(self):
        self.elementClick(self._side_menu, locatorType="xpath")
        self.elementClick(self._time_off, locatorType='link')

    def Training(self):
        self.elementClick(self._side_menu, locatorType="xpath")
        self.elementClick(self._training, locatorType='link')

    def NewEmployee(self):
        self.Employee()
        self.elementClick(self._new_employees, locatorType='link')

    def Details(self):
        self.Attendence()
        self.elementClick(self._details, locatorType='link')