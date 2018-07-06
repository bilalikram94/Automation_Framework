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
        self.nav = Navigation(driver)

    def verifyMyTickets(self):
        result = self.isElementPresent(self._my_ticket, locatorType='link')
        return result

    def verifyCompanyTickets(self):
        result = self.isElementPresent(self._company_tickets, locatorType='link')
        return result

    def verifySearchBar(self):
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def verifyOpenTicket(self):
        result = self.isElementPresent(self._open_ticket, locatorType='css')
        return result

    def verifyTickets(self):
        result = self.isElementPresent(self._tickets, locatorType='css')
        return result

    def verifyTextSupport(self):
        text = self.getText(self._text_supportticket, locatorType='css')
        result = self.util.verifyTextContains("Support Tickets", text)
        return result

    def verifyTextOpen(self):
        text = self.getText(self._text_open, locatorType='xpath')
        result = self.util.verifyTextContains("Open (4)", text)
        return result

    def SupportTicketSmoke(self):
        self.nav.SupportTicket()
        self.verifyPageTitle(self._title)
        result = self.verifyMyTickets()
        self.stat.mark(result, "Verify My Tickets")
        result1 = self.verifyCompanyTickets()
        self.stat.mark(result1, "Verify Company Tickets")
        result2 = self.verifySearchBar()
        self.stat.mark(result2, "Verify Search Bar")
        result3 = self.verifyOpenTicket()
        self.stat.mark(result3, "Verify Open Ticket")
        result4 = self.verifyTickets()
        self.stat.mark(result4, "Verify Tickets")
        result5 = self.verifyTextSupport()
        self.stat.mark(result5, "Verify Support Ticket Text")
        result6 = self.verifyTextOpen()
        self.stat.markFinal("Test_Support Ticket", result6, "Verify Open Text")