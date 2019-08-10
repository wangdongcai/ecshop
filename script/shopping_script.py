import time

from page.address_page import AddressPage
from page.confirm_order_page import ConfirmOrder
from page.goods_detail_page import GoodsDetail
from page.home_page import HomePage
from page.login_page import LoginPage
from page.user_center_page import UserCenter


class Shopping():

    def __init__(self,driver):
        self.home=HomePage(driver)
        self.user_center=UserCenter(driver)
        self.login=LoginPage(driver)
        self.address=AddressPage(driver)
        self.goods_detial=GoodsDetail(driver)
        self.confirm_order=ConfirmOrder(driver)


    def shopping_flow(self,username,password,data):
        #在首页点击我的进入用户中心
        self.home.click_user_center()
        #点击个人中心的头像进入登陆界面
        self.user_center.click_address()
        #登录
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()
        #新建一个地址
        time.sleep(6)
        self.user_center.click_address()
        self.address.click_add_new_address()
        self.address.input_consignee_name(data["consignee_name"])
        self.address.input_consignee_mobile(data["consignee_mobile"])
        self.address.choose_consignee_region()
        self.address.input_consignee_address(data["consignee_address"])
        self.address.click_save_address()

        #回到首页
        self.home.click_home()
        #选择商品
        self.home.click_goods()
        #点击立即购买
        time.sleep(5)
        self.goods_detial.click_buy_now()
        self.goods_detial.click_confirm()
        #使用积分和余额付款
        self.confirm_order.click_order_point()
        self.confirm_order.click_order_balance()
        #点击提交订单
        time.sleep(5)
        self.confirm_order.click_submit()
        self.confirm_order.input_pay_passwd("111111")
        self.confirm_order.click_confirm_pay()
        # 点击用户中心
        self.home.click_user_center()
        self.user_center.click_my_order()
        order_number = self.user_center.get_order_number()
        return order_number


if __name__ == '__main__':
    pass








