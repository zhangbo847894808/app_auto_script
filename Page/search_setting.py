import pytest
from selenium.webdriver.common.by import By
from Base.Base import Base
import Page


class SearchSetting(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search(self):
        # 点击搜索框
        self.click_element(Page.search_button)

    def inputtext(self, text):
        # 输入文本
        self.input_text(Page.search_text, text)




