from Driver.web_control import WebControl
from Element.LibElements import AllElements

class StepAccount:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.Account
    def Go_SignInPage(self):
        self.wc.maximize_window()
        self.wc.enter_target_page("https://stage.myviewboard.com/teamwork")
        self.wc.element_click(self.ele.HomeSignBtn)
    def KeyIn_Account(self, acc):
        self.wc.element_send_keys(self.ele.AccField, acc)
    def Click_LoginBtn(self):
        self.wc.element_click(self.ele.SignInBtn)
    def KeyIn_Password(self, pwd):
        self.wc.element_send_keys(self.ele.PwdField, pwd)
    def Click_SubmitBtn(self):
        self.wc.element_click(self.ele.SubmitBtn)

class StepDashboard:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.Dashboard
    def Create_Board(self):
        self.wc.element_click(self.ele.CreateBoardTab)
    def Delete_Board(self):
        self.wc.all_page_wait()
        self.wc.element_click(self.ele.DropDownBtn[0])
        self.wc.element_click(self.ele.DeleteBtn)
        self.wc.element_click(self.ele.ConfirmDelBtn)

class StepCanvas:
    def __init__(self, driver: WebControl, element: AllElements):
        self.wc = driver
        self.ele = element.Board
    def Click_PenIcon(self):
        self.wc.element_wait("//button[text()='Share']", 30)
        self.wc.element_click(self.ele.PenBtn)
    def Open_PinMap(self):
        self.wc.element_click(self.ele.PinMapBtn)
    def DragOn_Canvas(self, putPos: list):
        self.wc.DragTo(self.ele.Canvas, putPos)
    def ScreenShot_Canvas(self):
        self.wc.screenshot(self.ele.Canvas)
    def DeleteBoard(self):
        self.wc.element_click(self.ele.SettingBtn)
        self.wc.element_click(self.ele.DeleteBtn)
        self.wc.element_click(self.ele.ConfirmDelBtn)
        self.wc.element_wait("//div[@data-testid='create-borad-button']", 30)


class TWSteps:
    def __init__(self, driver: WebControl, element: AllElements):
        self.Account = StepAccount(driver, element)
        self.Dashboard = StepDashboard(driver, element)
        self.Canvas = StepCanvas(driver , element)
        