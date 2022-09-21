import bs4
import requests

url_base ='http://books.toscrape.com/catalogue/page-{}.html'
"""
for n in range(1,11):
    print(url_base.format(n))"""
resultado = requests.get(url_base.format('1'))

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = (sopa.select('.product_pod'))
#Cantidad de Estrella
ejemplo = libros[0].select('.star-rating.Four')
#Titulo del libro
ejemplo2 = libros[0].select('a')[1]['title']




