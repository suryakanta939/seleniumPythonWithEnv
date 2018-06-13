
class HandelWindow():

    def __init__(self,driver):
        self.driver=driver


    def switchingToWindoByNo(self, window_no):

        handels=self.driver.window_handles
        print("the total no of window is "+str(len(handels)))
        for handel in range(0,len(handels)):
            if handel==window_no-1:
                self.driver.switch_to.window(handels[handel])
                print("switch to the "+str(window_no)+" successfully")

    def switchingToWindowByTitle(self,windowTitle):
        parent_id = self.driver.current_window_handle
        handels = self.driver.window_handles

        for handel in handels:
            if handel is not parent_id:
                title=self.driver.title

                if title is windowTitle :
                    self.driver.switch_to.window(handel)