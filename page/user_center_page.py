import time
from common.base import Base, open_app
from data.config import Operation_config
from page.home_page import HomePage



class UserCenter(Base):

    click_address_loc=("xpath","//*[@text='地址管理']")
    click_head_loc=("id", "com.tpshop.malls: id / head_img")
    wait_evaluate_loc=("xpath","//*[@text='待评价']")
    my_order_loc = ("xpath", "//*[@text='我的订单']")
    order_number=("id","com.tpshop.malls:id/order_sn_tv")




    def click_address(self):
        """点击地址管理"""
        self.swipe_while(self.click_address_loc)

    def click_head(self):
        """点击个人中心的头像"""
        self.click(self.click_head_loc)
        # self.press(self.click_head_loc)

    def click_wait_evaluate(self):
        """点击待评价"""
        self.click(self.wait_evaluate_loc)

    def click_my_order(self):
        """点击我的订单"""
        self.click(self.my_order_loc)

    def get_order_number(self):
        """获取订单号"""
        elements=self.find_elements(self.order_number)
        order_number=elements[0].text
        return order_number




if __name__ == '__main__':
    driver = open_app()

    home = HomePage(driver)
    # home.click_mine()
    home.click_user_center()
    user=UserCenter(driver)
    time.sleep(10)
    user.click_address()
