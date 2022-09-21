import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())
print(sopa.select('h1'))


resultado2= requests.get('https://escueladirecta-blog.blogspot.com/2022/09/la-forma-correcta-de-importar-librerias.html')
sopa2= bs4.BeautifulSoup(resultado2.text, 'lxml')

parrafo_especial =  sopa2.select('p')
print(parrafo_especial)


