from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Employees(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _search_bar = "[type='text']"  # By CSS
    _new_employees = "New Employee"  # By Link
    _page_header = "//main[@id='wrapper']/div[@class='right-content']//strong[@class='text-dark']"  # By Xpath
    _title = "Advanced HRMS - Staging"  # Title
    _employees = ".owl-stage div:nth-of-type(1) .emp-info"  # By CSS
    _active = ".owl-stage div:nth-of-type(2) .emp-info"  # By CSS
    _inactive = ".owl-stage div:nth-of-type(3) .emp-info"  # By CSS
    _full_time = ".owl-stage div:nth-of-type(4) .emp-info"  # By CSS
    _part_time = ".owl-stage div:nth-of-type(5) .emp-info"  # By CSS
    _probation = ".owl-stage div:nth-of-type(6) .emp-info"  # By CSS
    _contractual = ".owl-stage div:nth-of-type(7) .emp-info"  # By CSS
    _name = "thead tr th:nth-of-type(1)"  # By CSS
    _designation = "thead tr th:nth-of-type(2)"  # By CSS
    _department = "thead tr th:nth-of-type(3)"  # By CSS
    _location = "thead tr th:nth-of-type(4)"  # By CSS
    _status = "thead tr th:nth-of-type(5)"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)

    def verifyPageheader(self):
        text = self.getText(self._page_header, locatorType='xpath')
        result = self.util.verifyTextContains("employees", text)
        return result

    def verifyNewEmployee(self):
        result = self.isElementPresent(self._new_employees, locatorType='link')
        return result

    def verifySearchBar(self):
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def EmployeesSmoke(self):
        self.nav.Employee()
        self.util.sleep(2)
        self.verifyPageTitle(self._title)
        result = self.verifyPageheader()
        self.stat.mark(result, "Verify Page Header")
        result1 = self.verifyNewEmployee()
        self.stat.mark(result1, "Verify New Employee")
        result2 = self.verifySearchBar()
        self.stat.markFinal("Test_Employees Smoke", result2, "Verify Search Bar")

    def verifyTextEmployee(self, newemployeetext, nametext, designation, department, location, status):
        text = self.getText(self._new_employees, locatorType='link')
        result = self.util.verifyTextContains(newemployeetext, text)
        self.stat.mark(result, "Verify Text Employees")
        text2 = self.getText(self._name, locatorType='css')
        result2 = self.util.verifyTextContains(nametext, text2)
        self.stat.mark(result2, "Verify Text Name")
        text3 = self.getText(self._designation, locatorType='css')
        result3 = self.util.verifyTextContains(designation, text3)
        self.stat.mark(result3, "Verify Text Designation")
        text4 = self.getText(self._department, locatorType='css')
        result4 = self.util.verifyTextContains(department, text4)
        self.stat.mark(result4, "Verify Text Department")
        text5 = self.getText(self._location, locatorType='css')
        result5 = self.util.verifyTextContains(location, text5)
        self.stat.mark(result5, "Verify Text Location")
        text6 = self.getText(self._status, locatorType='css')
        result6 = self.util.verifyTextContains(status, text6)
        self.stat.markFinal("Test_Text Employees", result6, "Verify Text Status")