from desired_caps.setup import setup
import time

driver = setup()
ele_list = driver.find_elements_by_id('com.android.settings:id/title')
for i in ele_list:
    if i.text == 'WLAN':
        i.click()
