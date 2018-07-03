from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.teststatus import Status
from pages.home.navigation import Navigation
import logging


class Training(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _title = "Advanced HRMS - Staging"
    _search_bar = "//div[@id='basic_search']/input[@type='text']"  # By Xpath
    _page_title = ".page-title"  # By CSS
    _employee_training = "Employee Training"  # By Link
    _training_evaluation = "Training Evaluations"  # By Link
    _trainers = "Trainers"  # By Link
    _training_events = "Training Events"  # By Link
    _training_needs_assessment = "Training Needs Assessment"  # By Link
    _add_new_training = ".flex-v-middle .btn-action"  # By CSS
    _training_type = "thead tr th:nth-of-type(1)"  # By CSS
    _table_title = "thead tr th:nth-of-type(2)"  # By CSS
    _training_from = "thead tr th:nth-of-type(3)"  # By CSS
    _training_to = "thead tr th:nth-of-type(4)"  # By CSS
    _actions = "thead .text-right"  # By CSS
    _more_options = "tbody tr:nth-of-type(1) .dropdown"  # By CSS
    _text_page_title = "employee training"
    _text_employee_training = "employee training"  # Text
    _text_training_evaluation = "training evaluations"  # Text
    _text_trainers = "trainers"  # Text
    _text_training_events = "training events"  # Text
    _text_training_needs_assessment = "training needs assessment"  # Text
    _text_add_new_training = "add new training"  # Text
    _text_training_type = "training type"  # Text
    _text_table_title = "title"  # Text
    _text_training_from = "training from"  # Text
    _text_training_to = "training to"  # Text
    _text_actions = "actions"  # Text

    def __init__(self, driver):
        super().__init__(driver)
        self.stat = Status(driver)
        self.nav = Navigation(driver)

    def verifySearchbar(self):
        result = self.isElementPresent(self._search_bar, locatorType='xpath')
        self.stat.mark(result, "Verify Search Bar")

    def verifyTextTitlePage(self):
        text = self.getText(self._page_title, locatorType='css')
        result1 = self.util.verifyTextContains(self._text_page_title, text)
        self.stat.mark(result1, "Verify Text Title Page")

    def verifyTextEmployeeTraining(self):
        text = self.getText(self._employee_training, locatorType='link')
        result2 = self.util.verifyTextContains(self._text_employee_training, text)
        self.stat.mark(result2, "Verify Text Employee Training")

    def verifyTextTrainingEvaluation(self):
        text = self.getText(self._training_evaluation, locatorType='link')
        result3 = self.util.verifyTextContains(self._text_training_evaluation, text)
        self.stat.mark(result3, "Verify Text Training Evaluation")

    def verifyTextTrainers(self):
        text = self.getText(self._trainers, locatorType='link')
        result4 = self.util.verifyTextContains(self._text_trainers, text)
        self.stat.mark(result4, "Verify Text Trainers")

    def verifyTextTrainingEvents(self):
        text = self.getText(self._training_events, locatorType='link')
        result5 = self.util.verifyTextContains(self._text_training_events, text)
        self.stat.mark(result5, "Verify Text Training Events")

    def verifyTextTrainingNeedsAssessment(self):
        text = self.getText(self._training_needs_assessment, locatorType='link')
        result6 = self.util.verifyTextContains(self._text_training_needs_assessment, text)
        self.stat.mark(result6, "Verify Text Training Needs Assessment")

    def verifyTextAddNewTraining(self):
        text = self.getText(self._add_new_training, locatorType='css')
        result7 = self.util.verifyTextContains(self._text_add_new_training, text)
        self.stat.mark(result7, "Verify Text Add New Training")

    def verifyTextTrainingType(self):
        text = self.getText(self._training_type, locatorType='css')
        result8 = self.util.verifyTextContains(self._text_training_type, text)
        self.stat.mark(result8, "Verify Text Training Type")

    def verifyTextTableTitle(self):
        text = self.getText(self._table_title, locatorType='css')
        result9 = self.util.verifyTextContains(self._text_table_title, text)
        self.stat.mark(result9, "Verify Table Title")

    def verifyTextTrainingFrom(self):
        text = self.getText(self._training_from, locatorType='css')
        result10 = self.util.verifyTextContains(self._text_training_from, text)
        self.stat.mark(result10, "Verify Text Training From")

    def verifyTextTrainingTo(self):
        text = self.getText(self._training_to, locatorType='css')
        result11 = self.util.verifyTextContains(self._text_training_to, text)
        self.stat.mark(result11, "Verify Text Training To")

    def verifyTextActions(self):
        text = self.getText(self._actions, locatorType='css')
        result12 = self.util.verifyTextContains(self._text_actions, text)
        self.stat.mark(result12, "Verify Text Actions")

    def verifyMoreOptions(self):
        result13 = self.isElementPresent(self._more_options, locatorType='css')
        self.stat.markFinal("Test Employee Training", result13, "Verify More Options")

    def EmployeeTrainingSmoke(self):
        self.nav.Training()
        self.verifyPageTitle(self._title)
        self.verifySearchbar()
        self.verifyTextTitlePage()
        self.verifyTextEmployeeTraining()
        self.verifyTextTrainingEvaluation()
        self.verifyTextTrainers()
        self.verifyTextTrainingEvents()
        self.verifyTextTrainingNeedsAssessment()
        self.verifyTextAddNewTraining()
        self.verifyTextTrainingType()
        self.verifyTextTableTitle()
        self.verifyTextTrainingFrom()
        self.verifyTextTrainingTo()
        self.verifyTextActions()
        self.verifyMoreOptions()