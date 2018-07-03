from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.teststatus import Status
from pages.home.navigation import Navigation
import logging


class SupportTicket(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _my_ticket = "My Tickets"  # By Link
    _company_tickets = "Company Tickets"  # By Link
    _search_bar = "[class='inner-page-search flex-12'] [type]"  # By CSS
    _open_ticket = ".ml10"  # By CSS
    _text_supportticket = ".text-dark:nth-of-type(1)"  # By CSS
    _text_open = "//div[@id='my-tickets']/span[.=' Open (4)']"  # By Xpath
    _tickets = "#my-tickets [class='col-lg-4 mb20']:nth-of-type(1) .support-link"  # By CSS
    _title = "Advanced HRMS - Staging"

    def __init__(self, driver):
        super().__init__(driver)
        self.ts = Status(driver)
        self.nav = Navigation(driver)

    def verifyMyTickets(self):
        result = self.isElementPresent(self._my_ticket, locatorType='link')
        self.ts.mark(result, "Verify My Tickets")

    def verifyCompanyTickets(self):
        result1 = self.isElementPresent(self._company_tickets, locatorType='link')
        self.ts.mark(result1, "Verify Company Tickets")

    def verifySearchBar(self):
        result2 = self.isElementPresent(self._search_bar, locatorType='css')
        self.ts.mark(result2, "Verify Search Bar")

    def verifyOpenTicket(self):
        result3 = self.isElementPresent(self._open_ticket, locatorType='css')
        self.ts.mark(result3, "Verify Open Ticket")

    def verifyTickets(self):
        result4 = self.isElementPresent(self._tickets, locatorType='css')
        self.ts.mark(result4, "Verify Tickets")

    def verifyTextSupport(self):
        text = self.getText(self._text_supportticket, locatorType='css')
        result5 = self.util.verifyTextContains("Support Tickets", text)
        self.ts.mark(result5, "Verify Support Ticket Text")

    def verifyTextOpen(self):
        text = self.getText(self._text_open, locatorType='xpath')
        result6 = self.util.verifyTextContains("Open (4)", text)
        self.ts.markFinal("Test_Support Ticket", result6, "Verify Open Text")

    def SupportTicketSmoke(self):
        self.nav.SupportTicket()
        self.verifyPageTitle(self._title)
        self.verifyMyTickets()
        self.verifyCompanyTickets()
        self.verifySearchBar()
        self.verifyOpenTicket()
        self.verifyTickets()
        self.verifyTextSupport()
        self.verifyTextOpen()