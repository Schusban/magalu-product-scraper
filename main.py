from inicializar_site import abrir_site_magalu, pesquisar_produto
from extrair import extrair_dados
from excel import criar_planilha
from analise import analisar_produtos

def main():
    """
    Esta função coordena o processo de pesquisa de produtos no site Magalu,
    extração de dados, criação de planilha Excel e análise dos produtos.

    Fluxo:
    1. Solicita ao usuário o produto a ser pesquisado.
    2. Abre o navegador e acessa o site Magalu.
    3. Pesquisa o produto informado.
    4. Extrai os dados dos produtos encontrados.
    5. Cria uma planilha Excel com os dados.
    6. Executa a análise do top 3 produtos com base em score.
    
    Parâmetros:
    Nenhum
    
    Retorna:
    None
    """

    # Solicita ao usuário o produto a ser pesquisado
    produto = input("Digite o produto que deseja pesquisar: ").strip()
    if not produto:
        print("❌ Produto não informado. Encerrando o programa.")
        return

    # Inicializa o navegador
    browser = abrir_site_magalu()
    if not browser:
        print("❌ Não foi possível abrir o site. Encerrando o programa.")
        return

    # Pesquisa o produto
    pesquisar_produto(browser, produto)
    df_produtos = extrair_dados(browser)

    if df_produtos is not None and not df_produtos.empty:
        arquivo_excel = criar_planilha(df_produtos)
        
        # 🚀 Roda análise logo após salvar os dados
        analisar_produtos(arquivo_excel)

        print(f"✅ Pesquisa e análise concluídas! Resultados salvos em {arquivo_excel}")
        browser.quit()
    else:
        print(f"❌ Nenhum dado encontrado para o produto '{produto}'.")
        browser.quit()

if __name__ == "__main__":
    main()
