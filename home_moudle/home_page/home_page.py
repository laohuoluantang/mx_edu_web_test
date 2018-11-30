from selenium.webdriver.common.action_chains import ActionChains
from home_moudle.login.login import Login_web_by_css
from test_assist.login_mes import login_mes
import time
'''
用于主页中的各子模块进入方式
driver：登陆后返回的driver
link_text:子模块上的链接文字名
'''
class Child_page_hover_by_css(object):
    def __init__(self, driver, card_num, link_text):
        self.driver = driver
        self.link_text = link_text
        self.card_num = card_num

    #点击显示出的元素
    def goto_by_text_link(self):
        above = self.driver.find_elements_by_css_selector('.itemText')[self.card_num ]
        #需要悬停显示元素
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_link_text(self.link_text).click()
        return self.driver

    #可获取所有显示元素
    def child_page_hover(self):
        above = self.driver.find_elements_by_css_selector('.itemText')[2]
        #需要悬停显示元素
        ActionChains(self.driver).move_to_element(above).perform()
        return self.driver

if __name__ == '__main__':
    test_login = Login_web_by_css(*login_mes)
    driver = test_login.login()
    time.sleep(1)
    test_hover = Child_page_hover_by_css(driver, 2, '录制课堂')
    driver =  test_hover.goto_by_text_link()
    time.sleep(5)
    driver.quit()

