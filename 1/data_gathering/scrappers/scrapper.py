import logging
import requests
import time
from lxml import html

logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def _get_urls(self, html_page) -> str:
        for href in html_page.xpath('//div[@class="obj__center"]/a/@href'):
            yield href

    def scrap_process(self, storage):

        # You can iterate over ids, or get list of objects
        # from any API, or iterate throught pages of any site
        # Do not forget to skip already gathered data
        # Here is an example for you
        url = 'https://www.beboss.ru/business/search'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        urls_list = []
        tries = 0
        for page in range(1, 211):
            if tries == 100:
                break
            response = requests.get("{}?page={}".format(url, page), headers=headers, verify=False)
            if response.ok:
                html_page = html.fromstring(response.text)
                urls_list.extend(self._get_urls(html_page))
                time.sleep(0.3)
            else:
                logging.info("")
                tries += 1
            if page == 2:
                break
        logging.info("Ссылок страниц: {}".format(len(urls_list)))
        for gathered_url in urls_list:
            response = requests.get(gathered_url, headers=headers, verify=False)
            storage.append_data(['start_page\n{}\nend_page'.format(response.text)])
            time.sleep(0.3)




