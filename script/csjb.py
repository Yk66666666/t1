#测试脚本
import unittest
from parameterized import parameterized
from api.xtjk import Jk
import requests
from script.csh import csh
#定义测试类
class Test_jb(unittest.TestCase):
    #前置
    def setUp(self):
        #调用类方法得实例化
        self.jk = Jk()
        self.session = requests.Session()
    def tearDown(self):
        self.session.close()

    #定义测试方法
    @parameterized.expand(csh)
    def test_01(self,username,password,verify_code,Content_Type,status,status_code,msg):
        #调用验证码接口
        response = self.jk.yzm(self.session)
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertIn(Content_Type,response.headers.get('Content-type'))

        #调用登录接口
        response = self.jk.dl(self.session,username,password,verify_code)
        result = response.json()
        #登录断言
        self.assertIn(msg,result.get('msg'))
        self.assertEqual(status,result.get('status'))



