'''
this class will contain all the common functions

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
import os

import time
class SeleniumDriver():


    def __init__(self,driver):
        self.driver=driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            print("Screenshot save to directory: " + destinationFile)
        except:
            print("### Exception Occurred when taking screenshot")
            print_stack()
    # this function is to get the locator type

    def getByType(self,locatorType):
        locatorType=locatorType.lower()

        try:

            if locatorType=='id':
                return By.ID

            elif locatorType=='name':
                return By.NAME

            elif locatorType=='xpath':
                return By.XPATH

            elif locatorType=='classname':
                return By.CLASS_NAME

            elif locatorType=='linktext':
                return By.LINK_TEXT

            elif locatorType=='partiallinktext':
                return By.PARTIAL_LINK_TEXT

            elif locatorType=='tagname':
                return By.TAG_NAME

            elif locatorType=='cssselector':
                return By.CSS_SELECTOR

        except:
            print("The availbale locator are id,name,xpath,classname,linktext,partiallinktext"
                  "tagname,cssselector ")
            print_stack()
            raise Exception("element is not fund by the locator")

    # This function is going to return the web element

    def getElement(self,locatorType,locator):

        element=None
        locatorType = self.getByType(locatorType)
        element = self.driver.find_element(locatorType, locator)
        print("found the element by the locator type " + locatorType + " and by the locator " + locator)
        return element


    # This function is going to return the web elements

    def getElements(self, locatorType, locator):

        elements = None
        locatorType = self.getByType(locatorType)
        elements = self.driver.find_elements(locatorType, locator)

        return elements

    # This function is to click on the web element

    def clickOnElement(self,locatorType,locator):
        self.getElement(locatorType, locator).click()
        print("clicked on the element by the locator type " + locatorType + " and by the locator " + locator)


    # This function will help to send the value to the element

    def sendKeys(self,text,locatorType,locator):

        self.getElement(locatorType, locator).send_keys(text)
        print("send the value " + text + " to the  element at " + locatorType + " and by the locator " + locator)







    # This function is to find out weather the elment is present

    def isElementPresnt(self,locatorType,locator):
        
        totalElement = self.getElements(locatorType, locator)

        if len(totalElement) != 0:
            isPresent = True
            print("The asked element is present")

        else:
            isPresent = False
            print("The asked element is present")

        return isPresent




