import logging
import requests
from lxml import html

logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        # You can iterate over ids, or get list of objects
        # from any API, or iterate throught pages of any site
        # Do not forget to skip already gathered data
        # Here is an example for you
        url = 'https://kinokopilka.tv'
        response = requests.get(url, verify=False)
        tree = html.fromstring(response.text)
        films_urls = []
        for div_node in tree.xpath('//div[@class="movie"]'):
            films_urls.append(f"{url}{div_node.xpath('.//a/@href')[0]}")


        # if not response.ok:
        #     logger.error(response.text)
        #     # then continue process, or retry, or fix your code
        #
        # else:
        #     # Note: here json can be used as response.json
        #     data = response.text
        #
        #     # save scrapped objects here
        #     # you can save url to identify already scrapped objects
        #     storage.write_data([url + '\t' + data.replace('\n', '')])
