import urllib.request
from bs4 import BeautifulSoup


def _crawl(urlBase, query, headers, waitRequests, attrs, allBooks: list = []):
    req = urllib.request.Request(urlBase+query, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')

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
        allBooks.append(book)

    try:
        nextQuery = soup.find_all("a", {"class": "next"})[0].attrs['href']
    except (IndexError, KeyError):
        nextQuery = None

    if (query == nextQuery) or (nextQuery is None):
        return allBooks
    else:
        print(nextQuery)
        _crawl(urlBase, nextQuery, headers, waitRequests, attrs, allBooks)
