from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_btn = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_btn = By.ID, "com.tpshop.malls:id/edit_password"
    login_btn = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username_btn, text)

    def input_password(self, text):
        self.input(self.password_btn, text)

    def click_login(self):
        self.click(self.login_btn)
