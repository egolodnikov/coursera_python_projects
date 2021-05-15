from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_python_org():
    driver = webdriver.Firefox()
    # задаем урл
    driver.get("http://www.python.org")
    # проверяем, что в заголовке странице есть Python
    assert "Python" in driver.title
    # поиск элемента с name="q"
    elem = driver.find_element_by_name("q")
    # эмулируем печать "pycon" в input
    elem.send_keys("pycon")
    # эмулируем нажатие BACKSPACE, тем самым удаляя "n",
    # получая в остатке "pyco"
    elem.send_keys(Keys.RETURN)
    # убеждаемся, что присутствует на странице надпись
    assert "No results found." not in driver.page_source
    driver.close()
