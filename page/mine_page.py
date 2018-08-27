import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_sign_up_btn = By.ID, "com.tpshop.malls:id/nickname_txtv"
    setting_btn = By.ID, "com.tpshop.malls:id/setting_btn"
    # 点击设置后出现的标题文字按钮
    title_text_view = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    @allure.step(title="点击‘登录/注册’")
    def click_login_sign_up(self):
        self.click(self.login_sign_up_btn)

    @allure.step(title="点击设置图像按钮")
    def click_setting(self):
        self.click(self.setting_btn)

    @allure.step(title="判断是否登录状态")
    def is_login(self):
        self.click_setting()
        is_login = not self.find_element(self.title_text_view).text == "登录"
        self.press_back()
        return is_login
