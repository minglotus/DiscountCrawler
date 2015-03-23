# -*- coding: utf-8 -*-

# Scrapy settings for discount project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'discount'

SPIDER_MODULES = ['discount.spiders']
NEWSPIDER_MODULE = 'discount.spiders'
ITEM_PIPELINES = ['discount.pipelines.JsonWithEncodingPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'discount (+http://www.yourdomain.com)'
