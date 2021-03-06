import random
import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegionPage(BaseAction):
    # 选择地区
    city_text_view = By.ID, "com.tpshop.malls:id/tv_city"
    # 确定 按钮
    commit_btn = By.ID, "com.tpshop.malls:id/btn_right"

    @allure.step(title="选择省市区镇")
    def click_city(self):
        for i in range(4):
            # 获取所有的com.tpshop.malls:id/tv_city
            cities = self.find_elements(self.city_text_view)
            # 获取elements的长度 根据长度生成随机数
            city_index = random.randint(0, len(cities) - 1)
            # 在列表中随机获取一个元素进行点击
            cities[city_index].click()
            time.sleep(2)

    @allure.step(title="选择后点击确定")
    def click_commit(self):
        self.click(self.commit_btn)
