from base.selenium_driver import SeleniumDriver
from commonutilities.handel_window import HandelWindow
import time
from commonutilities.wait_webpage import WaitForPage
from commonutilities.Action_functions import ActionFunction
from commonutilities.scroll import Scrolling


class OtherELement(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    # This xpath for the open tab
    _openWindow_xapth="//button[@id='openwindow']"
    _all_xapth = "//div[div[contains(text(),'Category:')]]//button[contains(text(),'All')]"
    _testing_xpath = "//a[text()='Software Testing (5)']"
    # *************************************************
    # This xpath is for open tab and childs
    _open_tab_id="opentab"
    #
    _all_author_xpath = "//div[div[contains(text(),'Author:')]]//button[contains(text(),'All')]"
    _author_xpath="//a[contains(text(),'Kode It')]"
    # *************************************************

    _mouseHover_id="mousehover"
    _reload_xpath="//a[text()='Reload']"

    _alert_id="alertbtn"
    _confirm_button_id="confirmbtn"


    def openWindow(self):
        self.clickOnElement("xpath",self._openWindow_xapth)
        hw=HandelWindow(self.driver)
        hw.switchingToWindoByNo(2)
        wt=WaitForPage(self.driver)
        wt.waitPresenceOfElemnet(10,"xpath",self._all_xapth)
        self.clickOnElement("xpath",self._all_xapth)
        self.clickOnElement("xpath",self._testing_xpath)
        url=self.driver.current_url
        print("title is "+url)
        self.driver.close()
        hw.switchingToWindoByNo(1)


    def openTab(self):

        self.clickOnElement("id",self._open_tab_id)
        hw1=HandelWindow(self.driver)
        hw1.switchingToWindoByNo(2)
        # time.sleep(3)
        wt = WaitForPage(self.driver)
        wt.waitElementToBeClickable(15, "xpath", self._all_author_xpath)
        self.clickOnElement("xpath", self._all_author_xpath)
        self.clickOnElement("xpath", self._author_xpath)
        url = self.driver.current_url
        print("title is " + url)
        self.driver.close()
        hw1.switchingToWindoByNo(1)


    def mouseHover(self):
        act=ActionFunction(self.driver)
        scrol=Scrolling(self.driver)
        scrol.scroll_to_exact_element("id",self._mouseHover_id)
        act.hover_on_element("id",self._mouseHover_id)
        self.clickOnElement("xpath",self._reload_xpath)