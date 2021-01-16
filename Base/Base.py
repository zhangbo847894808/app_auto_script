from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10):
        # 封装称为智能等待方法
        # loc:类型为元祖,格式(By.ID,value),(By.CLASS_NAME,value),(By.XPATH,value)
        # timeout:搜索超时时间
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # 封装点击操作
        self.find_element(loc).click()

    def input_text(self, loc, text):
        # 封装输入操作
        self.fm = self.find_element(loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        self.fm.send_keys(text)
