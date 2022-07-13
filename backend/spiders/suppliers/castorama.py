from scrapy.exceptions import DropItem
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider

from ..items import OfferItem


class CastoramaSpider(SitemapSpider):
    name = 'uralint'
    sitemap_urls = ["https://www.castorama.ru/sitemap.xml"]
    sitemap_alternate_links = True
    sitemap_rules = [
        ('/', 'parse'),
    ]

    def parse(self, response, **kwargs):
        if response.xpath('//div[contains(@class, "product-essential")]'):
            loader = ItemLoader(OfferItem(), response=response)
            name: str = response.xpath('//h1[contains(@class, "product-essential__name")]/text()').get()
            price: str = response.xpath('//div[contains(@class, "add-to-cart__price")]//span[@class="price"]/span/span[1]/text()').get()
            package: str = 'ШТ'
            loader.add_value('name', name)
            loader.add_value('price', price, re=r'[\d+,?|.?]')
            loader.add_value('package', package)
            loader.add_value('url', response.url)
            loader.add_value('supplier', 'www.castorama.ru')
            yield loader.load_item()
        else:
            return DropItem
