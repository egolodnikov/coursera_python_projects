import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

url = "https://mozilla.org"
title = "Internet for people"


@pytest.fixture
def web_fix():
    driver = webdriver.Firefox()
    driver.get(url)


def test_add():
    assert 2 + 3 == 5
