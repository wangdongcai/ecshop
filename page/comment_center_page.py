import time

from common.base import Base, open_app
from data.config import Operation_config


class CommentCenter(Base):
    """评价中心"""

    evaluate_img_loc=("id","com.tpshop.malls:id/order_show_btn")
    evaluate_content_loc=("xpath","//*[@text='请输入评价']")
    add_img_loc=("id","com.tpshop.malls:id/add_img")
    choose_img_loc=("xpath","//*[@text='从相册选择']")
    star_loc=("id","com.tpshop.malls:id/star5_btn")
    submit_loc=("xpath","//*[@text='提交']")
    goods_title_loc=("id","com.tpshop.malls:id/product_name_tv")
    have_comment_loc = ("xpath", "//*[contains(@text,'已评价')]")
    have_comment_goods_loc=("id","com.tpshop.malls:id/product_name_tv")


    def click_evaluate_img(self):
        """点击评价"""
        # self.click(self.evaluate_img_loc)
        element=self.find_elements(self.evaluate_img_loc)
        element[0].click()


    def get_text(self):
        """获取被评价商品的标题"""
        title=self.goods_title(self.goods_title_loc)
        print(f"""
====  评价商品的标题   =====
【{title}】

""")



    def input_evaluate_content(self,text):
        """输入评价内容"""
        self.send_keys(self.evaluate_content_loc,text)

    def click_add_img(self):
        """点击添加图片"""
        self.click(self.add_img_loc)

    def img_from_photo_album(self):
        """从相册选择图片"""
        self.click(self.choose_img_loc)

    def click_star(self):
        """星级评价"""
        elements=self.find_elements(self.star_loc)

        for element in elements:
            element.click()

    def click_submit(self):
        """点击提交"""
        self.click(self.submit_loc)


    def click_have_comment(self):
        """点击已评价"""
        self.click(self.have_comment_loc)

    def find_have_comment_goods(self):
        """根据标题找到已经评价的商品"""
        elements=self.find_elements(self.have_comment_goods_loc)
        # for element in elements:
        #     title_com=element.text
        #     time.sleep(8)
        #     if title_com==title:
        #         element.click()
        elements[0].click()


if __name__ == '__main__':
    pass












