from selenium.webdriver import ActionChains
from selenium import webdriver
from base.selenium_driver import SeleniumDriver

# This class is all about the action class functions

class ActionFunction(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    # this function will help to mouse hove on the element

    def hover_on_element(self,locatorType,locator):
        act = ActionChains(self.driver)
        act.move_to_element(self.getElement(locatorType,locator)).perform()


    def move_to_element_cordinate(self,locatorType,locator):
        act = ActionChains(self.driver)
        element=self.getElement(locatorType,locator)
        loc = element.location
        x_offset = loc['x']
        y_offset = loc['y']
        act.move_to_element_with_offset(element,x_offset,y_offset).perform()

    def dragAndDrop(self,locatorType_source,locator_source,locatorTyep_dest,locator_dest):
        act = ActionChains(self.driver)
        element_src = self.getElement(locatorType_source, locator_source)
        element_dst = self.getElement(locatorTyep_dest, locator_dest)
        act.drag_and_drop(element_src,element_dst).perform()

