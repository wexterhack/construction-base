from scrapy.exceptions import DropItem, IgnoreRequest
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider

from ..items import OfferItem


class UralintSpider(SitemapSpider):
    name = 'uralint'
    sitemap_urls = ["https://chel.uralint.ru/sitemap.xml"]
    sitemap_alternate_links = True
    sitemap_rules = [
        ('/catalog/', 'parse'),
    ]

    def parse(self, response, **kwargs):
        if response.xpath('//div[@class="info_item"]').get():
            loader = ItemLoader(OfferItem(), response=response)
            name: str = response.xpath('//h1/text()').get()
            price: str = response.xpath('//div[@class="info_item"]//span[@class="price_value"]/text()').get()
            package: str = response.xpath('//div[@class="info_item"]//span[@class="price_measure"]/text()').get()
            loader.add_value('name', name)
            loader.add_value('price', price, re=r'[\d+,?|.?]')
            loader.add_value('package', package)
            loader.add_value('url', response.url)
            loader.add_value('supplier', 'chel.uralint.ru')
            yield loader.load_item()
        else:
            return DropItem()
