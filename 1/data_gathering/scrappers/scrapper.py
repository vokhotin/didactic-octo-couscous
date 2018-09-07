import logging
import requests
import time
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
        html_page = html.fromstring(response.text)
        for div_node in html_page.xpath('//div[@class="movie"]'):
            film_url = f"{url}{div_node.xpath('.//a/@href')[0]}"
            response = requests.get(film_url, verify=False)
            data = response.text
            while '\n' in data:
                data.replace('\n', ' ')
            # storage.append_data(["".join(data.split('\n'))])
                storage.append_data([data])
            del film_url
            del response
            del data
            time.sleep(0.3)

        del html_page


