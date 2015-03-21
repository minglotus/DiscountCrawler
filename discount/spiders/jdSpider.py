import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from discount.items import DiscountItem
from scrapy.http import Request, Response
import re

def first_element(element_list):
    return element_list[0].strip() if isinstance(element_list, list) and len(element_list) > 0 else None
def last_item(element_list):
    return element_list[-1].strip() if isinstance(element_list, list) and len(element_list) > 0 else None
class JDSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['http://xuan.jd.com/youhui']
    # start_urls = ['http://item.jd.com/1203874.html']
    base_url = 'http://xuan.jd.com'
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('http://xuan.jd.com/youhui/(.*?).html', '/youhui/(.*?).html'), ), callback='parse_item'),

    )



    def parse_item(self, response):
        sel = Selector(response)
        item_entries = sel.xpath('//*[@id="h-zxtj"]/ul/li')
        category = first_element(sel.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/a[3]/text()').extract())
        for entry in item_entries:
            item = DiscountItem()
            item['name'] = first_element(entry.xpath('div[2]/dl/dd/a/text()').extract())
            item['price'] = first_element(entry.xpath('div[1]/a/i/text()').extract())
            item['description'] = first_element(entry.xpath('div[2]/div[2]/text()').extract())
            item['category'] = category
            item['url'] = first_element(entry.xpath('div[2]/div[4]/a[1]/@href').extract())
            item['imgsrc'] = first_element(entry.xpath('div[1]/a/img/@data-lazyload').extract())
            item['discount'] = first_element(entry.xpath('div[2]/dl/dd/a/span/text()').extract())
            yield item
        pages = sel.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[7]/div/a/@href').extract()
        nextpage = last_item(pages)
        if (nextpage):
            yield Request(self.base_url + nextpage)


