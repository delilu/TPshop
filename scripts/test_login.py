import allure
import pytest

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @allure.step(title="测试登录")
    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        expect = args["expect"]
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()
        assert self.page.login.is_toast_exist(expect)

    @allure.step(title="登录中用户名或密码为空")
    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_part"))
    def test_login_part(self, args):
        username = args["username"]
        pwd = args["password"]
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username(username)
        self.page.login.input_password(pwd)
        assert not self.page.login.login_btn_is_enabled()
