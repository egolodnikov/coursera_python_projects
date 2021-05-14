from selenium import webdriver

url = "https://www.mozilla.org"
title = "Internet for people"


def see_links():
    """
    See all links on "mozilla.org"
    :return:
    """
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        links = driver.find_elements_by_tag_name("a")
        for link in links:
            href = link.get_attribute("href")
            print(href)
    except Exception as e:
        print(e)
    driver.quit()


if __name__ == "__main__":
    see_links()
