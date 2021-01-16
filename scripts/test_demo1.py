import pytest

from appium import webdriver

# 函数级别setup()／teardown() 运行一次测试函数会运行一次setup和teardown
from selenium.webdriver.support.wait import WebDriverWait


class Test_ST:

    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    def teardown_class(self):
        self.driver.quit()

    # def wait_ele(self,xpathx):
    #
    #     return WebDriverWait(self.driver,5,0.5).until(lambda x: x.find_element_by_xpath(xpathx))

    def test_002(self):
        # 设置
        # 点击更多
        G_D=WebDriverWait(self.driver,5,0.5).\
            until(lambda x: x.find_element_by_xpath("//*[contains(@text,'更多')]"))
        G_D.click()
        # 点击移动网络
        Y_D = WebDriverWait(self.driver, 5, 0.5).\
            until(lambda x: x.find_element_by_xpath("//*[contains(@text,'移动')]"))
        Y_D.click()
        # 首选网络类型
        S_X = WebDriverWait(self.driver, 5, 0.5).\
            until(lambda x: x.find_element_by_xpath("//*[contains(@text,'首选网络')]"))
        S_X.click()
        # 弹窗点击3G
        G_3 = WebDriverWait(self.driver, 5, 0.5).\
            until(lambda x: x.find_element_by_xpath("//*[contains(@text,'3G')]"))
        G_3.click()
        # 获取所有描述信息
        sum_list = self.driver.find_elements_by_id("android:id/summary")
        text_list = []
        for i in sum_list:
            text_list.append(i.text)

        assert "2G" in text_list, "失败了～"
