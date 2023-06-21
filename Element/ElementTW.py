from Driver.web_control import WebControl

class TWAccount:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def HomeSignBtn(self): return self.wc.get_element("//button[@data-testid='button']")
    @property
    def AccField(self): return self.wc.get_element("//input[@name='login']")
    @property
    def SignInBtn(self): return self.wc.get_element("//button[@type='button'][@data-i18n='SIGNIN']")
    @property
    def PwdField(self): return self.wc.get_element("//input[@name='password']")
    @property
    def SubmitBtn(self): return self.wc.get_element("//button[@type='submit'][@data-i18n='SIGNIN']")

class TWDashboard:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def CreateBoardTab(self): return self.wc.get_element("//div[@data-testid='create-borad-button']")
    @property
    def DropDownBtn(self): return self.wc.get_elements("//div[@data-testid='dropdown']")
    @property
    def DeleteBtn(self): return self.wc.get_elements("//li[@data-testid='dropdown-option']")[3]
    @property
    def ConfirmDelBtn(self): return self.wc.get_element("//button[@data-testid='button']/div[@data-testid='button-content']//span[text()='Delete']")

class TWBoard:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def Canvas(self): return self.wc.get_element("//div[@class='touch-none']/canvas")
    @property
    def PenBtn(self): return self.wc.get_elements("//button[@role='button']")[3]
    @property
    def ShareBtn(self): return self.wc.get_element("//button[text()='Share']")
    @property
    def SettingBtn(self): return self.wc.get_element("//div[@class='h-12 w-12']//button")
    @property
    def DeleteBtn(self): return self.wc.get_element("//ul/li/span[text()='Delete']")
    @property
    def ConfirmDelBtn(self): return self.wc.get_element("//button[@data-testid='button']//div[@data-testid='button-content']/span[@data-testid='confirm-modal-ok']")
    @property
    def PinMapBtn(self): return self.wc.get_element("//button[@aria-label='pinMap']")

class TWElements:
    def __init__(self, driver: WebControl):
        self.wc = driver
        self.Account = TWAccount(driver)
        self.Dashboard = TWDashboard(driver)
        self.Board = TWBoard(driver)
