from selenium.webdriver.common.by import By

# 搜索按钮
search_button = (By.ID, "com.android.settings:id/search")
# 搜索输入框
search_text = (By.ID, "android:id/search_src_text")
# 搜索框返回按钮
search_return_button = (By.CLASS_NAME, "android.widget.ImageButton")