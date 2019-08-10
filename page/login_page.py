import time

from common.base import Base
from data.config import Operation_config
from common.base import open_app
from page.home_page import HomePage
# from page.user_center_page import UserCenter
# from page.user_center_page import UserCenter
from page.user_center_page import UserCenter


class LoginPage(Base):
    username_loc = ("xpath", "//*[@text='请输入账号']")
    password_loc = ("id", 'com.tpshop.malls:id/pwd_et')
    login_loc = ("id", "com.tpshop.malls:id/login_tv")


    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc, text)

    def input_password(self, text):
        """输入密码"""
        self.send_keys(self.password_loc, text)
        time.sleep(10)

    def click_login(self):
        """点击登陆"""
        self.press(self.login_loc)
        print("====           登录成功         ==========")


if __name__ == '__main__':
    driver = open_app()
    swipe = Base(driver)
    home = HomePage(driver)
    #home.click_mine()
    home.click_user_center()
    user = UserCenter(driver)
    time.sleep(5)
    user.click_address()
    login = LoginPage(driver)
    login.input_username("17788888888")
    login.input_password("123456")
    login.click_login()
    time.sleep(10)
    user.click_address()
