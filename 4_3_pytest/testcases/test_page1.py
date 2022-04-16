# -*- coding:utf-8 -*-
# Time : 2022/4/4 20:20
# Author : Lu
# File : test_page1.py
# Desc :
import unittest
from time import sleep
from objectpage.login_page import LoginPage
from config.config import url, driver_path, system_version
from log.log import loggers
from data.data import ReadWrite


class TestLoginCase:
    def test_1(self,login):
        # 验证使用有效的用户名和密码，登录成功
        # print("登录的第一个测试用例")
        self.driver = login
        self.loginpage = LoginPage(self.driver)
        user_list = ReadWrite().excel_read('user')
        username = user_list[3][0]
        password = user_list[3][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(3)
        # assert '我的地盘 - 禅道' in self.driver.title
        self.loginpage.click_logout()
        loggers.info("有效用户名和密码，登录成功")

    # @unittest.skip('不执行该测试用例')
    @unittest.skipIf(system_version == '1.1', reason='只有在1.1版本时执行')
    def test_2(self):
        # 验证密码为空时，登陆失败
        # print("登录的第二个测试用例")
        self.loginpage.input_username('shelly')
        self.loginpage.login_user()
        sleep(2)
        alter_login = self.driver.switch_to.alert
        alter_login.accept()
