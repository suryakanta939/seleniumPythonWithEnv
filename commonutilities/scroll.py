from base.selenium_driver import SeleniumDriver
import time

class Scrolling(SeleniumDriver):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    def scroll_up(self):
        self.driver.execute_script("window.scrollBy(0,-1500);")


    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,1500);")


    def scroll_to_exact_element(self,locatorType,locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",self.getElement(locatorType,locator))
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-150);")