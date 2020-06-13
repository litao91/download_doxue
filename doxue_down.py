from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import selenium.webdriver.common.by
import sys
import os

def extract_urls(driver, page_url):
    driver.get(url)
    WebDriverWait(driver, 50).until(
      expected_conditions.presence_of_element_located(
        (By.ID, 'detailed-catalog')
      )
    )
    catalog = driver.find_element_by_id('detailed-catalog')
    hrefs = catalog.find_elements(By.TAG_NAME, "a")
    return [href.get_attribute('href') for href in hrefs]

def download(driver, url, base):
    driver.get(url)
    WebDriverWait(driver, 50).until(
      expected_conditions.presence_of_element_located(
        (By.TAG_NAME, 'source')
      )
    )
    video_src = driver.find_element_by_tag_name("source").get_attribute("src")
    name = driver.find_element_by_tag_name("h4").get_attribute("innerHTML").strip()
    print(name + " = " + video_src)
    dest = 'downloads/%s/%s' % (base, name)
    if os.path.exists(dest):
        print(dest + ' exists, skip')
        return
    cmd = '/Users/taoli/.local/bin/m3u8 -u="%s" -o="%s"' % (video_src, 'downloads/%s/%s' % (base, name))
    print('running: ' + cmd)
    os.system(cmd)

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        url = sys.argv[1]
        print('working on ' + url)
        urls = extract_urls(driver, url)
        for url in urls:
            print(url)
            download(driver, url, sys.argv[2])
    finally:
        driver.close()
"""
if __name__ == "__main__":
    driver = webdriver.Chrome()
    url_pattern = "https://www.doxue.com/video/play/%d"
    for i in range(int(sys.argv[1]), int(sys.argv[2])):
        try:
            print('i = %d' %(i))
            download(driver, url_pattern % i, sys.argv[3])
        except:
            pass

    driver.close()
"""
