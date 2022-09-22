import bs4
import requests

resultado = requests.get('http://10.76.16.166/pandora_console/index.php?sec=gmodule_library&sec2=godmode/module_library/module_library_view')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

colunma= sopa.select('.library_main p')


print(colunma)
