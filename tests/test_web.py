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
        element = wait(driver, 5).until(EC.title_contains(title))
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
    assert 'Mozilla' in title


def test_web_links(web_fix):
    links = web_fix.find_elements_by_tag_name("a")
    urls = ['cnbc.com', 'bbc.com', 'mozilla', 'firefox', 'buzzfeed', 'getpocket', 'thenextweb']
    for link in links:
        href = link.get_attribute("href")
        # TODO
        # так как при больше чем 2 значениях через or почему-то в href пустая строка в проверке
        # вероятно связано с тем, что ссылки успевают затираться как-то
        tmp = {url in href for url in urls}
        assert True in tmp
