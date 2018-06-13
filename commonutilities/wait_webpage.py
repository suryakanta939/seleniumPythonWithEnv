import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from base.selenium_driver import SeleniumDriver

class WaitForPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def waitPresenceOfElemnet(self,time,locatorType,locator):
        wait = WebDriverWait(self.driver, time, poll_frequency=1,
                             ignored_exceptions=(NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 NoAlertPresentException))
        wait.until(EC.presence_of_element_located((self.getByType(locatorType),locator)))


    def waitElementToBeVisible(self,time,locatorType,locator):
        wait = WebDriverWait(self.driver, time, poll_frequency=1,
                             ignored_exceptions=(NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 NoAlertPresentException))
        wait.until(EC.visibility_of_element_located((self.getByType(locatorType),locator)))


    def waitElementToBeClickable(self,time,locatorType,locator):

        wait = WebDriverWait(self.driver,time, poll_frequency=1,
                             ignored_exceptions=(NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 NoAlertPresentException))
        wait.until(EC.element_to_be_clickable((self.getByType(locatorType),locator)))