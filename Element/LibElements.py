from Element.ElementGoogle import GoogleElements
from Element.ElementMVBcom import MVBcomElements
from Element.ElementTW import TWElements
from Driver.web_control import WebControl

class AllElements:
    def __init__(self, driver: WebControl):
        self.wc = driver
        self.G_Account = GoogleElements(driver).G_Account
        self.Gmail = GoogleElements(driver).Gmail
        self.M_Account = MVBcomElements(driver).M_Account
        self.M_Message = MVBcomElements(driver).M_Message
        self.FirstUse = MVBcomElements(driver).FirstUse
        self.Setting = MVBcomElements(driver).Setting
        self.Account = TWElements(driver).Account
        self.Dashboard = TWElements(driver).Dashboard
        self.Board = TWElements(driver).Board