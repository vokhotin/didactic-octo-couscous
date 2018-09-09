import logging
import re
from lxml import html

class Transformer(object):
    def transform_process(self, html_string: str) -> dict:
        # Ожидаемые параметры:
        #   'Название'
        #   'Стоимость'
        #   'Город'
        #   'Описание'
        #   'Услуга'
        #   'Среднемесячная выручка'' \
        #   'Среднемесячные расходы'' \
        #   'Действующий бизнес'
        #   'Возраст бизнеса' \
        #   'Количество сотрудников'' \
        #   'Организационно-правовая форма'
        #   'Доля к продаже'' \
        #   'Причина продажи'
        pattern = re.compile("\d+")
        tree = html.fromstring(html_string)
        parameters = {}
        parameters['Название'] = tree.xpath('//h1[@class="publ-page__title"]/text()')[0]
        try:
            parameters['Стоимость'] = float("".join(re.findall(pattern, tree.xpath('//h2[@class="publ-price__num"]/text()')[0])))
        except:
            parameters['Стоимость'] = tree.xpath('//h2[@class="publ-price__num"]/text()')[0]
        try:
            parameters['Город'] = tree.xpath('//p[@class = "publ__txt"]/text()')[0]
        except:
            parameters['Город'] = ""
        try:
            parameters['Описание'] = tree.xpath('//p[@itemprop = "description"]/text()')[0]
        except:
            parameters['Описание'] = ""
        try:
            parameters['Услуга'] = tree.xpath('//p[@class = "publ__txt m-t15"]/text()')[0]
        except:
            pass
        parameters.update(dict(zip(
                                tree.xpath('//div[@class = "publ-info__key"]/text()'),
                                tree.xpath('//div[@class = "publ-info__value"]/text()')
                                    )))
        try:
            parameters['Возраст бизнеса'] = float("".join(re.findall(pattern, parameters['Возраст бизнеса'])))
        except:
            pass
        try:
            parameters['Количество сотрудников'] = float("".join(re.findall(pattern, parameters['Количество сотрудников'])))
        except:
            pass
        try:
            parameters['Среднемесячная выручка'] = float("".join(re.findall(pattern, parameters['Среднемесячная выручка'])))
        except:
            pass
        try:
            parameters['Среднемесячные расходы'] = float("".join(re.findall(pattern, parameters['Среднемесячные расходы'])))
        except:
            pass

        return parameters

