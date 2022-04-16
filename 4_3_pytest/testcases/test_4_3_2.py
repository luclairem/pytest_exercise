# -*- coding:utf-8 -*-
# Time : 2022/4/11 20:01
# Author : Lu
# File : test_4_3_2.py
# Desc :
import pytest
import allure


@allure.feature('登录模块')
class TestCases1:
    @allure.story('登录成功的测试用例')
    def test_1(self):
        with allure.step('输入用户名和密码'):
            print('用户名和密码')
        with allure.step('点击登录'):
            print('点击登录按钮')

    @pytest.mark.smoke
    @allure.story('登录失败的测试用例')
    def test_2(self):
        print('第二个测试用例')


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
