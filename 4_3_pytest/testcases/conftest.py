# -*- coding:utf-8 -*-
# Time : 2022/4/6 21:12
# Author : Lu
# File : conftest.py
# Desc :
import pytest
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from config.config import driver_path, url


@pytest.fixture(scope='session')
def login():
    e = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=e)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()

