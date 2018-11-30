from home_moudle.login.login import Login_web_by_css
from test_assist.login_mes import login_mes
from home_moudle.class_resource_center.record_class import Record_class
import time
import unittest

'''
测试数据
'''
#学校、年级信息
test_school_name = '测试学校-wwp'
test_grade_name = ['小学一年级', '初中一年级', '高中三年级']
test_class_name = ['上课班', '听课班']
#科目列表
test_subjects_list = ['化学', '历史', '地理', '政治', '数学', '物理', '生物', '英语', '语文', '名字比较长的课程名字比较长的课程', '测试课程1', '测试课程3']
#老师列表
test_teachers_list = ['数学老师', '语文老师', '音乐老师', '英语老师', '绝命毒师', '化学老师', '名字比较长的的老师']
class Test_record_class(unittest.TestCase):
    ''' 录制课堂测试用例集 '''

    @classmethod
    def setUpClass(self):
        user_login_test = Login_web_by_css(*login_mes)
        self.driver = user_login_test.login()
        # 切换到录制课堂
        self.record_class_test = Record_class(self.driver)
        time.sleep(1)

    def test_a_class(self):
        '''验证测试节点年级的正确性（个数、名称）'''
        grade_name_list = self.record_class_test.get_class_name_by_css()
        self.assertEqual(len(test_grade_name), len(grade_name_list) - 1)
        for i in range(0, len(test_grade_name)):
            with self.subTest(i = i):
                self.assertEqual(test_grade_name[i], grade_name_list[i + 1])
                print(grade_name_list[i + 1])
        self.assertEqual(test_school_name, grade_name_list[0])

    def test_b_grade(self):
        '''验证测试节点班级的正确性（个数、名称）'''
        # 展开班级
        self.driver = self.record_class_test .unflod_grade_by_css()
        time.sleep(1)
        # 选中班级
        return_list = self.record_class_test .click_class_by_css()
        time.sleep(1)
        self.driver = return_list[0]
        class_name_get = return_list[1]
        self.assertEqual(len(test_class_name), len(class_name_get))
        for i in range(0, len(test_class_name)):
            with self.subTest(i = i):
                self.assertEqual(test_class_name[i], class_name_get[i])

    def test_c_subjects(self):
        '''验证科目下拉列表中科目正确性（个数和名称）'''
        subjects_list_get = self.record_class_test.get_subjects_list_by_css()
        self.assertEqual(len(test_subjects_list + test_teachers_list), len(subjects_list_get))
        for i in range(0, len(test_subjects_list)):
            with self.subTest(i = i):
                self.assertEqual((test_subjects_list)[i], subjects_list_get[i])
        #temp test
        # self.record_class_test.click_drop_menu(0)
        # time.sleep(1)
        # self.record_class_test.join_evaluate_course('参选评课')
        # self.record_class_test.release_course_to_evaluate_center('test', 'test', 'D:/jpg500k.jpg')
        # time.sleep(10)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()