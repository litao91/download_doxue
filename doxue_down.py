from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



def download(driver, url):
    driver.get(url)
    WebDriverWait(driver, 3).until(
      expected_conditions.presence_of_element_located(
        (By.TAG_NAME, 'source')
      )
    )
    video_src = driver.find_element_by_tag_name("source").get_attribute("src")
    name = driver.find_element_by_tag_name("h4").get_attribute("innerHTML")
    print(name + " = " + video_src)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://www.doxue.com/video/play/1704"
    download(driver, url)

