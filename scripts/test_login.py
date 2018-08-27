import random
import time

import allure
import pytest
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


def random_password():
    password = ""
    for i in range(6):
        password += str(random.randint(0, 9))
    return password


def show_password_data():
    temp_list = list()
    for i in range(2):
        temp_list.append(random_password())
    return temp_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @allure.step(title="测试登录")
    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_sign_up()
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login()
    #     assert self.page.login.is_toast_exist(expect)
    #
    # @allure.step(title="登录中用户名或密码为空")
    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_part"))
    # def test_login_part(self, args):
    #     username = args["username"]
    #     pwd = args["password"]
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_sign_up()
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(pwd)
    #     assert not self.page.login.login_btn_is_enabled()
    #
    # @allure.step(title="密码是否可显示隐藏")
    # @pytest.mark.parametrize("pwd", show_password_data())
    # def test_show_password(self, pwd):
    #     pwd_location = (By.XPATH, "//*[@text='%s']" % pwd)
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_sign_up()
    #     self.page.login.input_password(pwd)
    #     # 在点击显示密码按钮之前，是要找不到输入的密码
    #     assert not self.page.login.is_location_exist(pwd_location)
    #     self.page.login.click_view_pwd()
    #     time.sleep(3)
    #     # 显示密码时截图
    #     allure.attach("显示密码:", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
    #     assert self.page.login.is_location_exist(pwd_location)
    # 验证登录状态的方法是否添加成功
    def test_hello(self):
        self.page.home.click_mine()
        res = self.page.mine.is_login()
        print(res)