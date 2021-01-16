from desired_caps.setup import setup
import time

driver = setup()
driver.find_element_by_id('com.android.settings:id/search').click()
time.sleep(2)

driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)
driver.quit()