from pages.home.login_page import LoginPage
from commonutilities.teststatus import TestStatus
from selenium import webdriver
from pages.home.radio_checkBox_page import RadioCheckBox
from pages.home.selectbox_check import SelectBoxCheking
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.lg = LoginPage(self.driver)
        self.rdc = RadioCheckBox(self.driver)
        self.sel = SelectBoxCheking(self.driver)
        self.ts=TestStatus(self.driver)

    @pytest.mark.run(order=3)
    def test_validation(self):
        driver=self.driver
        result1=self.lg.loginToLetsKode("suryakanta@abacies.com","abcabc")
        self.ts.mark(result1,"did not click")
        driver.back()
        time.sleep(1)
        driver.back()

    @pytest.mark.run(order=2)
    def test_radio_checkBox(self):
        result1=self.rdc.radioTypeClick()
        self.ts.mark(result1,"clicked on all")
        result2=self.rdc.checkBoxTypeClick()
        self.ts.mark(result2,"cliked on check box")

    @pytest.mark.run(order=1)
    def test_select_box(self):
        resul1=self.sel.testSelectBox()
        self.ts.mark(resul1,"clciked on all")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()



