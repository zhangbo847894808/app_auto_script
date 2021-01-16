from appium.webdriver.common.touch_action import TouchAction

from desired_caps.setup import setup
import time


driver = setup()
for i in range(5):
    driver.keyevent(25)
    time.sleep(1)
driver.quit()