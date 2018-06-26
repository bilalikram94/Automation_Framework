import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.fixture()
@ddt
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
@data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Framework/validlogin.csv"))
@unpack
def oneTimeSetUp(request, browser, email, password):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login(email, password)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
