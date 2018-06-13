
class HandelAlert():

    def __init__(self,driver):
        self.driver=driver

    def accept_alert(self):
        alt=self.driver.switch_to.alert
        alt.accept()

    def cancel_alert(self):
        alt = self.driver.switch_to.alert
        alt.dismiss()

    def read_alert_text(self):
        alt = self.driver.switch_to.alert
        message=alt.text
        return message
