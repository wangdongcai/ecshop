import time

from common.base import Base, open_app
from data.config import Operation_config
from page.home_page import HomePage
from page.login_page import LoginPage


class GoodsDetail(Base):
    buy_now_loc=("xpath","//*[@text='立即购买']")
    add_cart_loc=("xpath","//*[@text='加入购物车']")
    collect_loc=("id","com.tpshop.malls:id/collect_img")
    confirm_loc=("xpath", "//*[@text='确定']")
    comment_loc = ("xpath", "//*[@text='评价']")
    comment_content=("id","com.tpshop.malls:id/comment_content_tv")


    def click_buy_now(self):
        """点击立即购买"""
        time.sleep(5)
        self.click(self.buy_now_loc)

    def click_add_cart(self):
        """点击加入购物车"""
        self.click(self.add_cart_loc)

    def clikc_collect(self):
        """点击收藏"""
        self.click(self.collect_loc)

    def click_confirm(self):
        """点击确定立即购买"""
        self.click(self.confirm_loc)

    def click_comment(self):
        """点击评价"""
        self.click(self.comment_loc)

    def find_comment(self,text):
        """找到自己评价的内容"""
        time.sleep(7)
        elements=self.find_elements(self.comment_content)
        for element in elements:
            content=element.text
            if content==text:
                return content


if __name__ == '__main__':
    driver = open_app()
    home=LoginPage(driver)