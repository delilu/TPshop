import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(location_by, location_value))

    def find_elements(self, location, timeout=10.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(location_by, location_value))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = self.find_element((By.XPATH, message), timeout, poll=0.1)
        return element.text

    @allure.step(title="判断toast是否存在")
    def is_toast_exist(self, message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    @allure.step(title="判断这个元素/按钮是否可用")
    def is_location_enabled(self, location):
        return self.find_element(location).get_attribute("enabled") == "true"

    @allure.step(title="判断这个元素/按钮是否可点击")
    def is_location_clickable(self, location):
        return self.find_element(location).get_attribute("clickable") == "true"

    @allure.step(title="判断这个元素/按钮在页面是否存在")
    def is_location_exist(self, location):
        try:
            self.find_element(location)
            return True
        except:
            return False

    def press_keycode(self, key_code):
        cap_dict = self.driver.capabilities
        if cap_dict.get("automationName") == "Uiautomator2":
            self.driver.press_keycode(key_code)
        else:
            self.driver.key_event(key_code)

    @allure.step(title="点击返回按钮")
    def press_back(self):
        self.press_keycode(4)

    @allure.step(title="点击回车按钮")
    def press_enter(self):
        self.press_keycode(66)

    @allure.step("屏幕滑动一次的方法")
    def scroll_page_one_time(self, direction="up"):
        """
        屏幕滑动一次
        :param direction: 滑动方向
        up:从下往上滑
        down：从上往下
        left:从左往右
        right：从右往左
        """
        screen_size = self.driver.get_window_size()
        width = screen_size["width"]
        height = screen_size["height"]
        center_x = width * 0.5
        center_y = height * 0.5
        top_x = center_x
        top_y = height * 0.25
        down_x = center_x
        down_y = height * 0.75
        left_x = width * 0.25
        left_y = center_y
        right_x = width * 0.75
        right_y = center_y
        if direction == "up":
            self.driver.swipe(down_x, down_y, top_x, top_y, 2000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, down_x, down_y, 2000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 2000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 2000)
        else:
            raise Exception("请输入正确的参数:up、left、right、down")

    @allure.step("滑动找到元素位置")
    def is_location_exist_scroll_page(self, location, direction='up'):
        old_page = None
        new_page = self.driver.page_source
        while True:
            if self.is_location_exist(location):
                return True
            else:
                if not old_page == new_page:
                    self.scroll_page_one_time(direction)
                    old_page = new_page
                    new_page = self.driver.page_source
                else:
                    return False
