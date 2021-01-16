from appium.webdriver.common.touch_action import TouchAction
from desired_caps.setup import setup
import time


driver = setup()
TouchAction(driver).press(x=316, y=1700).wait(5000).move_to(x=316, y=524).release().perform()
el_anquan = driver.find_element_by_xpath("//*[contains(@text, '安全')]")
el_anquan.click()
el_screen_lock = driver.find_element_by_xpath("//*[contains(@text, '屏幕锁定方式')]")
el_screen_lock.click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
time.sleep(1)
# 3.(542,997)  898,997
for i in range(2):
    TouchAction(driver).press(x=179, y=640).wait(500).move_to(x=361, y=0)\
        .wait(500).move_to(x=0, y=357).wait(500).move_to(x=361,y=0).release().perform()
    driver.find_element_by_id('com.android.settings:id/footerRightButton').click()
driver.find_element_by_id('com.android.settings:id/next_button').click()
time.sleep(2)
driver.quit()
