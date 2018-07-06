from base.basepage import BasePage
import utilities.custom_logger as cl
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

    def verifyFirstName(self):
        result = self.isElementPresent(self._first_name, locatorType='xpath')
        return result

    def verifyLastName(self):
        result = self.isElementPresent(self._last_name, locatorType='xpath')
        return result

    def verifyEmployeeCard(self):
        result = self.isElementPresent(self._employee_card, locatorType='xpath')
        return result

    def verifyGender(self):
        result = self.isElementPresent(self._gender, locatorType='xpath')
        return result

    def verifyDateOfJoining(self):
        result = self.isElementPresent(self._date_of_joining, locatorType='xpath')
        return result

    def verifyDepartment(self):
        result = self.isElementPresent(self._department)
        return result

    def verifyDesignation(self):
        result = self.isElementPresent(self._designation)
        return result

    def verifyReportingPerson(self):
        result = self.isElementPresent(self._reporting_person, locatorType='css')
        return result

    def verifyTaxRule(self):
        result = self.isElementPresent(self._tax_rule, locatorType='css')
        return result

    def verifyUserRole(self):
        self.scrollIntoView(self._user_role, locatorType='css')
        self.util.sleep(3)
        result = self.isElementPresent(self._user_role, locatorType='css')
        return result

    def verifyPolicyType(self):
        self.scrollIntoView(self._policy_type, locatorType='css')
        result = self.isElementPresent(self._policy_type, locatorType='css')
        return result

    def NewEmployeeSmoke(self):
        self.nav.NewEmployee()
        self.verifyPageTitle(self._page_title)
        result = self.verifyFirstName()
        self.stat.mark(result, "Verify First Name")
        result1 = self.verifyLastName()
        self.stat.mark(result1, "Verify Last Name")
        result2 = self.verifyEmployeeCard()
        self.stat.mark(result2, "Verify Employee Card")
        result3 = self.verifyGender()
        self.stat.mark(result3, "Verify Gender")
        result4 = self.verifyDateOfJoining()
        self.stat.mark(result4, "Verify Date Of Joining")
        result5 = self.verifyDepartment()
        self.stat.mark(result5, "Verify Department")
        result6 = self.verifyDesignation()
        self.stat.mark(result6, "Verify Designation")
        result7 = self.verifyReportingPerson()
        self.stat.mark(result7, "Verify Reporting Person")
        result8 = self.verifyTaxRule()
        self.stat.mark(result8, "Verify Tax Rule")
        result9 = self.verifyUserRole()
        self.stat.mark(result9, "Verify User Role")
        result10 = self.verifyPolicyType()
        self.stat.markFinal("Test New Employee", result10, "Verify Policy Type")