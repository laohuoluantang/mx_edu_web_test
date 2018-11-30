import unittest
import time
from test_assist.htmltestrunner.HTMLTestRunner_PY3 import HTMLTestRunner
from test_moudle.test_record_class.test_record_class import Test_record_class
from test_moudle.test_evaluate_research_center.test_evaluate_course_center import Test_evaluate_course_center

'''
1、定义与web界面有关的css元素以及测试数据
2、各模块只定义动作，定位均为class和序号作为传入参数，方便根据页面改动而修改
'''


if __name__ == '__main__':
    report_title = '用例执行报告'
    desc = 'mx_edu_test'
    time_now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    report_file = str(time_now) + '.html'
    time.sleep(1)
    testsuite = unittest.TestSuite()
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_record_class))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_evaluate_course_center))

    with open(report_file, 'wb') as report:
        #verbosity设置大于1 显示测试用例执行情况
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc, verbosity=2)
        runner.run(testsuite)
    # unittest.main()