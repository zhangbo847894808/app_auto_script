from desired_caps.setup import setup
import time
import os


driver = setup()
driver.get_screenshot_as_file(os.getcwd() + os.sep + './screen.png')