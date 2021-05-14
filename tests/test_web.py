import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mozilla.org"
title = "Internet for people"


@pytest.fixture
def web_fix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = wait(driver, 10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    # always quit driver
    driver.quit()


def test_add():
    assert 2 + 3 == 5


def test_web_link(web_fix):
    web_fix.find_element_by_link_text("Загрузить Firefox").click()
    title = web_fix.title
    assert 'Firefox' in title
