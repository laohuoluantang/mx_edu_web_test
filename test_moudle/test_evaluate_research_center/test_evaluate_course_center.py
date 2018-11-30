'''
测试用例编号：
0、在录制课堂发布精品课程（注：为指定用于测试的课程涉及到时间只记录到天，测试时间不能跨天）
1、评课中心课程总数是否正确
2、年级列表中年级名称与数量是否正确
3、科目列表中年级名称与数量是否正确
4、主讲老师列表中年级名称与数量是否正确
5、测试年级筛选功能是否正确
6、测试科目筛选功能
7、测试主讲老师筛选功能
8、测试时间筛选功能
9、查询按钮是否有效
10、重置按钮
11、在首页中查看筛选的课程标题、简介、主讲老师是否正确
12、在详情页中查看课程标题、简介、主讲老师、评分是否正确
13、验证评分、评论功能
14、切换第二位账户，打分评论，查看评分的正确性
15、验证首页中删除功能
'''

from home_moudle.login.login import Login_web_by_css
from test_assist.login_mes import login_mes
from home_moudle.class_resource_center.record_class import Record_class
from home_moudle.evaluate_research_center .evaluate_course_center import Evaluate_course_center
import time
import unittest

'''
测试数据
'''
#年级列表
test_grade_name_list = ['小学一年级', '初中一年级', '高中三年级']

#科目列表
test_subjects_list = ['化学', '历史', '地理', '政治', '数学', '物理', '生物', '英语', '语文', '名字比较长的课程名字比较长的课程', '测试课程1', '测试课程3']

#老师列表
test_teachers_list = ['数学老师', '语文老师', '音乐老师', '英语老师', '绝命毒师', '化学老师', '名字比较长的的老师']

#课程详细信息
course_detail_info_list = ['test', 'test', '主讲老师：化学老师 时间：2018-11-29 14:24:10']
class Test_evaluate_course_center(unittest.TestCase):
    ''' 录制课堂测试用例集 '''

    @classmethod
    def setUpClass(self):
        user_login_test = Login_web_by_css(*login_mes)
        self.driver = user_login_test.login()
        # 切换到录制课堂
        self.record_class_test = Record_class(self.driver)
        self.record_class_test.click_school_name_by_css()
        time.sleep(1)
        course_num = self.record_class_test.get_click_drop_menu_list_len()
        for i in range(0, course_num):
            self.record_class_test.click_drop_menu(i)
            time.sleep(1)
            self.record_class_test.join_evaluate_course('参选评课')
            self.record_class_test.release_course_to_evaluate_center('test', 'test', 'D:\github_project\\auto_test_mx_edu\mx_edu_web_test\\test_assist\hmbb.jpg')
        self.driver.quit()
        time.sleep(1)
        #重新进入评课中心
        user_login_test = Login_web_by_css('http://mxtest.meetsoon.net/education/login', '17612031655', '111111')
        self.driver = user_login_test.login()
        self.evaluate_course_test = Evaluate_course_center(self.driver)
        time.sleep(3)

    def test_a_evaluate_course_num_all(self):
        '''在录制课堂发布精品课程后在评课中心查看课程总数是否正确'''
        course_num = self.evaluate_course_test.get_current_course_num_by_id()
        self.assertEqual(6, course_num)

    def test_b_grade_name_list(self):
        '''年级列表中年级名称与数量是否正确'''
        get_grade_list_func = self.evaluate_course_test.get_list_content_func_by_css(0)
        self.assertListEqual(test_grade_name_list, get_grade_list_func())

    def test_c_subject_name_list(self):
        '''科目列表中年级名称与数量是否正确'''
        get_subject_list_func = self.evaluate_course_test.get_list_content_func_by_css(1)
        self.assertListEqual(test_subjects_list, get_subject_list_func())

    def test_d_teacher_name_list(self):
        '''老师列表中年级名称与数量是否正确'''
        get_teacher_list_func = self.evaluate_course_test.get_list_content_func_by_css(2)
        self.assertListEqual(test_teachers_list, get_teacher_list_func())

    def test_e_query_by_grade(self):
        '''年级筛选功能；查询按钮功能；在首页中查看筛选的课程标题、简介、主讲老师、时间、评分是否正确'''
        query_by_grade_name_func = self.evaluate_course_test.click_list_content_func_by_css(0)
        query_by_grade_name_func(2)
        self.evaluate_course_test.click_query_button_by_tag()
        time.sleep(1)
        course_num = self.evaluate_course_test.get_current_course_num_by_id()
        self.assertEqual(1, course_num)
        detail_info_get_list = self.evaluate_course_test.get_course_detail_info()
        for i in range(0, 2):
            self.assertEqual(course_detail_info_list[i], detail_info_get_list[i])

    def test_f_query_by_subject(self):
        '''测试科目筛选功能'''
        #点击重置按钮
        self.evaluate_course_test.click_reset_button_by_id()
        time.sleep(1)
        self.evaluate_course_test.click_query_button_by_tag()
        time.sleep(1)
        query_by_subject_name_func = self.evaluate_course_test.click_list_content_func_by_css(1)
        query_by_subject_name_func(len(test_grade_name_list))
        self.evaluate_course_test.click_query_button_by_tag()
        time.sleep(1)
        course_num = self.evaluate_course_test.get_current_course_num_by_id()
        self.assertEqual(2, course_num)

    def test_g_query_by_teacher(self):
        '''测试主讲老师筛选功能'''
        #点击重置按钮
        self.evaluate_course_test.click_reset_button_by_id()
        time.sleep(1)
        self.evaluate_course_test.click_query_button_by_tag()
        time.sleep(1)
        query_by_teacher_name_func = self.evaluate_course_test.click_list_content_func_by_css(2)
        query_by_teacher_name_func(len(test_grade_name_list)+ len(test_subjects_list))
        self.evaluate_course_test.click_query_button_by_tag()
        time.sleep(1)
        course_num = self.evaluate_course_test.get_current_course_num_by_id()
        self.assertEqual(2, course_num)



    def test_z_del_course_all(self):
        '''删除所有课程，查看课程总数是否为0'''
        self.evaluate_course_test.del_current_course_num_by_id()
        self.assertEqual(0, self.evaluate_course_test.get_current_course_num_by_id())


    @classmethod
    def tearDownClass(self):
        self.driver.quit()

