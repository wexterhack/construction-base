import scrapy.http
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider

from ..items import OfferItem


class SDvorSpider(SitemapSpider):
    username = 'sonicpark'
    password = 'vfrcbvec'

    def parse(self, response, **kwargs):
        loader = ItemLoader(OfferItem(), response=response)
        name: str = response.xpath('//h1/text()').get()
        price: str = response.xpath('normalize-space(//div[@class="product-price"]//div[@class="price"]//text())').get()
        package: str = response.xpath('normalize-space(//div[@class="product-price"]//div[@class="text"]//text())').get()
        loader.add_value('name', name)
        loader.add_value('price', price, re='\d+')
        loader.add_value('package', package)
        loader.add_value('url', response.url)
        loader.add_value('supplier', 'www.sdvor.com')
        yield loader.load_item()

    name = 'sdvor'
    sitemap_urls = ["https://www.sdvor.com/sitemaps.xml"]
    sitemap_alternate_links = True
    sitemap_rules = [
        ('/chelyabinsk/product/', 'parse'),
    ]
