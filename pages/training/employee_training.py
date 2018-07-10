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

    def __init__(self, driver):
        super().__init__(driver)

    def verifySearchbar(self):
        result = self.isElementPresent(self._search_bar, locatorType='xpath')
        return result

    def verifyTextTitlePage(self, page_title):
        text = self.getText(self._page_title, locatorType='css')
        result = self.util.verifyTextContains(page_title, text)
        return result

    def verifyTextEmployeeTraining(self, emp_train):
        text = self.getText(self._employee_training, locatorType='link')
        result = self.util.verifyTextContains(emp_train, text)
        return result

    def verifyTextTrainingEvaluation(self, train_eval):
        text = self.getText(self._training_evaluation, locatorType='link')
        result = self.util.verifyTextContains(train_eval, text)
        return result

    def verifyTextTrainers(self, trainers):
        text = self.getText(self._trainers, locatorType='link')
        result = self.util.verifyTextContains(trainers, text)
        return result

    def verifyTextTrainingEvents(self, train_events):
        text = self.getText(self._training_events, locatorType='link')
        result = self.util.verifyTextContains(train_events, text)
        return result

    def verifyTextTrainingNeedsAssessment(self, train_assess):
        text = self.getText(self._training_needs_assessment, locatorType='link')
        result = self.util.verifyTextContains(train_assess, text)
        return result

    def verifyTextAddNewTraining(self, add_train):
        text = self.getText(self._add_new_training, locatorType='css')
        result = self.util.verifyTextContains(add_train, text)
        return result

    def verifyTextTrainingType(self, train_type):
        text = self.getText(self._training_type, locatorType='css')
        result = self.util.verifyTextContains(train_type, text)
        return result

    def verifyTextTableTitle(self, table_title):
        text = self.getText(self._table_title, locatorType='css')
        result = self.util.verifyTextContains(table_title, text)
        return result

    def verifyTextTrainingFrom(self, train_frm):
        text = self.getText(self._training_from, locatorType='css')
        result = self.util.verifyTextContains(train_frm, text)
        return result

    def verifyTextTrainingTo(self, train_to):
        text = self.getText(self._training_to, locatorType='css')
        result = self.util.verifyTextContains(train_to, text)
        return result

    def verifyTextActions(self, actions):
        text = self.getText(self._actions, locatorType='css')
        result = self.util.verifyTextContains(actions, text)
        return result

    def verifyMoreOptions(self):
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def EmployeeTrainingSmoke(self,page_title,emp_train,train_eval,trainers,train_events,train_assess,add_train,train_type,table_title,train_frm,train_to,actions):
        self.nav.Training()
        self.verifyPageTitle(self._title)
        result = self.verifySearchbar()
        self.stat.mark(result, "Verify Search Bar")
        result1 = self.verifyTextTitlePage(page_title)
        self.stat.mark(result1, "Verify Text Title Page")
        result2 = self.verifyTextEmployeeTraining(emp_train)
        self.stat.mark(result2, "Verify Text Employee Training")
        result3 = self.verifyTextTrainingEvaluation(train_eval)
        self.stat.mark(result3, "Verify Text Training Evaluation")
        result4 = self.verifyTextTrainers(trainers)
        self.stat.mark(result4, "Verify Text Trainers")
        result5 = self.verifyTextTrainingEvents(train_events)
        self.stat.mark(result5, "Verify Text Training Events")
        result6 = self.verifyTextTrainingNeedsAssessment(train_assess)
        self.stat.mark(result6, "Verify Text Training Needs Assessment")
        result7 = self.verifyTextAddNewTraining(add_train)
        self.stat.mark(result7, "Verify Text Add New Training")
        result8 = self.verifyTextTrainingType(train_type)
        self.stat.mark(result8, "Verify Text Training Type")
        result9 = self.verifyTextTableTitle(table_title)
        self.stat.mark(result9, "Verify Table Title")
        result10 = self.verifyTextTrainingFrom(train_frm)
        self.stat.mark(result10, "Verify Text Training From")
        result11 = self.verifyTextTrainingTo(train_to)
        self.stat.mark(result11, "Verify Text Training To")
        result12 = self.verifyTextActions(actions)
        self.stat.mark(result12, "Verify Text Actions")
        result13 = self.verifyMoreOptions()
        self.stat.markFinal("Test Employee Training", result13, "Verify More Options")