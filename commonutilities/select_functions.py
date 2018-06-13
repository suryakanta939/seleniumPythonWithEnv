from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select


class SelectFunction(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def selectBytext(self,locatorType,locator,textToselct):
        sel=Select(self.getElement(locatorType,locator))
        sel.select_by_visible_text(textToselct)


    def selectByIndex(self,locatorType,locator,indexToselect):
        sel=Select(self.getElement(locatorType,locator))
        sel.select_by_index(indexToselect)

    def selectByValue(self,locatorType,locator,valueToselct):
        sel=Select(self.getElement(locatorType,locator))
        sel.select_by_value(valueToselct)

