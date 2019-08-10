import time

from page.address_page import AddressPage
from page.comment_center_page import CommentCenter
from page.confirm_order_page import ConfirmOrder
from page.goods_detail_page import GoodsDetail
from page.home_page import HomePage
from page.login_page import LoginPage
from page.user_center_page import UserCenter
from common.base import open_app




class CommentFlow():

    def __init__(self,driver):
        self.home=HomePage(driver)
        self.user_center=UserCenter(driver)
        self.login=LoginPage(driver)
        self.address=AddressPage(driver)
        self.goods_detial=GoodsDetail(driver)
        self.confirm_order=ConfirmOrder(driver)
        self.comment_center = CommentCenter(driver)


    def comment_flow(self,username,password,text):
        """评价流程"""
        # 在首页点击我的进入用户中心
        self.home.click_user_center()
        # 点击个人中心的头像进入登陆界面
        self.user_center.click_address()
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()

        #点击待评价订单
        time.sleep(6)
        self.user_center.click_wait_evaluate()
        #进入评价中心,获取标题
        self.comment_center.get_text()
        #点击评价晒单
        self.comment_center.click_evaluate_img()

        #输入评价内容
        time.sleep(9)
        self.comment_center.input_evaluate_content(text)
        #星级评价
        time.sleep(9)
        self.comment_center.click_star()
        #点击提交
        self.comment_center.click_submit()
        #点击已评价
        self.comment_center.click_have_comment()
        #点击评价的商品
        time.sleep(9)
        self.comment_center.find_have_comment_goods( )
        #点击评价
        time.sleep(9)
        self.goods_detial.click_comment()
        #打印评价内容
        time.sleep(9)
        content=self.goods_detial.find_comment(text)
        return content







if __name__ == '__main__':

    driver=open_app()
    ass=CommentFlow(driver)
    ass.comment_flow("17788888888","123456","111111")