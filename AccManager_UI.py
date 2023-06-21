import tkinter as tk
from tkinter import ttk
from Driver.web_control import WebControl
from Driver.create_driver import CreateDriver
from Flow.TeamWork import *
from Step.LibSteps import AllSteps
from Flow.MVBcom import *
from Flow.Google import *
from Element.LibElements import AllElements
import time
import pyautogui

width, height = pyautogui.size()

class MVBTest:
    # def __init__(self):
    #     self.driver = CreateDriver().Driver
    #     self.wc = WebControl(self.driver)
    #     self.ele = AllElements(self.wc)
    #     self.Step = AllSteps(self.wc, self.ele)
    def SignUp_Flow(self):
        self.driver = CreateDriver().Driver
        self.wc = WebControl(self.driver)
        self.ele = AllElements(self.wc)
        self.Step = AllSteps(self.wc, self.ele)
        FlowSignUpMVB(self.Step).TurnTo_SignUpPage()
        FlowSignInByGoogle(self.Step).SignInGoogle()
        FlowFirstUse(self.Step).FirstSetting()
    def Delete_Account(self):
        self.driver = CreateDriver().Driver
        self.wc = WebControl(self.driver)
        self.ele = AllElements(self.wc)
        self.Step = AllSteps(self.wc, self.ele)
        FlowGoogleSSOSignIn(self.Step).TurnTo_Google_SignInPage()
        FlowSignInByGoogle(self.Step).SignInGoogle()
        FlowDeleteAccount(self.Step).Delete_Account()
        FlowGoToGmail(self.Step).GoToGmail()
        FlowGetMailToDelAcc(self.Step).MailHandle()
        FlowCheckSuccessMsg(self.Step).Check_Success()

class AccManager:
    def __init__(self):
        self.initialize()
        self.set_createBtn()
        self.set_deleteBtn()
        self.master.mainloop()
    def initialize(self):
        self.master = tk.Tk()
        self.master.title("MVB帳號管理")
        self.master.geometry(f'450x200+{width//3}+{height//3}')
        self.master.resizable(False, False)
    
    def set_createBtn(self):
        self.createBtn = tk.Button(self.master, text= "創建GoogleSSO帳號", font=("Arial", 20), command= MVBTest().SignUp_Flow)
        self.createBtn.config(width = '18', height= '2')
        # self.createBtn.grid(row= 0, column= 1)
        self.createBtn.pack(side= 'top', pady= 5)

    def set_deleteBtn(self):
        self.deleteBtn = tk.Button(self.master, text= "刪除GoogleSSO帳號", font=("Arial", 20), command= MVBTest().Delete_Account)
        self.deleteBtn.config(width = '18', height= '2')
        self.deleteBtn.pack(side= 'top', pady= 5)

