import pandas as pd

def criar_planilha(df):
    """
    Esta função cria uma planilha Excel com os dados dos produtos fornecidos em um DataFrame.

    Parâmetros:
    df (pandas.DataFrame): DataFrame contendo os produtos a serem salvos. Espera-se que tenha colunas como
        "TITULO", "PRECO", "URL", "NOTA_AVAL" e "QTD_AVAL".

    Retorna:
    str: O nome do arquivo Excel criado ("Produtos.xlsx").  
    """

    nome_arquivo = "Produtos.xlsx"
    try:
        df.to_excel(nome_arquivo, index=False)
        print(f"Planilha '{nome_arquivo}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar a planilha: {e}")

    return nome_arquivo 