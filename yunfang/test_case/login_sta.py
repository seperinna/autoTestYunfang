#coding=utf-8
from time import sleep
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,function
from page_obj.loginPage import login

class LoginTest(myunit.MyTest):
    """ 云房登录测试   """

    #测试用户登录
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        """ 用户名，密码为空登录"""
        self.user_login_verify()
        po=login(self.driver)
        self.assertEqual(po.error_hint(),u'账户名或登录密码不正确，请重新输入')
        function.insert_img(self.driver,'user_psw_empty.jpg')

    def test_login2(self):
        """ 用户名正确，密码为空登录"""
        self.user_login_verify(username='13555555555')
        po=login(self.driver)
        self.assertEqual(po.error_hint(),u'账户名或登录密码不正确，请重新输入')
        function.insert_img(self.driver,'psw_empty.jpg')

    def test_login3(self):
        """ 用户名为空，密码正确登录"""
        self.user_login_verify(password='111111')
        po=login(self.driver)
        self.assertEqual(po.error_hint(),u'账户名或登录密码不正确，请重新输入')
        function.insert_img(self.driver,'user_empty.jpg')

    def test_login4(self):
        """ 用户名与密码不匹配"""
        character=random.choice('zyxwvutsrqponmlkjihgfedcba')
        username="test"+character
        self.user_login_verify(username=username,password=123456)
        po=login(self.driver)
        self.assertEqual(po.error_hint(),u'账户名或登录密码不正确，请重新输入')
        function.insert_img(self.driver,'user_psw_error.jpg')

    def test_login5(self):
        """ 用户名，密码正确登录"""
        self.user_login_verify(username='13555555555',password='111111')
        sleep(3)
        po=login(self.driver)
        po.switch_window()
        sleep(3)
        function.insert_img(self.driver,'user_pwd_ture.jpg')

if __name__=="__main__":
    unittest.main()
