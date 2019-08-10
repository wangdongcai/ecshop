import time
from common.base import Base, open_app
from data.config import Operation_config

class ConfirmOrder(Base):

    order_point_loc=("id","com.tpshop.malls:id/order_point_sth")
    order_balance_loc=("id", "com.tpshop.malls:id/order_balance_sth")
    submit_order_loc=("xpath","//*[@text='提交订单']")
    pay_passwd_loc=("id","com.tpshop.malls:id/pwd_et")
    confirm_pay_loc=("id","com.tpshop.malls:id/sure_tv")

    def click_order_point(self):
        """点击使用积分"""
        self.click(self.order_point_loc)

    def click_order_balance(self):
        """点击使用余额"""
        self.click(self.order_balance_loc)

    def click_submit(self):
        """点击提交订单"""
        time.sleep(6)
        self.click(self.submit_order_loc)

    def input_pay_passwd(self,text):
        """输入字符密码"""
        time.sleep(5)
        self.send_keys(self.pay_passwd_loc,text)

    def click_confirm_pay(self):
        """点击确定"""
        self.click(self.confirm_pay_loc)
        self.click_back()
        time.sleep(4)
        self.click_back()
        time.sleep(4)
        self.click_back()
        time.sleep(4)
        self.click_back()




