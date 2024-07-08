from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.indeed.com.br/'

chrome.get(url)

search_box = chrome.find_element(By.ID,'text-input-what')

search_box.send_keys('Estagio Desenvolvimento')


search_button = chrome.find_element(By.CLASS_NAME,'yosegi-InlineWhatWhere-primaryButton')

search_button.click()


time.sleep(10)
chrome.quit()

