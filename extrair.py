from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extrair_dados(driver):
    """
    Esta função extrai os dados dos produtos exibidos no site Magalu a partir de um driver Selenium.

    Parâmetros:
    driver (webdriver): Instância do Selenium WebDriver que já está com a página de resultados carregada.

    Retorna:
    pandas.DataFrame ou None: Retorna um DataFrame contendo os campos:
        - "TITULO": título do produto
        - "PRECO": preço do produto (como string)
        - "URL": link do produto
        - "NOTA_AVAL": nota de avaliação (float)
        - "QTD_AVAL": quantidade de avaliações (int)
    Retorna None se nenhum produto for encontrado.
    """
      
    products = []

    # Espera até que os cards de produtos estejam carregados
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-testid="product-card-container"]'))
    )

    cards = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="product-card-container"]')

    for card in cards:
        try:
            # Título
            try:
                title = card.find_element(By.CSS_SELECTOR, 'h2[data-testid="product-title"]').text.strip()
            except:
                continue  # pula cards sem título

            # Link
            try:
                url = card.get_attribute("href")
                if not url:
                    continue  # pula cards sem link
            except:
                continue

            # Preço
            try:
                preco_texto = card.find_element(By.CSS_SELECTOR, 'p[data-testid="price-value"]').text
                # Pega só o primeiro valor válido
                preco = preco_texto.split('\n')[0].replace('ou ', '').strip()
            except:
                preco = "Não informado"

            # Avaliações
            try:
                review_text = card.find_element(By.CSS_SELECTOR, 'div[data-testid="review"] span').text  # "5.0 (37)"
                note = float(review_text.split(' ')[0].replace(',', '.'))
                qtd = int(review_text.split('(')[1].replace(')', ''))
            except:
                note = 0.0
                qtd = 0

            # Só adiciona produtos que têm título e link
            products.append({
                "TITULO": title,
                "PRECO": preco,
                "URL": url,
                "NOTA_AVAL": note,
                "QTD_AVAL": qtd
            })

        except Exception as e:
            print(f"Erro ao processar um card: {e}")
            continue

    df = pd.DataFrame(products)

    if df.empty:
        print("Nenhum produto encontrado!")
        return None

    return df
