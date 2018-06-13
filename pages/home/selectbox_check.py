from base.selenium_driver import SeleniumDriver
from commonutilities.select_functions import SelectFunction
import time


class SelectBoxCheking(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver



    _selct_car_id="carselect"

    def testSelectBox(self):
        sel = SelectFunction(self.driver)
        sel.selectByIndex("id",self._selct_car_id,1)






