import time

from common.base import Base
from data.config import Operation_config
from common.base import open_app
from page.home_page import HomePage
from page.login_page import LoginPage
from page.user_center_page import UserCenter


class AddressPage( Base):

        add_address_loc=("xpath","//*[@text='+新建地址']")
        consignee_name_loc=("id","com.tpshop.malls:id/consignee_name_et")
        consignee_mobile_loc=("id", "com.tpshop.malls:id/consignee_mobile_et")
        consignee_region_loc=("id","com.tpshop.malls:id/consignee_region_tv")
        province_loc=("xpath","//*[@text='江苏省']")
        city_loc=("xpath","//*[@text='盐城市']")
        district_loc=("xpath","//*[@text='亭湖区']")
        street_loc=("xpath","//*[@text='五星街道']")
        confirm_address_loc=("id","com.tpshop.malls:id/btn_right")
        consignee_address_loc=("id", "com.tpshop.malls:id/consignee_address_et")
        save_address_loc=("xpath","//*[@text='保存收货地址']")


        def click_add_new_address(self):
            """点击新建地址"""
            self.click(self.add_address_loc)

        def input_consignee_name(self,text):
            """输入收货人姓名"""
            self.send_keys(self.consignee_name_loc,text)

        def input_consignee_mobile(self,text):
            """输入电话号码"""
            self.send_keys(self.consignee_mobile_loc,text)

        def choose_consignee_region(self):
            """选择收货人所在区"""
            self.click(self.consignee_region_loc)
            #选择省市区街道
            time.sleep(5)
            self.swipe_while(self.province_loc)
            self.swipe_while(self.city_loc)
            time.sleep(5)
            self.swipe_while(self.district_loc)
            time.sleep(5)
            self.swipe_while(self.street_loc)
            self.click(self.confirm_address_loc)



        def input_consignee_address(self,text):
            """收货人详细地址"""
            self.send_keys(self.consignee_address_loc, text)

        def click_save_address(self):
            """点击保存收货地址"""
            self.click(self.save_address_loc)
            time.sleep(5)
            self.click_back()



if __name__ == '__main__':
    driver = open_app()
    swipe = Base(driver)
    home = HomePage(driver)
    # home.click_mine()
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
    address=AddressPage(driver)
    address.click_add_new_address()
    time.sleep(5)
    address.input_consignee_name("三只松鼠")
    address.input_consignee_mobile(18888888888)
    address.choose_consignee_region()
    address.input_consignee_address("三只小猪")
    address.click_save_address()


