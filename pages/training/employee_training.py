from base.basepage import BasePage
import utilities.custom_logger as cl
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

    def verifySearchbar(self):
        result = self.isElementPresent(self._search_bar, locatorType='xpath')
        return result

    def verifyTextTitlePage(self):
        text = self.getText(self._page_title, locatorType='css')
        result = self.util.verifyTextContains(self._text_page_title, text)
        return result

    def verifyTextEmployeeTraining(self):
        text = self.getText(self._employee_training, locatorType='link')
        result = self.util.verifyTextContains(self._text_employee_training, text)
        return result

    def verifyTextTrainingEvaluation(self):
        text = self.getText(self._training_evaluation, locatorType='link')
        result = self.util.verifyTextContains(self._text_training_evaluation, text)
        return result

    def verifyTextTrainers(self):
        text = self.getText(self._trainers, locatorType='link')
        result = self.util.verifyTextContains(self._text_trainers, text)
        return result

    def verifyTextTrainingEvents(self):
        text = self.getText(self._training_events, locatorType='link')
        result = self.util.verifyTextContains(self._text_training_events, text)
        return result

    def verifyTextTrainingNeedsAssessment(self):
        text = self.getText(self._training_needs_assessment, locatorType='link')
        result = self.util.verifyTextContains(self._text_training_needs_assessment, text)
        return result

    def verifyTextAddNewTraining(self):
        text = self.getText(self._add_new_training, locatorType='css')
        result = self.util.verifyTextContains(self._text_add_new_training, text)
        return result

    def verifyTextTrainingType(self):
        text = self.getText(self._training_type, locatorType='css')
        result = self.util.verifyTextContains(self._text_training_type, text)
        return result

    def verifyTextTableTitle(self):
        text = self.getText(self._table_title, locatorType='css')
        result = self.util.verifyTextContains(self._text_table_title, text)
        return result

    def verifyTextTrainingFrom(self):
        text = self.getText(self._training_from, locatorType='css')
        result = self.util.verifyTextContains(self._text_training_from, text)
        return result

    def verifyTextTrainingTo(self):
        text = self.getText(self._training_to, locatorType='css')
        result = self.util.verifyTextContains(self._text_training_to, text)
        return result

    def verifyTextActions(self):
        text = self.getText(self._actions, locatorType='css')
        result = self.util.verifyTextContains(self._text_actions, text)
        return result

    def verifyMoreOptions(self):
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def EmployeeTrainingSmoke(self):
        self.nav.Training()
        self.verifyPageTitle(self._title)
        result = self.verifySearchbar()
        self.stat.mark(result, "Verify Search Bar")
        result1 = self.verifyTextTitlePage()
        self.stat.mark(result1, "Verify Text Title Page")
        result2 = self.verifyTextEmployeeTraining()
        self.stat.mark(result2, "Verify Text Employee Training")
        result3 = self.verifyTextTrainingEvaluation()
        self.stat.mark(result3, "Verify Text Training Evaluation")
        result4 = self.verifyTextTrainers()
        self.stat.mark(result4, "Verify Text Trainers")
        result5 = self.verifyTextTrainingEvents()
        self.stat.mark(result5, "Verify Text Training Events")
        result6 = self.verifyTextTrainingNeedsAssessment()
        self.stat.mark(result6, "Verify Text Training Needs Assessment")
        result7 = self.verifyTextAddNewTraining()
        self.stat.mark(result7, "Verify Text Add New Training")
        result8 = self.verifyTextTrainingType()
        self.stat.mark(result8, "Verify Text Training Type")
        result9 = self.verifyTextTableTitle()
        self.stat.mark(result9, "Verify Table Title")
        result10 = self.verifyTextTrainingFrom()
        self.stat.mark(result10, "Verify Text Training From")
        result11 = self.verifyTextTrainingTo()
        self.stat.mark(result11, "Verify Text Training To")
        result12 = self.verifyTextActions()
        self.stat.mark(result12, "Verify Text Actions")
        result13 = self.verifyMoreOptions()
        self.stat.markFinal("Test Employee Training", result13, "Verify More Options")