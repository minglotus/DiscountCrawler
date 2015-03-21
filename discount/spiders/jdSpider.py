# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from discount.items import DiscountItem
from scrapy.http import Request, Response
import re


def first_element(element_list):
    return element_list[0].strip() if isinstance(element_list, list) and len(element_list) > 0 else None


def last_element(element_list):
    return element_list[-1].strip() if isinstance(element_list, list) and len(element_list) > 0 else None


class JDSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['http://xuan.jd.com/youhui', 'http://xuan.jd.com/pianyi']
    # start_urls = ['http://item.jd.com/1203874.html']
    base_url = 'http://xuan.jd.com'
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('http://xuan.jd.com/youhui/(.*?).html', '/youhui/(.*?).html'), ),
             callback='parse_youhui'),
        Rule(LinkExtractor(allow=('http://xuan.jd.com/pianyi/(.*?).html', '/pianyi/(.*?).html'), ),
             callback='parse_pianyi'),

    )


    def parse_youhui(self, response):
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
            item['url'] = self.base_url + item['url'] if item['url'].startswith('/') else item['url']
            item['imgsrc'] = first_element(entry.xpath('div[1]/a/img/@data-lazyload').extract())
            item['discount'] = first_element(entry.xpath('div[2]/dl/dd/a/span/text()').extract())
            item['source'] = u'京东京选/优惠'
            yield item
        pages = sel.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[7]/div/a/@href').extract()
        nextpage = last_element(pages)
        if (nextpage):
            yield Request(self.base_url + nextpage)

    def parse_pianyi(self, response):
        sel = Selector(response)
        latest_entries = sel.xpath('//*[@id="latestO"]/ul/li')
        category = first_element(
            sel.xpath('//li[@class="content-youhui-banner-list-item  yact "]/a/span/text()').extract())
        for entry in latest_entries:
            item = DiscountItem()
            item['name'] = first_element(entry.xpath('div[3]/h4/a/text()').extract())
            item['price'] = first_element(entry.xpath('div[3]/p[2]/span/text()').extract()) + \
                            first_element(entry.xpath('div[3]/p[2]/strong/text()').extract())
            item['description'] = first_element(entry.xpath('div[3]/p[1]/text()').extract())
            item['category'] = category
            item['url'] = first_element(entry.xpath('div[3]/h4/a/@href').extract())
            item['imgsrc'] = first_element(entry.xpath('div[2]/a/img/@data-lazyload').extract())
            item['discount'] = first_element(entry.xpath('div[1]/p/b/text()').extract()) + \
                               first_element(entry.xpath('div[1]/p/b/b/text()').extract())
            item['source'] = u'京东京选/便宜'
            yield item
        pages = sel.xpath('//*[@id="latestO"]/div/div/a/@href').extract()
        nextpage = last_element(pages)
        if (nextpage):
            yield Request(self.base_url + nextpage)