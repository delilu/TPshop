from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        # 点击我的
        self.page.home.click_mine()
        # 判断是否登录
        if not self.page.mine.is_login():
            # 进行登录
            self.page.mine.click_login_sign_up()
            self.page.login.login()
        # 滑动页面找 收货地址
        if self.page.mine.is_location_exist_scroll_page(self.page.mine.address_btn):
            # 点击收货地址
            self.page.mine.click_address()
            # 点击 新建地址
            self.page.address.click_new_address()
            # 输入收货人
            self.page.new_address.input_name("hello")
            # 输入手机号码
            self.page.new_address.input_mobile("13100131008")
            # 输入详细地址
            self.page.new_address.input_address("花园小区10栋4单元508")
            # 点击 所在地区
            self.page.new_address.click_region()
            # 选择省市区镇
            self.page.region.click_city()
            # 选择后点击 确定
            self.page.region.click_commit()
            # 点击 保存收货地址
            self.page.new_address.click_save_address()
            # 断言是否添加成功
            assert self.page.address.is_toast_exist("添加成功")
        else:
            assert False
