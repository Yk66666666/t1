#执行测试用例入口，并生成html网页
from HTMLTestReportCN import HTMLTestRunner
import unittest
from script.csjb import Test_jb
#封装测试套件
zx = unittest.TestSuite()
zx.addTest(unittest.makeSuite(Test_jb))
#指定报告路径
bj_path = './report/tpshop.html'
#打开文件流
with open(bj_path,'wb') as f:
    #创建HTMLTestRunner执行器
    xxxx = HTMLTestRunner(f,title=('测试报告'))
    xxxx.run(zx)