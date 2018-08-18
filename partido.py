import requests
from bs4 import BeautifulSoup
html = requests.get('http://meucongressonacional.com/lavajato/partidos').text
soup = BeautifulSoup(html, 'html.parser')
print('Abaixo estão os valores doados aos partidos. Dados da operação: "lava-jato" ')
for content in soup.select('tr'): #Mostra o conteúdo na <td>
    print(content.text)
