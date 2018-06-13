'''
This function is all  about the radio and check box

'''

from base.selenium_driver import SeleniumDriver
import time

class RadioCheckBox(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _radio_xpath="//input[@type='radio']"

    _check_box_xapth="//input[@type='checkbox']"

    def radioTypeClick(self):
        allradio=self.getElements("xpath",self._radio_xpath)

        for radio in allradio:
            radio.click()
            time.sleep(2)

    def checkBoxTypeClick(self):
        allcheckbox = self.getElements("xpath", self._check_box_xapth)

        for checkbox in allcheckbox:
            checkbox.click()
            time.sleep(2)

