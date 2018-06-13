'''
This class is for the storing the pages of
the login page
'''

from base.selenium_driver import SeleniumDriver
import time
class LoginPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    '''
    bellow will store the pages 
    '''
    _login_link_xapth="//a[contains(text(),'Login')]"
    _email_field_id="user_email"
    _password_filed_id="user_password"
    # here i changes the name of commit to commi
    _login_button_name="commit"


    def loginToLetsKode(self,usrename,password):
        self.clickOnElement("xpath",self._login_link_xapth)
        time.sleep(2)
        self.sendKeys(usrename,"id",self._email_field_id)
        self.sendKeys(password,"id",self._password_filed_id)
        self.clickOnElement("name",self._login_button_name)