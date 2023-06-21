from Step.LibSteps import AllSteps
import json, time

class FlowSignUpMVB:
    def __init__(self, step: AllSteps):
        self.Step = step.MVB_Step.M_SignUp
        with open("./User_Data/userInfo.json", "r", encoding= "utf-8") as f:
            data = json.load(f)
            self.acc = data['G_account']
            self.pwd = data['G_password']
    def TurnTo_SignUpPage(self):
        self.Step.Go_SignInPage()
        self.Step.Click_SignUp()
        self.Step.Click_GoogleSignUp()

class FlowGoogleSSOSignIn:
    def __init__(self, step: AllSteps):
        self.Step = step.MVB_Step.G_SSO_SignIn
        with open("./User_Data/userInfo.json", "r", encoding= "utf-8") as f:
            data = json.load(f)
            self.acc = data['G_account']
            self.pwd = data['G_password']
    def TurnTo_Google_SignInPage(self):
        self.Step.Go_SignInPage()
        self.Step.Click_GoogleSSO()

class FlowDeleteAccount:
    def __init__(self, step: AllSteps):
        self.Step = step.MVB_Step.AccManage
    def Delete_Account(self):
        self.Step.Open_Avatar()
        self.Step.Enter_AccountEditPage()
        self.Step.Del_Account()

class FlowCheckSuccessMsg:
    def __init__(self, step: AllSteps):
        self.Step = step.MVB_Step.M_DelSuccess
    def Check_Success(self):
        self.Step.Check_SuccessMsg()

class FlowFirstUse:
    def __init__(self, step: AllSteps):
        self.Step = step.MVB_Step.FirstUse
    def FirstSetting(self):
        self.Step.Click_AgreeCheckbox()
        self.Step.Click_AgreeConfirmBtn()
        self.Step.Click_SkipBtn()
        self.Step.Click_RoleBtn()
        self.Step.Click_CloseBtn()
        
