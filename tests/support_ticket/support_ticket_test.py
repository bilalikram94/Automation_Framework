import pytest
import unittest
from pages.support_ticket.support_ticket import SupportTicket


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSupportTicket(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.st = SupportTicket(self.driver)

    @pytest.mark.run(order=1)
    def test_SupportTicket(self):
        self.st.SupportTicketSmoke()
