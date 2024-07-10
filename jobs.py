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

def create_chrome_driver():
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except Exception as e:
        print(f"Erro ao iniciar o ChromeDriver: {e}")
        return None

def fetch_job_listings(driver, url):
    try:
        driver.get(url)

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'text-input-what'))
        )
        search_box.send_keys('Estagio Desenvolvimento')

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton'))
        )
        search_button.click()

        # Esperar até que a lista de vagas esteja presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.css-zu9cdh.eu4oa1w0'))
        )

        return driver.page_source

    except Exception as e:
        print(f"Erro ao buscar vagas: {e}")
        return None

def parse_job_listings(page_source):
    try:
        soup = BeautifulSoup(page_source, 'html.parser')
        jobs_list = soup.find('ul', class_="css-zu9cdh eu4oa1w0")

        if jobs_list:
            list_items = jobs_list.find_all('li')
            return [item.get_text() for item in list_items]
        else:
            print("Lista não encontrada.")
            return ["LISTA NÃO ENCONTRADA"]
    except Exception as e:
        print(f"Erro ao parsear HTML: {e}")
        return ["ERRO AO PARSEAR HTML"]

def main():
    url = 'https://www.indeed.com.br/'
    driver = create_chrome_driver()

    if not driver:
        return

    try:
        page_source = fetch_job_listings(driver, url)

        if page_source:
            job_listings = parse_job_listings(page_source)
        else:
            job_listings = ["ERRO AO OBTER FONTES DA PÁGINA"]

        pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vagas.pdf")
        pdf_creator.create_pdf("\n".join(job_listings), pdf_path)

        print(f"PDF criado com sucesso e salvo em {pdf_path}")

    finally:
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
