from Driver.web_control import WebControl

class MVBcomAccount:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def AccField(self): return self.wc.get_element("//input[@name='login']")
    @property
    def SignInBtn(self): return self.wc.get_element("//button[@type='button'][@data-i18n='SIGNIN']")
    @property
    def PwdField(self): return self.wc.get_element("//input[@name='password']")
    @property
    def SubmitBtn(self): return self.wc.get_element("//button[@type='submit'][@data-i18n='SIGNIN']")
    @property
    def GoogleSSOBtn(self): return self.wc.get_element("//form[@id='google']//button[@type='submit']")
    @property
    def SignUpBtn(self): return self.wc.get_element("//a[@data-i18n='SIGNUP']")
    # @property
    # def SignUpFirstName(self): return self.wc.get_element("//input[@placeholder='First Name']")
    # @property
    # def SignUpLastName(self): return self.wc.get_element("//input[@placeholder='Last Name']")
    @property
    def GoogleSignUp(self): return self.wc.get_element("//button[@ng-reflect-ng-class='icon-google']")
    @property
    def SignUpCheckbox(self): return self.wc.get_element("//mat-checkbox[@aria-labelledby='agreement']//div[@class='mat-checkbox-inner-container']")

class MVBcomMessage:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def AccDelMessage(self): 
        self.wc.element_wait("//mvb-message//div//p[@aria-label='感謝您願意使用 myViewBoard！若有任何想法或意見，都歡迎聯繫我們。']", 10)
        return self.wc.get_element("//mvb-message//div//p[@aria-label='感謝您願意使用 myViewBoard！若有任何想法或意見，都歡迎聯繫我們。']")


class MVBcomFirstUsage:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def AgreeCheckbox(self): return self.wc.get_element("//p-checkbox//div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default']")
    # @property
    # def AgreeCheckbox(self): return self.wc.get_element("//p-checkbox[@ng-reflect-disabled='false']")
    @property
    def AgreeConfirmBtn(self): return self.wc.get_element("//button[@mat-raised-button]")
    @property
    def SkipBtn(self): return self.wc.get_element("//button[@mat-button]")
    @property
    def RoleBtn(self) : return self.wc.get_elements("//button[@class='content__flex__item']")
    @property
    def CloseBtn(self): return self.wc.get_element("//div[@class='close']//button")

class MVBcomSetting:
    def __init__(self, driver: WebControl):
        self.wc = driver
    @property
    def Avatar(self): return self.wc.get_element("//a[@class='dropdown-toggle']")
    @property
    def AccountEdit(self): return self.wc.get_element("//a[@ng-reflect-router-link='/account/edit']")
    @property
    def AccountDelBtn(self): return self.wc.get_element("//button[@ng-reflect-translate='Account.Delete_Button']")
    @property
    def ConfirmDelBtn(self): return self.wc.get_element("//button[text()='繼續']")
    @property
    def DelMainConfirmBtn(self): return self.wc.get_element("//div[@style='overflow-y: auto;']//button[text()='確認']")
    
class MVBcomElements:
    def __init__(self, driver: WebControl):
        self.M_Account = MVBcomAccount(driver)
        self.M_Message = MVBcomMessage(driver)
        self.FirstUse = MVBcomFirstUsage(driver)
        self.Setting = MVBcomSetting(driver)