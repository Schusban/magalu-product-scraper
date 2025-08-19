# 🛒 Magalu Scraper & Análise de Produtos

Este projeto é uma ferramenta de **web scraping** que pesquisa produtos no **Magazine Luiza**, coleta informações como título, preço, avaliação e link do produto, e gera automaticamente uma **planilha Excel** com análises e ranking dos **Top 3 produtos**. Além disso, cria um gráfico de preço x avaliação para auxiliar na tomada de decisão.

---

## ✨ Funcionalidades

- Pesquisa produtos por palavra-chave (ex.: "TV", "abacate", etc.)
- Extrai informações detalhadas dos produtos:
  - Título
  - Preço
  - Nota de avaliação
  - Quantidade de avaliações
  - Link do produto
- Gera uma planilha Excel (`Produtos.xlsx`) contendo:
  - Dados brutos de todos os produtos
  - Tabela Top 3 produtos recomendados baseada em **score estatístico**
  - Gráfico visual de preço vs avaliação
- Calcula um **score ponderado** considerando:
  - Nota de avaliação (50%)
  - Quantidade de avaliações (30%)
  - Preço (20%, favorecendo produtos mais baratos)

---

## 🛠️ Pré-requisitos

Antes de rodar o projeto, você precisa ter:

1. **Python 3.10+**
2. **Google Chrome** instalado
---

## 📦 Instalação das dependências

Instale as bibliotecas Python necessárias:

```bash
pip install selenium pandas openpyxl matplotlib
```
## 🚀 Como usar

1. Clone o repositório:

```bash
git clone https://github.com/Schusban/magalu-product-scraper.git
cd magalu-product-scraper
```

2. Execute o script principal:

```bash
python main.py
```

3. Digite o produto que deseja pesquisar quando solicitado:
```bash
Digite o produto que deseja pesquisar: TV
```

4. Aguarde enquanto os dados são coletados e analisados.

5. Ao final, você terá:

    - Produtos.xlsx com os dados e análise

    - Gráfico de preço x avaliação inserido na planilha

---

🧠 Como funciona o score dos produtos

O score final é calculado assim:

    - Nota do produto: 50% do peso (normalizada de 0 a 1)
    - Quantidade de avaliações: 30% do peso (normalizada de 0 a 1)
    - Preço: 20% do peso (normalizado invertido, produtos mais baratos recebem maior pontuação)
    
O score é então escalado de 0 a 10.
