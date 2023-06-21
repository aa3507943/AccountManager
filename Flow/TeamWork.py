from Element.ElementTW import *
from Step.StepTW import *
import json

class FlowTWSignIn:
    def __init__(self, step: StepAccount):
        self.Step = step
        with open("./User_Data/userInfo.json", "r", encoding= "utf-8") as f:
            data = json.load(f)
            self.acc = data['account']
            self.pwd = data['password']
    def SignIn_TeamWork(self):
        self.Step.Go_SignInPage()
        self.Step.KeyIn_Account(self.acc)
        self.Step.Click_LoginBtn()
        self.Step.KeyIn_Password(self.pwd)
        self.Step.Click_SubmitBtn()

class FlowTWDashboard:
    def __init__(self, step: StepDashboard):
        self.Step = step
    def Create_NewBoard(self):
        self.Step.Create_Board()

class FlowTWBoard:
    def __init__(self, step: StepCanvas):
        self.Step = step
    def Draw_Canvas(self):
        self.Step.Click_PenIcon()
        putPos = [[500, 300], [500, 600], [700, 600], [700, 300], [500, 300]]
        self.Step.DragOn_Canvas(putPos)
    def PinMap(self):
        self.Step.Open_PinMap()
    def ScreenShot_Canvas(self):
        self.Step.ScreenShot_Canvas()
        self.Step.DeleteBoard()
        