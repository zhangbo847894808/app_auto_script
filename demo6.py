from desired_caps.setup import setup
import time


driver = setup()
search = driver.find_element_by_id('com.android.settings:id/search')
driver.swipe(148,1100,148,452,3000)
driver.background_app(5)