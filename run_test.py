#导包
import common.HTMLTestRunnerNew as HT
import unittest
import time
#设置一个装这些用例的容器
suite = unittest.TestSuite()
#设置一个发现用例的工具
load = unittest.defaultTestLoader
#用load取发现用例
testcases=load.discover('test_cases',pattern='test*.py',top_level_dir=None)
#把发现的用例放在容器中
suite.addTests(testcases)
#设置测试报告的文档名字-----固定的名字reporter+当前系统时间+.html
#currenttime = time.strftime("%Y-%m-%d %H-%M-%S")
filename = r'report/reporter.html'
#生成测试报告  1、保证HTMLTestRunnerNew包要在common文件中 2 导包 import  common.HTMLTestRunnerNew as HT
with open(filename,'wb+') as fp:
    runner=HT.HTMLTestRunner(stream=fp,title='学生管理系统接口测试报告',description='balalala',tester="xj")
    runner.run(suite)













