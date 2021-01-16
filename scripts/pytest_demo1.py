import pytest
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


class Test_ST:
    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:5555 devices'
        # app信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = 'com.android.settings.Settings'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def teardown_class(self):
        print(">>>>teardown")

    @pytest.mark.run(order=2)
    def test_001(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '显示')]").click()
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, 'daf')]")).click()

        self.driver.find_element_by_xpath("//*[contains(@text, '字体大小')]").click()
        time.sleep(1)
        self.driver.find_elements_by_id("android:id/text1")[0].click()
        summary_list = self.driver.find_elements_by_id("android:id/summary")
        summary_text_list = list()
        for i in summary_list:
            summary_text_list.append(i.text)
        assert "小" in summary_text_list, "失败了~"

    @pytest.mark.run(order=1)
    def test_002(self):
        print(">>>>test_002")
