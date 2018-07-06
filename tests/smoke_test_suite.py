import unittest
from tests.home.login_test import LoginTests
from tests.sidemenu.test_side_menu import TestSideMenu
from tests.attendence.logs_test import TestLogs
from tests.attendence.details_test import TestDetails
from tests.attendence.absentees_test import TestAbsentees
from tests.employees.employee_test import TestEmployees
from tests.employees.new_employee_test import TestNewEmployee
from tests.support_ticket.support_ticket_test import TestSupportTicket
from tests.training.employee_training_test import TestEmployeeTraining

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSideMenu)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestLogs)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestDetails)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestAbsentees)
tc6 = unittest.TestLoader().loadTestsFromTestCase(TestEmployees)
tc7 = unittest.TestLoader().loadTestsFromTestCase(TestNewEmployee)
tc8 = unittest.TestLoader().loadTestsFromTestCase(TestSupportTicket)
tc9 = unittest.TestLoader().loadTestsFromTestCase(TestEmployeeTraining)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9])

unittest.TextTestRunner(verbosity=2).run(smokeTest)