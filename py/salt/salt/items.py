# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SaltItem(scrapy.Item):
	place=scrapy.Field()
	name=scrapy.Field()
	money=scrapy.Field()
