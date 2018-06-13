import pytest
import os
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
@pytest.fixture()
def setUp():
    print("This set up is running one time before everytest")
    yield
    print("This will run after evry test")


@pytest.fixture(scope="class")
def oneTimeSetUp(request,browser):

    print("This will run once before every test")
    wdf=WebDriverFactory(browser)
    driver=wdf.getBrowserInstance()
    # if browser=='firefox':
    #     url = "https://learn.letskodeit.com/p/practice/"
    #     driver = webdriver.Firefox()
    #     driver.get(url)
    #     driver.maximize_window()
    #
    # elif browser=='chrome':
    #     driver_location = 'D:\seleniumpythonsoftware\chromedriver.exe'
    #     os.environ['webdriver.chrome.driver'] = driver_location
    #     url = "https://learn.letskodeit.com/p/practice/"
    #     driver = webdriver.Chrome(driver_location)
    #     driver.get(url)
    #     driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("This will run Once after every test")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="This is osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.connfig.getoption("--osType")
