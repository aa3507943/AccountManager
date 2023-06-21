from Driver.web_control import WebControl
from Element.LibElements import *
import time

class StepSignUp:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.M_Account
    def Go_SignInPage(self):
        self.wc.maximize_window()
        self.wc.enter_target_page("https://stage.myviewboard.com/signin")
        cookies = {
    'name': 'myLang',
    'value': 'zh-TW',
    'path': '/',
    'domain': '.stage.myviewboard.com'
}
        self.wc.add_cookies(cookies)
    def Click_SignUp(self):
        self.wc.element_click(self.ele.SignUpBtn)
        time.sleep(1)
    def Click_GoogleSignUp(self):
        self.wc.element_click(self.ele.GoogleSignUp)
        time.sleep(1)

class StepGoogleSSOSignIn:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.M_Account
    def Go_SignInPage(self):
        self.wc.maximize_window()
        self.wc.enter_target_page("https://stage.myviewboard.com/signin")
    def Click_GoogleSSO(self):
        self.wc.element_click(self.ele.GoogleSSOBtn)
        time.sleep(1)

class StepCheckDelSuccess:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.M_Message
    def Check_SuccessMsg(self):
        self.wc.switch_window(-1)
        if self.ele.AccDelMessage:
                print("刪除帳號成功")
        else:
            print("刪除帳號失敗")
        self.wc.close_webpage()
        time.sleep(1)

class FirstUseSet:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.FirstUse
    def Click_AgreeCheckbox(self):
        time.sleep(5)
        self.wc.element_click(self.ele.AgreeCheckbox)
        time.sleep(1)
    def Click_AgreeConfirmBtn(self):
        self.wc.element_click(self.ele.AgreeConfirmBtn)
        time.sleep(1)
    def Click_SkipBtn(self):
        self.wc.element_click(self.ele.SkipBtn)
        time.sleep(1)
    def Click_RoleBtn(self):
        self.wc.element_click(self.ele.RoleBtn[3])
        time.sleep(1)
    def Click_CloseBtn(self):
        self.wc.element_click(self.ele.CloseBtn)
        time.sleep(1)
        self.wc.close_webpage()
        time.sleep(1)
        print("帳號創建成功")

class AccountManage:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.Setting
    def Open_Avatar(self):
        self.wc.element_click(self.ele.Avatar)
        time.sleep(1)
    def Enter_AccountEditPage(self):
        self.wc.element_click(self.ele.AccountEdit)
        time.sleep(1)
    def Del_Account(self):
        self.wc.element_click(self.ele.AccountDelBtn)
        time.sleep(1)
        self.wc.element_click(self.ele.ConfirmDelBtn)
        time.sleep(1)
        self.wc.element_click(self.ele.DelMainConfirmBtn)
        time.sleep(1)
        

class StepMVBcom:
    def __init__(self, driver: WebControl, element: AllElements):
        self.M_SignUp = StepSignUp(driver, element)
        self.M_DelSuccess = StepCheckDelSuccess(driver, element)
        self.FirstUse = FirstUseSet(driver, element)
        self.G_SSO_SignIn = StepGoogleSSOSignIn(driver, element)
        self.AccManage = AccountManage(driver, element)
