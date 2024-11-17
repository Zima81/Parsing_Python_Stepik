import time
from selenium import webdriver

path = '/home/igor/.config/google-chrome/Default/Extensions/gkkmpbaijflcgbbdfjgihbgmpkhgpgof/coordinates.crx'
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(path)

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)

