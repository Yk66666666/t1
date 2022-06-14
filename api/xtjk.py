'''-------------------封装被测系统接口------------------'''


class Jk:
    #初始化  登录地址以及验证码地址
    def __init__(self):
        self.dl_url = 'http://localhost/index.php?m=Home&c=User&a=do_login'
        self.yzm_url = 'http://localhost/index.php?m=Home&c=User&a=verify'
    #验证码接口
    #这个session留着后面调用它的人来定义  session = requests.Session()
    def yzm(self,session):
        return session.get(self.yzm_url)

    #登录接口
    def dl(self,session,username,password,verify_code):

        dl_data = {
            'username': username,
            'password': password,
            'verify_code': verify_code
        }
        return session.post(url = self.dl_url,data=dl_data)