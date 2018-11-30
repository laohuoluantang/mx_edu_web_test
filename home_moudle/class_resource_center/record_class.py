from home_moudle.home_page.home_page import Child_page_hover_by_css
import time
'''
driver：上层返回的浏览器对象
click_to_record_class_message:点击录制课堂所需测试数据集合

'''
class Record_class(object):
    def __init__(self, driver):
        self.driver = driver
        click_to_record = Child_page_hover_by_css(self.driver, 2, '录制课堂')
        click_to_record.goto_by_text_link()

#获取左侧列表所有年级名称
    def get_class_name_by_css(self):
        class_name_driver_list = self.driver.find_elements_by_css_selector('.ivu-tree-title')
        class_name_list = []
        for class_name_driver in class_name_driver_list:
            class_name_list.append(class_name_driver.text)
        return class_name_list

#选中学校节点
    def click_school_name_by_css(self):
        self.driver.find_elements_by_css_selector('.ivu-tree-title')[0].click()

#进入录制课堂页面后展开年级
    def unflod_grade_by_css(self):
        self.driver.find_elements_by_css_selector('.ivu-icon.ivu-icon-arrow-right-b')[1].click()


#获取对应班级的科目列表里的内容

#由于被隐藏所以让其强制显示（不会和实际使用不一致）
#1、先点开对应列表
#2、找到设置为displayed:none 的ul标签
#3、将其强制转为可见（这边为了简化，没有先一个个判断找到ul返回的self.driver是否是isDisplayed()在强制转，直接将所有的ul标签强制转）

    def get_subjects_list_by_css(self):
        self.driver.find_elements_by_css_selector('.ivu-select-placeholder')[0].click()
        time.sleep(1)

        ul_num = len(self.driver.find_elements_by_tag_name('ul'))
        for i in range(0, ul_num):
            self.driver.execute_script('document.querySelectorAll("ul")[' + str(i) + '].style.display="block";')

        subjects_driver_list = self.driver.find_elements_by_css_selector('.ivu-select-item')
        subjects_list = []
        for subjects_driver in subjects_driver_list:
            subjects_list.append(subjects_driver.text)
        return subjects_list

#展开年级后选择班级
    def click_class_by_css(self):
        self.driver.find_elements_by_css_selector('.ivu-tree-title')[2].click()
        class_name_list = [self.driver.find_elements_by_css_selector('.ivu-tree-title')[2].text, self.driver.find_elements_by_css_selector('.ivu-tree-title')[3].text]
        return self.driver, class_name_list

#点击更多下拉菜单
#drop_menu_num:下拉菜单选择
    def click_drop_menu(self, drop_menu_num):
        self.driver.find_elements_by_css_selector('.ivu-icon.ivu-icon-ios-arrow-down')[drop_menu_num].click()

#下拉菜单driver列表长度
    def get_click_drop_menu_list_len(self):
        driver_list = self.driver.find_elements_by_css_selector('.ivu-icon.ivu-icon-ios-arrow-down')
        return len(driver_list)
#点击下拉菜单中的选项
    def join_evaluate_course(self, link_text):
        self.driver.find_element_by_link_text(link_text).click()

#发布课程到评课，为input type=file类型，可用send_keys方法发送文件，这个比较奇怪，需要在定位元素的上一个class中去发送
    def release_course_to_evaluate_center(self, course_title, course_content, picture_root, submit = True):
        self.driver.find_elements_by_css_selector('.ivu-input')[1].send_keys(course_title)
        self.driver.find_elements_by_css_selector('.ivu-input')[2].send_keys(course_content)
        self.driver.find_elements_by_css_selector('.img-inputer__inputer')[0].send_keys(picture_root)
        time.sleep(1)
        if submit:
            self.driver.find_elements_by_css_selector('.ivu-btn.ivu-btn-primary')[2].click()
        else:
            self.driver.find_elements_by_css_selector('.ivu-btn')[5].click()
        time.sleep(1)
#若不需要其他操作，通过该方法返回driver
    def get_driver(self):
            return self.driver