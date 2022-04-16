# -*- coding:utf-8 -*-
# Time : 2022/4/4 20:47
# Author : Lu
# File : login_page.py
# Desc :
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.account_user = By.ID, 'account'
        self.password_user = By.NAME, 'password'
        self.login_user = By.ID, 'submit'
        self.user_logout = By.CLASS_NAME, 'user-name'
        self.logout = By.LINK_TEXT, '退出'
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(*self.account_user).clear()
        self.driver.find_element(*self.account_user).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_user).clear()
        self.driver.find_element(*self.password_user).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_user).click()

    def click_logout(self):
        self.driver.find_element(*self.user_logout).click()
        self.driver.find_element(*self.logout).click()











