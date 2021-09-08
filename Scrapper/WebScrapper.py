from bs4 import BeautifulSoup

import requests
# objeto site esta recebento dodo o conteudo da requisição http do site climatempo
site = requests.get('https://climatempo.com.br/').content
# objeto soup esta baixando o html do site climatempo
soup = BeautifulSoup(site, 'html.parser')
# o print esta transformando o html em string e o exibindo na tela
print(soup.prettify())

# temperatura = soup.find("span", class_="_margin-l-10 _margin-r-5")
# print(temperatura.string)

print(soup.title.string)