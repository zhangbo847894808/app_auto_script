from appium.webdriver.common.touch_action import TouchAction

from desired_caps.setup import setup
import time


driver = setup()
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).tap(el).perform()
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
TouchAction(driver).tap(x=317,y=504).perform()