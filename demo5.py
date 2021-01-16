from desired_caps.setup import setup
import time


driver = setup()
search = driver.find_element_by_id('com.android.settings:id/search')
search.click()
print(search.location)
print(driver.current_activity, driver.current_package)
search.send_keys('张博')
search.clear()
time.sleep(2)
search.send_keys('abc')
search.clear()
time.sleep(2)



driver.quit()