import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagen = sopa.select('.course-box-image')[0]['src']

for i in imagen:
    print(i)

print(imagen)

imagen_curso= requests.get(imagen)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()