from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

def abrir_site_magalu():
    """
    Esta função abre o site do Magazine Luiza utilizando Selenium WebDriver, garantindo que a página
    carregue corretamente antes de retornar o driver.

    Parâmetros:
    Nenhum.

    Retorna:
    webdriver.Chrome ou None: Retorna uma instância do Selenium WebDriver caso a página seja carregada
        com sucesso; caso contrário, retorna None após 3 tentativas.
    """

    attempts = 3
    driver = None
    while attempts > 0:
        try:
 # Configurações do Selenium WebDriver
            chrome_options = Options()
            chrome_options.add_argument("--disable-web-security")  # Desabilitar a segurança SSL.
            chrome_options.add_argument("--ignore-certificate-errors")  # Ignorar erros de SSL.

            driver = webdriver.Chrome(options=chrome_options)            
            driver.get("https://www.magazineluiza.com.br/")
            WebDriverWait(driver, 10).until(
                EC.title_contains("Magazine Luiza")
            )
            print("Site carregado com sucesso!")
            return driver
        except Exception as e:
            print(f"Erro ao carregar o site: {e}")
            attempts -= 1
            print(f"Tentando novamente... {attempts} tentativas restantes.")
            time.sleep(2)
    return None

def pesquisar_produto(driver, search_term):
    """
    Esta função realiza uma pesquisa de produtos no site do Magazine Luiza utilizando o WebDriver fornecido.

    Parâmetros:
    driver (webdriver.Chrome): Instância do Selenium WebDriver previamente inicializada.
    search_term (str): Termo que será buscado no site, como "TV", "Celular", etc.

    Retorna:
    None: A função realiza a busca e aguarda o carregamento dos produtos na página.
    """

    try:
        search_field = driver.find_element(By.ID, "input-search")
        search_field.clear()
        search_field.send_keys(search_term)
        search_field.submit()
        
        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[data-testid="image"]'))
        )
        print("Produtos carregados!")
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao realizar a busca: {e}")