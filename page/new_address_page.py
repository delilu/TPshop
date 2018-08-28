import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewAddressPage(BaseAction):
    # 收货人
    name_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"
    # 手机号码
    mobile_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"
    # 详细地址
    address_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"
    # 所在地区
    region_text_view = By.ID, "com.tpshop.malls:id/consignee_region_txtv"
    # 保存收货地址
    save_address_btn = By.ID, "com.tpshop.malls:id/submit_btn"

    @allure.step(title="点击所在区域的选择按钮")
    def click_region(self):
        self.click(self.region_text_view)

    @allure.step(title="输入收货人")
    def input_name(self, text):
        allure.attach("收货人：",text)
        self.input(self.name_text, text)

    @allure.step(title="输入手机号码")
    def input_mobile(self, text):
        allure.attach("手机号码：",text)
        self.input(self.mobile_text, text)

    @allure.step(title="输入详细地址")
    def input_address(self, text):
        allure.attach("详细地址：",text)
        self.input(self.address_text, text)

    @allure.step(title="点击保存收货地址")
    def click_save_address(self):
        self.click(self.save_address_btn)
