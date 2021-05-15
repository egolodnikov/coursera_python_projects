from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def init_driver(fn):
    url = "https://www.mozilla.org"

    def wrapper(self):
        driver = webdriver.Firefox()
        driver.get(url)
        fn(self, driver)
        driver.quit()

    return wrapper


class MainTest:
    @init_driver
    def see_links(self, driver):
        """
        See all links on "mozilla.org"
        :return:
        """
        try:
            links = driver.find_elements_by_tag_name("a")
            for link in links:
                href = link.get_attribute("href")
                print(href)
        except Exception as e:
            print(e)

    @init_driver
    def see_account_form(self, driver):
        driver.find_element_by_link_text("Создать Аккаунт Firefox").click()
        try:
            element = wait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'email tooltip-below'))
            )
        except Exception as ex:
            print(ex)
        text_input = driver.find_element_by_tag_name('input')
        text_input.send_keys('fjordsail@gmail.com')
        driver.find_element_by_id('submit-btn').click()


if __name__ == "__main__":
    main_test = MainTest()
    main_test.see_account_form()
