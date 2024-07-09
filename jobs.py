from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdf_creator
import time
import os

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.indeed.com.br/'

chrome.get(url)

search_box = chrome.find_element(By.ID,'text-input-what')

search_box.send_keys('Estagio Desenvolvimento')

search_button = chrome.find_element(By.CLASS_NAME,'yosegi-InlineWhatWhere-primaryButton')

search_button.click()

page_source = chrome.page_source

soup = BeautifulSoup(page_source, 'html.parser')

jobs_list = soup.find('ul',class_="css-zu9cdh eu4oa1w0")


if jobs_list:

    list_items = jobs_list.find_all('li')
    list_content = [item.get_text() for item in list_items]
    
    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vagas.pdf")
    pdf_creator.create_pdf(list_content, pdf_path)

else:
    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vagas.pdf")
    pdf_creator.create_pdf("LISTA NAO ENCONTRADA", pdf_path)
    print("Lista não encontrada.")

time.sleep(10)
chrome.quit()

