from selenium import webdriver
import time

'''
通过css来定位登录页面，页面加载慢，需要强制延时
login_url:登陆页面链接
username:用户名
password:密码
'''
class Login_web_by_css(object):
    def __init__(self, login_url, username, password):
        self.login_url = login_url
        self.username = username
        self.password = password

    def login(self, switch_school = True):
        options = webdriver.ChromeOptions()
        #设置不弹出下载窗口，默认下载路径
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\mx_edu_web_selenium'}
        options.add_experimental_option('prefs', prefs)
        #第一次得到返回的浏览器对象,需要关闭防火墙
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(self.login_url)
        #定位到用户名输入框输入用户名
        driver.find_elements_by_css_selector('.ivu-input')[0].send_keys(self.username)
        #定位到密码输入框输入密码
        driver.find_elements_by_css_selector('.ivu-input')[1].send_keys(self.password)
        #点击登录按钮
        driver.find_elements_by_css_selector('.ivu-form-item-content')[2].click()
        #登录后切换节点
        if switch_school:
            time.sleep(1)
            time.sleep(1)
            #展开学校列表
            driver.find_elements_by_css_selector('.item')[0].click()
            #需要强制延时，否则无法找齐所有元素
            time.sleep(1)
            #选择学校
            driver.find_elements_by_css_selector('.ivu-radio-wrapper.ivu-radio-group-item')[12].click()
            time.sleep(1)
            #点击确认按钮
            driver.find_elements_by_css_selector('.ivu-btn.ivu-btn-primary')[0].click()
        return driver


#login模块自测
if __name__ == '__main__':
    test_login = Login_web_by_css('http://edu.meetsoon.cn/education/login', '17612031655', '123456')
    driver = test_login.login(0)
    time.sleep(10)
    driver.quit()