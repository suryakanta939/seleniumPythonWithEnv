from pages.home.login_page import LoginPage
import unittest
from selenium import webdriver
from pages.home.radio_checkBox_page import RadioCheckBox
from pages.home.selectbox_check import SelectBoxCheking
import pytest
import time

class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        url = "https://learn.letskodeit.com/p/practice/"
        cls.driver = webdriver.Firefox()
        cls.driver.get(url)
        cls.driver.maximize_window()

    # def setUp(self):
    #    url = "https://learn.letskodeit.com/p/practice/"
    #    self.driver = webdriver.Firefox()
    #    self.driver.get(url)
    #    self.driver.maximize_window()

    @pytest.mark.run(order=1)
    def test_validation(self):
        driver=self.driver
        lg = LoginPage(driver)
        lg.loginToLetsKode("suryakanta@abacies.com","abcabc")
        driver.back()
        time.sleep(1)
        driver.back()

    @pytest.mark.run(order=2)
    def test_radio_checkBox(self):
        driver=self.driver
        rdc=RadioCheckBox(driver)
        rdc.radioTypeClick()
        rdc.checkBoxTypeClick()

    @pytest.mark.run(order=3)
    def test_select_box(self):
        driver=self.driver
        sel=SelectBoxCheking(driver)
        sel.testSelectBox()


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()



if __name__=="__main__":
    unittest.main()