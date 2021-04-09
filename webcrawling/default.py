DEFAULT_HEADERS: dict = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applica'
    'tion/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.estantevirtual.com.br/livreiros/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/'
    '537.36'
}
DEFAULT_URL_BASE: str = 'https://www.estantevirtual.com.br'
DEFAULT_WAIT_REQUEST: int = 1
DEFAULT_FILTER_BY_ATTRS: list = ['bookName', 'author', 'releaseYear', 'publishingCompany', 'type', 'weight']
DEFAULT_OFFSET: int = 1


class Language:

    PORTUGUESE: str = 'Portugu%C3%AAs'
