import time

from common.base import Base, open_app
from data.config import Operation_config


class HomePage(Base):
    mine_loc = ("id", "com.tpshop.malls:id/mine_img")
    user_center_loc = ("id", "com.tpshop.malls:id/home_menu_user_layout")
    good_loc = ("id", "com.tpshop.malls:id/shop_img_iv")
    home_loc = ("id", "com.tpshop.malls:id/home_img")
    goods_promotion_loc = ("xpath", "//*[@text = '商品促销']")
    promotion_goods_loc=("xpath", "//*[contains(@text,'容声冰箱小型家用宿舍冷藏冷冻电冰箱租房二人世界三门节能小冰箱')]")

    search_default = ("id", "com.tpshop.malls:id/default_search_et")  # 请输入搜索关键词
    send_search = ("id", "com.tpshop.malls:id/search_et")  # 输入框
    search_click = ("xpath", "//*[@text='搜索']")  # 搜索按钮
    goods_img = ("id", "com.tpshop.malls:id/product_pic_img")  # 商品图

    def click_mine(self):
        """点击首页我的"""
        self.click(self.mine_loc)

    def click_user_center(self):
        """点击用户中心"""
        self.click(self.user_center_loc)

    def click_goods(self):
        """滑动直到点击育儿大百科"""
        self.click(self.good_loc)

    def search_goods(self):
        """搜索并点击"""
        self.click(self.search_default)
        self.send_keys(self.send_search,"容声冰箱")
        self.click(self.search_click)
        self.click(self.goods_img)



    def click_home(self):
        """点击首页"""
        self.click(self.home_loc)

    def click_promotion(self):
        """点击商品促销"""
        self.click(self.goods_promotion_loc)

    def click_promotion_goods(self):
        """点击促销商品"""
        self.swipe_while(self.promotion_goods_loc)


if __name__ == '__main__':
    driver = open_app()

    home = HomePage(driver)
    # home.click_mine()
    home.click_user_center()
