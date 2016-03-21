#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    """
    用户登录页面
    """
    url='/login/toLogin'

    #登录页面元素
    login_username_loc=(By.NAME,'userName')
    login_password_loc=(By.NAME,'password')
    login_button_loc=(By.ID,'loginBtn')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username="13555555555",password='111111'):
        """
        获取的用户名密码登录
        """
        self.open()
        sleep(3)
        self.login_username(username)
        self.login_password(password)
        self.login_button()


    error_hint_loc=(By.XPATH,'//*[@id="loginForm"]/div[1]/span') #提示框元素

    #错误提示
    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text



