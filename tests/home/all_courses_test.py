import unittest
import time
import pytest
from pages.home.login_page import LoginPage
from pages.home.all_courses import AllCourses
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, LoginPage)
        self.ac = AllCourses(self.driver, AllCourses)
        self.ts = TestStatus(self.driver, TestStatus)
        self.lp.login("test@email.com", "abcabc")
        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_course(self):
        self.ac.clickAllCourseLink()
        time.sleep(3)
        result = self.ac.verifyAllCourse()
        self.ts.mark(result, "Can't Locate All Courses")
        time.sleep(3)
        self.ac.clickCourseLink()
        result1 = self.ac.verifyCourse()
        self.ts.mark(result1, "Can't Verify Course")
        self.lp.Logout()
        result2 = self.lp.verifySuccessfulLogout()
        self.ts.markFinal("test_Courses", result2, "Logout unsuccessful")

    #@pytest.mark.run(order=2)
    #def test_logout(self):
    #    time.sleep(2)
    #    self.lp.Logout()
    #    result = self.lp.verifySuccessfulLogout()
    #    assert result == True

