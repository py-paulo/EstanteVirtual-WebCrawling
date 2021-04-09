import urllib.request
import pprint
import json

from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4, compact=True, width=80)

uri_base = 'https://www.estantevirtual.com.br'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applica'
    'tion/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.estantevirtual.com.br/livreiros/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/'
    '537.36'
}
livraria = 'Livraria Progresso Sebo'.lower().replace(' ', '')
query = '/livreiros/'+livraria+'?offset=1&idioma=Portugu%C3%AAs'
req = urllib.request.Request(uri_base+query,
                             headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8', errors='ignore')

# with open('example.html', 'w') as fp:
#     fp.write(html)

# with open('example.html') as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup(html, 'html.parser')
books = []
count = 0
last_page = query

while True:
    for div in soup.find_all("div", {"class": "info-exemplar"}):
        h2_book_name = div.find("h2", {"itemprop": "name"})
        book_name = h2_book_name.attrs['data-enhanced-ecommerce-impression-name']

        span_author = div.find("span", {"itemprop": "author"})
        author = span_author.attrs['data-enhanced-ecommerce-impression-brand']
        
        div_sub_info = div.find("div", {"class": "sub-info"})

        div_year_editor = div_sub_info.find("div", {"class": "ano-editora"})
        span_year_editor = div_year_editor.findChildren("span", recursive=False)[0]
        year_editor = span_year_editor.text.split(':')[-1].strip()

        div_publishing_company = div_sub_info.find("div", {"class": "nome-editora"})
        span_publishing_company = div_publishing_company.findChildren("span", recursive=False)[0]
        publishing_company = span_publishing_company.text.split(':')[-1].strip()

        div_type = div_sub_info.find("span", {"class": "info-exemplar-tipo_peso"})
        type_book, weight_book = [text.strip().split(':')[-1].strip() for text in div_type.text.split('\n')]

        book = {
            'name': book_name,
            'author': author,
            'release_year': year_editor,
            'publishing_company': publishing_company,
            'type': type_book,
            'weight': weight_book
        }
        count += 1
        print('total: %d' % count)
        pp.pprint(book)
        books.append(book)

    try:
        next_page = soup.find_all("a", {"class": "next"})[0].attrs['href']
    except (IndexError, KeyError):
        next_page = None

    if (next_page == last_page) or (next_page is None): break
    else: last_page = next

    if next_page:
        print('next page: %s' % next_page)

        req = urllib.request.Request(uri_base + next_page, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')

        soup = BeautifulSoup(html, 'html.parser')
    else:
        break

json.dump(books, open(livraria, 'w'))
