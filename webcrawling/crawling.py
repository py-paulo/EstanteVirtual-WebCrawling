from .crawl import _crawl

from .default import Language
from .default import (
    DEFAULT_HEADERS, DEFAULT_URL_BASE, DEFAULT_WAIT_REQUEST, DEFAULT_FILTER_BY_ATTRS, DEFAULT_OFFSET)


class WebCrawling:

    def crawl(
            self,
            bookStore: str,
            urlBase: str = DEFAULT_URL_BASE,
            offset: int = DEFAULT_OFFSET,
            language: str = Language.PORTUGUESE,
            headers: dict = DEFAULT_HEADERS,
            waitRequests: int = DEFAULT_WAIT_REQUEST,
            attrs: list = DEFAULT_FILTER_BY_ATTRS):

        bookStore = bookStore.lower().replace(' ', '')
        query = '/livreiros/'+bookStore+'?offset='+str(offset)+'&idioma='+language

        return _crawl(urlBase, query, headers, waitRequests, attrs)
