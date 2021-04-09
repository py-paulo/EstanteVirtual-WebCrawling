import pprint
import json

from webcrawling.crawling import WebCrawling

pp = pprint.PrettyPrinter(indent=4, compact=True, width=80)

webcrawl = WebCrawling()

books = webcrawl.crawl('Livraria Progresso Sebo')

with open('progresso.json', 'w') as fp:
    json.dump(books, fp)
