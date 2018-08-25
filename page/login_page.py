import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_btn = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_btn = By.ID, "com.tpshop.malls:id/edit_password"
    login_btn = By.ID, "com.tpshop.malls:id/btn_login"
    # 显示密码的小眼睛按钮
    view_pwd_btn = By.ID,"com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach("用户名：", text)
        self.input(self.username_btn, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach("密码：", text)
        self.input(self.password_btn, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_btn)

    @allure.step(title="登录按钮是否可用")
    def login_btn_is_enabled(self):
        return self.is_location_enabled(self.login_btn)

    @allure.step(title="点击显示密码按钮")
    def click_view_pwd(self):
        self.click(self.view_pwd_btn)