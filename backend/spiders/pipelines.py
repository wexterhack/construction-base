# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import requests
import logging
from .items import OfferItem


class OfferPipeline:
    def __init__(self):
        self.session = None

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        try:
            data = {
                'name': item.name[0],
                'supplier': 'http://127.0.0.1:8000/api/suppliers/1/',
                'url': item.url[0]
            }
            response = requests.post('http://127.0.0.1:8000/api/offers/', json=data)
            if response.status_code == 201:
                offer = response.json()
                logging.debug(offer)
                requests.post('http://127.0.0.1:8000/api/prices/', data={
                    'offer': f'http://127.0.0.1:8000/api/offers/{offer["id"]}/',
                    'amount': item.price[0] if item.price else 0
                })
        except Exception as e:
            print(e)
        return item

    def close_spider(self, spider):
        pass
