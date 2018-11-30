from home_moudle.home_page.home_page import Child_page_hover_by_css
import time
'''
driver：上层返回的浏览器对象
click_to_record_class_message:点击录制课堂所需测试数据集合

'''
class Evaluate_course_center(object):
    def __init__(self, driver):
        self.driver = driver
        click_to_evaluate = Child_page_hover_by_css(self.driver, 6, '评课中心')
        click_to_evaluate.goto_by_text_link()

#获取当前评课中心页面课程总数
    def get_current_course_num_by_id(self):
        course_num = len(self.driver.find_elements_by_id('evaCard'))
        return course_num

#获取课程的详细信息
    def get_course_detail_info(self):
        course_info_list = []
        course_info_list.append(self.driver.find_element_by_id('title').text)
        course_info_list.append(self.driver.find_element_by_id('content').text)
        course_info_list.append(self.driver.find_element_by_id('infoBlock').text)
        return course_info_list
#点击查询按钮
    def click_query_button_by_tag(self):
        self.driver.find_elements_by_tag_name('button')[0].click()

#点击重置按钮
    def click_reset_button_by_id(self):
        self.driver.find_element_by_id('reset').click()

#删除当前评课中心页面课程
    def del_current_course_num_by_id(self):
        #先点击重置再查询，列出所有课程
        self.click_reset_button_by_id()
        time.sleep(1)
        self.click_query_button_by_tag()
        time.sleep(1)
        course_num = self.get_current_course_num_by_id()
        for i in range(0, course_num):
            #从0删除时，只会删除一半，因为find_elements_by_id在不断更新找到的数据
            # self.driver.find_elements_by_id('del')[i].click()
            self.driver.find_elements_by_id('del')[course_num - 1 - i].click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('.ivu-btn.ivu-btn-primary.ivu-btn-large').click()
            time.sleep(1)

    # 由于被隐藏所以让其强制显示（不会和实际使用不一致）
    # 1、先点开对应列表
    # 2、找到设置为displayed:none 的ul标签
    # 3、将其强制转为可见（这边为了简化，没有先一个个判断找到ul返回的self.driver是否是isDisplayed()在强制转，直接将所有的ul标签强制转）
#获取对列表里的内容
    def get_list_content_func_by_css(self, css_num):
        def get_list_content():
            self.driver.find_elements_by_css_selector('.ivu-icon.ivu-icon-arrow-down-b.ivu-select-arrow')[css_num].click()
            time.sleep(1)
            ul_num = len(self.driver.find_elements_by_tag_name('ul'))
            for i in range(0, ul_num):
                self.driver.execute_script('document.querySelectorAll("ul")[' + str(i) + '].style.display="block";')
                driver_list = self.driver.find_elements_by_css_selector('.ivu-select-item')
                content_list = []
            for driver_one in driver_list:
                content_list.append(driver_one.text)
                # 注：py3的filter返回的是迭代器
                content_list = list(filter(lambda s: s and s.strip(), content_list))
            return content_list
        return get_list_content

#点击列表里的内容
    def click_list_content_func_by_css(self, css_num):
        def click_list_content(click_css_num):
            self.driver.find_elements_by_css_selector('.ivu-icon.ivu-icon-arrow-down-b.ivu-select-arrow')[css_num].click()
            time.sleep(1)
            ul_num = len(self.driver.find_elements_by_tag_name('ul'))
            for i in range(0, ul_num):
                self.driver.execute_script('document.querySelectorAll("ul")[' + str(i) + '].style.display="block";')
                driver_list = self.driver.find_elements_by_css_selector('.ivu-select-item')
            driver_list[click_css_num].click()
        return click_list_content



#若不需要其他操作，通过该方法返回driver
    def get_driver(self):
            return self.driver