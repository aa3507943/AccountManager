from Step.LibSteps import AllSteps
import json 

class FlowGoToGmail:
    def __init__(self, step: AllSteps):
        self.Step = step.G_Step
    def GoToGmail(self):
        self.Step.G_AccDel.Goto_Gmail()

class FlowSignInGoogle:
    def __init__(self, step: AllSteps):
        self.Step = step.G_Step.G_SignIn
        with open("./User_Data/userInfo.json", "r", encoding= "utf-8") as f:
            data = json.load(f)
            self.acc = data['G_account']
            self.pwd = data['G_password']
    def SignInGoogle(self):
        self.Step.Enter_SignInPage()
        self.Step.KeyIn_Account(self.acc)
        self.Step.Click_NextBtn()
        self.Step.KeyIn_Password(self.pwd)
        self.Step.Click_NextBtn()

class FlowSignInByGoogle:
    def __init__(self, step: AllSteps):
        self.Step = step.G_Step.G_SignIn
        with open("./User_Data/userInfo.json", "r", encoding= "utf-8") as f:
            data = json.load(f)
            self.acc = data['G_account']
            self.pwd = data['G_password']
    def SignInGoogle(self):
        self.Step.KeyIn_Account(self.acc)
        self.Step.Click_NextBtn()
        self.Step.KeyIn_Password(self.pwd)
        self.Step.Click_NextBtn()

class FlowGetMailToDelAcc:
    def __init__(self, step: AllSteps):
        self.Step = step.G_Step.G_AccDel
    def MailHandle(self):
        self.Step.TurnTo_SpamBox()
        self.Step.Enter_SpamMail()
        self.Step.Change_SpamToNormal()
        self.Step.TurnTo_ReceiveBox()
        self.Step.Enter_TargetMail()
        self.Step.Confirm_DelAcc()
    