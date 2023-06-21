from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.webelement import WebElement

class WebControl: #python v3.11.x selenium 4.8.x
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        
    """呼叫此函式需可最大化當前控制的瀏覽器"""
    def maximize_window(self):
        self.driver.maximize_window()
        
    """呼叫此函式需可最小化當前控制的瀏覽器"""
    def minimize_window(self):
        self.driver.minimize_window()

    """呼叫此函式可以將視窗移到所需的位置"""
    def move_window(self, x, y):
        self.driver.set_window_position(x, y)

    """呼叫此函式並於參數位置放入URL，連結至目標網頁"""
    def enter_target_page(self, url):
        self.driver.get(url)
        self.all_page_wait()
    
    """呼叫此函式可以關閉當前控制的瀏覽器"""
    def close_webpage(self):
        self.driver.quit()
    
    """呼叫此函式需可重整當前控制的瀏覽器"""
    def reload_webpage(self):
        self.driver.refresh()
        self.all_page_wait()
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件"""
    def get_element(self, element):
        try:
            self.element_wait(element, 15)
            return self.driver.find_element(By.XPATH, element)
        except:
            # ExceptionHandler(msg= "Cannot get the target element. 無法獲取目標元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件列表，並給定另一參數指定要從
    列表中取第幾個index的元件"""
    def get_elements(self, element):
        try:
            self.elements_wait(element, 15)
            return self.driver.find_elements(By.XPATH, element)
        except:
            # ExceptionHandler(msg= "Cannot get the target element. 無法獲取目標元件。\n", exceptionLevel= "error")
            raise
    
    def add_cookies(self, cookies:dict):
        self.driver.add_cookie(cookies)
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做點擊的動作"""
    def element_click(self, getElement: get_element or get_elements):
        try:
            getElement.click()
        except:
            # ExceptionHandler(msg= "Cannot click the element. 無法點擊該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做輸入的動作，並給定另一參數指定可以輸入什麼"""
    def element_send_keys(self, getElement: get_element or get_elements, content):
        try:
            getElement.send_keys(content)
        except:
            # ExceptionHandler(msg= "Cannot send the target key to the element. 無法傳送目標值至該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入欲定位的元件要等待多久時間載入"""
    def element_wait(self, element, time: int):
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, element))) 
        except:
            # logging.error(msg= "Time Out! Cannot locate the eleement. 時間到！無法定位到該元件。\n", exc_info= True)
            # ExceptionHandler(msg= "Time Out! Cannot locate the element. 時間到！無法定位到該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入欲定位的元件列表要等待多久時間載入"""
    def elements_wait(self, elements, time: int):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, elements))) 
        except:
            # ExceptionHandler(msg= "Time Out! Cannot locate the element. 時間到！無法定位到該元件。\n", exceptionLevel= "error")
            raise
        
    """等待整個頁面載入完畢"""
    def all_page_wait(self): 
        self.driver.implicitly_wait(30)


    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    """控制警告視窗"""
    def switch_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


    def DragTo(self, target:WebElement, putPos: list): # [[500, 300], [500, 600], [700, 600], [700, 300], [500, 300]]
        startX, startY = target.location['x'], target.location['y']
        midX, midY = startX + target.size['width']//2, startY + target.size['height']//2
        self.actions.move_to_element(target)
        for i in range(len(putPos)):
            if i == 0:
                self.actions.move_by_offset(putPos[i][0] - midX, putPos[i][1] - midY)
                self.actions.click_and_hold()
            else:
                self.actions.move_by_offset(putPos[i][0] - tmpX, putPos[i][1] - tmpY)
            tmpX = putPos[i][0]
            tmpY = putPos[i][1]
            
        self.actions.release().perform()
    
    def screenshot(self, target: WebElement):
        target.screenshot("canvas.png")