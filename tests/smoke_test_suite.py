import unittest
from tests.home.login_test import LoginTests
from tests.home.sidemenu.test_side_menu import TestSideMenu
from tests.attendence.logs_test import TestLogs
from tests.attendence.details_test import TestDetails
from tests.attendence.absentees_test import TestAbsentees

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSideMenu)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestLogs)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestDetails)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestAbsentees)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

unittest.TextTestRunner(verbosity=2).run(smokeTest)