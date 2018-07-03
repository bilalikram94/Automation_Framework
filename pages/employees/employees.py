from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Employees(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _search_bar = "[type='text']"  # By CSS
    _new_employees = "New Employee"  # By Link
    _page_header = "//main[@id='wrapper']/div[@class='right-content']//strong[@class='text-dark']"  # By Xpath
    _title = "Advanced HRMS - Staging"

    def __init__(self, driver):
        super().__init__(driver)

    def verifyPageheader(self):
        text = self.getText(self._page_header, locatorType='xpath')
        result = self.util.verifyTextContains("employees", text)
        self.stat.mark(result, "Verify Page Header")

    def verifyNewEmployee(self):
        result1 = self.isElementPresent(self._new_employees, locatorType='link')
        self.stat.mark(result1, "Verify New Employee")

    def verifySearchBar(self):
        result2 = self.isElementPresent(self._search_bar, locatorType='css')
        self.stat.markFinal("Test Employees", result2, "Verify Search bar")

    def EmployeesSmoke(self):
        self.nav.Employee()
        self.util.sleep(2)
        self.verifyPageTitle(self._title)
        self.verifyPageheader()
        self.verifyNewEmployee()
        self.verifySearchBar()
