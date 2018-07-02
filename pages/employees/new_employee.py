from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.teststatus import Status
from pages.home.navigation import Navigation
import logging


class NewEmployee(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _first_name = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='fname']"  # Xpath
    _last_name = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='lname']"  # By Xpath
    _employee_card = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='employee_code']"  # By Xpath
    _gender = "//main[@id='wrapper']//div[@class='container']/div[@class='row']/div[@class='col-lg-10']/form[@role='form']/div[1]/div[@class='panel-body']/div[3]/div[1]/span//span[@role='combobox'] "  # By Xpath
    _date_of_joining = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='doj']"  # By Xpath
    _department = "select2-department_id-container"  # By ID
    _designation = "select2-designation-container"  # By ID
    _reporting_person = ".select2-selection--multiple .select2-selection__rendered"  # By CSS
    _tax_rule = ".add-employee-form .row:nth-of-type(2) [class='col-md-5 form-group']:nth-of-type(2) .select2-selection__rendered"  # By CSS
    _user_role = ".add-employee-form .panel:nth-of-type(2) .row:nth-of-type(3) .select2-selection--single"  # By CSS
    _policy_type = ".add-employee-form .panel:nth-of-type(3) .select2-selection__rendered"  # By CSS
    _page_title = "Advanced HRMS - Staging"

    def __init__(self, driver):
        super().__init__(driver)
        self.ts = Status(driver)
        self.nav = Navigation(driver)

    def verifyFirstName(self):
        result = self.isElementPresent(self._first_name, locatorType='xpath')
        self.ts.mark(result, "Verify First Name")

    def verifyLastName(self):
        result1 = self.isElementPresent(self._last_name, locatorType='xpath')
        self.ts.mark(result1, "Verify Last Name")

    def verifyEmployeeCard(self):
        result2 = self.isElementPresent(self._employee_card, locatorType='xpath')
        self.ts.mark(result2, "Verify Employee Card")

    def verifyGender(self):
        result3 = self.isElementPresent(self._gender, locatorType='xpath')
        self.ts.mark(result3, "Verify Gender")

    def verifyDateOfJoining(self):
        result4 = self.isElementPresent(self._date_of_joining, locatorType='xpath')
        self.ts.mark(result4, "Verify Date Of Joining")

    def verifyDepartment(self):
        result5 = self.isElementPresent(self._department)
        self.ts.mark(result5, "Verify Department")

    def verifyDesignation(self):
        result6 = self.isElementPresent(self._designation)
        self.ts.mark(result6, "Verify Designation")

    def verifyReportingPerson(self):
        result7 = self.isElementPresent(self._reporting_person, locatorType='css')
        self.ts.mark(result7, "Verify Reporting Person")

    def verifyTaxRule(self):
        result8 = self.isElementPresent(self._tax_rule, locatorType='css')
        self.ts.mark(result8, "Verify Tax Rule")

    def verifyUserRole(self):
        self.scrollIntoView(self._user_role, locatorType='css')
        self.util.sleep(3)
        result9 = self.isElementPresent(self._user_role, locatorType='css')
        self.ts.mark(result9, "Verify User Role")

    def verifyPolicyType(self):
        self.scrollIntoView(self._policy_type, locatorType='css')
        result10 = self.isElementPresent(self._policy_type, locatorType='css')
        self.ts.markFinal("Test New Employee", result10, "Verify Policy Type")

    def NewEmployeeSmoke(self):
        self.nav.NewEmployee()
        self.verifyPageTitle(self._page_title)
        self.verifyFirstName()
        self.verifyLastName()
        self.verifyEmployeeCard()
        self.verifyGender()
        self.verifyDateOfJoining()
        self.verifyDepartment()
        self.verifyDesignation()
        self.verifyReportingPerson()
        self.verifyTaxRule()
        self.verifyUserRole()
        self.verifyPolicyType()