import unittest
from selenium import webdriver
from pages.practice.other_element_page import OtherELement
import time


class TestOtherElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url="https://learn.letskodeit.com/p/practice/"
        cls.driver=webdriver.Firefox()
        cls.driver.get(cls.url)
        cls.driver.maximize_window()


    def test_window_handel(self):
        driver=self.driver
        oth=OtherELement(driver)
        oth.openWindow()
        driver.refresh()
        oth.openTab()

    # def test_open_tab(self):
    #     driver = self.driver
    #     oth = OtherELement(driver)
    #     oth.openTab()

    def test_mouseHover(self):
        driver=self.driver
        other=OtherELement(driver)
        other.mouseHover()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()

