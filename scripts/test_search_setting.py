import os
import sys
import pytest
import allure
import allure_pytest

sys.path.append(os.getcwd())

from Base.read_data import Read_data
from Base.initdriver import init_driver
from Page.search_setting import SearchSetting
from Base.generate_report import generate_report


def get_yaml_data():
    search_test_data_obj = Read_data('search_data')
    search_yaml_data = search_test_data_obj.load_data()
    input_text_list = list()
    # search_yaml_data_inner1 = {'search_test_001':{'input_text':"你好"}, 'search_test_001':{'input_text':"1234"}}
    search_yaml_data_inner1 = search_yaml_data.get("yaml_data")
    for i in search_yaml_data_inner1.keys():
        input_text_list.append((i, search_yaml_data_inner1.get(i).get("input_text")))

    return input_text_list


class Test_Search_Setting:
    def setup_class(self):
        self.driver = init_driver()
        self.search_obj = SearchSetting(self.driver)

    def teardown_class(self):
        self.driver.quit()
        generate_report()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('test_num, text_input', get_yaml_data())
    @allure.step(title="搜索框输入")
    def test_002(self, test_num, text_input):
        self.search_obj.inputtext(text_input)
        print("用例编号:%s" % test_num)
        self.driver.get_screenshot_as_file('./images/search_setting_img_%s.png' % text_input)


    @pytest.mark.run(order=1)
    @allure.step(title="点击搜索框")
    def test_001(self):
        self.search_obj.click_search()



