from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementsList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element found with: " + locator + "and locatorType: " + locatorType)
        except:
            self.log.error("Element List not found with locator: " + locator + "and locatorType" + locatorType)
            return element

    def elementClick(self, locator, locatorType="id", element=None):
        """
        Click on an element ->Modified
        either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.error("Clicked on element with locator: " + locator + "and locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id", element=None):
        try:
            if locator:  # this means if the locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found by locator:" + locator + " and locatorType:" + locatorType)
                return True
            else:
                self.log.info("Element not found by locator" + locator + " and locatorType:" + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page:" + locator)
        except:
            self.log.info("Element not appeared on the web page" + locator)
            print_stack()
        return element

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/home/bilalikram/PycharmProjects/Automation_Framework/screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        # noinspection PyBroadException
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        New Method
        Get Text on an element
        Either provide element or combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = element.getElement(locator, locatorType)
            self.log.debug("Before Finding Text")
            text = element.text
            self.log.debug("after Finding Text" + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("inner text")
            if len(text) != 0:
                self.log.info("Getting text on element ::" + info)
                self.log.info("The Text is ::'" + text + "'")
                text = text.strip()

        except:
            self.log.error("###Failed To Get Text On Element !!!" + info)
            print_stack()
            text = None

        return text

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        New Method
        Check if element is displayed
        Either provide element or combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = element.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator:: " + locator + "and locatorType" + locatorType)
            else:
                self.log.error("Element not displayed with locator:: " + locator + "and locatorType" + locatorType)
            return isDisplayed
        except:
            print("Element NOT Found")
            return False

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll UP
            self.driver.execute_script("window.scrollBy(0,-1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0,1000);")
