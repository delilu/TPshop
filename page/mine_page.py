from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_sign_up_btn = By.ID, "com.tpshop.malls:id/nickname_txtv"

    def click_login_sign_up(self):
        self.click(self.login_sign_up_btn)
