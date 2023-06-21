from Driver.web_control import WebControl
from Element.LibElements import AllElements
import time

class StepSignInGoogle:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.G_Account
    def Enter_SignInPage(self):
        self.wc.enter_target_page("https://www.google.com/intl/zh-TW/gmail/about/")
        self.wc.element_click(self.ele.TurnToSignInBtn)
    def KeyIn_Account(self, acc):
        self.wc.element_send_keys(self.ele.SignInEmail, acc)
    def KeyIn_Password(self, pwd):
        self.wc.element_send_keys(self.ele.SignInPassword, pwd)
    def Click_NextBtn(self):
        self.wc.element_click(self.ele.NextStepBtn)
class StepSpamToReceive:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.Gmail
    def Goto_Gmail(self):
        self.wc.enter_target_page("https://mail.google.com")
    def TurnTo_SpamBox(self):
        self.wc.element_click(self.ele.MoreBtn)
        time.sleep(1)
        self.wc.element_click(self.ele.SpamBox)
        time.sleep(1)
    def Enter_SpamMail(self):
        self.wc.element_click(self.ele.SpamMail)
        time.sleep(1)
    def Change_SpamToNormal(self):
        self.wc.element_click(self.ele.NoProblemBtn)
        self.wc.element_click(self.ele.NoSpamBtn)
        time.sleep(1)
    def TurnTo_ReceiveBox(self):
        self.wc.element_click(self.ele.ReceiveBox)
        time.sleep(1)
    def Enter_TargetMail(self):
        self.wc.element_click(self.ele.TargetMail)
        time.sleep(1)
    def Confirm_DelAcc(self):
        self.wc.element_click(self.ele.DeleteAccBtn)
        time.sleep(1)

class StepGoogle:
    def __init__(self, driver: WebControl, element: AllElements):
        self.G_SignIn = StepSignInGoogle(driver, element)
        self.G_AccDel = StepSpamToReceive(driver, element)