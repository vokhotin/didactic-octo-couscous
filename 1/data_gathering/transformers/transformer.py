import logging
from lxml import html

class Transformer(object):
    def transform_process(self, html_string):
        tree = html.fromstring(html_string)

        raiting = tree.xpath('//span/text()')
        # ganre = tree.xpath('/html/body/div[2]/span/div[1]/div/div[2]/ul/li[1]')
        print (raiting)