from Driver.web_control import WebControl

class GoogleAccount:
    def __init__(self, driver: WebControl):
        self.wc =  driver
    @property
    def TurnToSignInBtn(self): return self.wc.get_element("//a[@data-label='header'][text()='Sign in']")
    @property
    def SignInEmail(self): return self.wc.get_element("//input[@type='email']")
    @property
    def NextStepBtn(self): return self.wc.get_element("//button//span[text()='下一步']")
    @property
    def SignInPassword(self): return self.wc.get_element("//input[@type='password']")

class GMail:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def MoreBtn(self): return self.wc.get_elements("//span[@role='button'][@gh='mll']")[0]
    @property
    def SpamBox(self): return self.wc.get_element("//div[@class='aim']//div[@data-tooltip='垃圾郵件']//a")
    @property
    def SpamMail(self): return self.wc.get_elements("//div[@style][@role='main']//tbody//tr//td//span[text()='myViewBoard Account Deletion You have received this email in response to the request made for the deletion of your myViewBoard account. Please click the following button to complete the Account']")[0]
    @property
    def NoProblemBtn(self): return self.wc.get_elements("//button[text()='看起來沒有問題']")[-1]
    @property
    def NoSpamBtn(self): return self.wc.get_element("//div[@gh='mtb']//div[@role='button']//div[text()='非垃圾郵件']")
    @property
    def ReceiveBox(self): return self.wc.get_element("//div[@data-tooltip='收件匣']")
    @property
    def TargetMail(self): return self.wc.get_elements("//div//tbody//tr[@draggable='false']")[0]
    @property
    def DeleteAccBtn(self): return self.wc.get_element("//tr//td[@align='center']/a[@href]")

class GoogleElements:
    def __init__(self, driver: WebControl):
        self.G_Account = GoogleAccount(driver)
        self.Gmail = GMail(driver)