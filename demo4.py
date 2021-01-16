from desired_caps.setup import setup
import time

driver = setup()
ele_list = driver.find_elements_by_xpath("//*[contains(@class, 'android.widget.TextView')]")
ele_list[4].click()

