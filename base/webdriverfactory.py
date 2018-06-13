from selenium import  webdriver
import os


class WebDriverFactory():

    def __init__(self,browser):
        self.browser=browser

    def getBrowserInstance(self):

        browser=self.browser
        baseUrl="https://learn.letskodeit.com/p/practice/"
        if browser=='firefox':
            driver=webdriver.Firefox()

        elif browser=='chrome':
            driver_location = 'D:\seleniumpythonsoftware\chromedriver.exe'
            os.environ['webdriver.chrome.driver'] = driver_location
            url = "https://learn.letskodeit.com/p/practice/"
            driver = webdriver.Chrome(driver_location)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        return driver