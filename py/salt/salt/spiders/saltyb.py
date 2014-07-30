# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class SaltybSpider(scrapy.Spider):
	name = "saltyb"
	allowed_domains = ["saltybet.com"]
	start_urls = ( 'http://www.saltybet.com/bank', )
	rules=[Rule(LinkExtractor(allow=['/bank?page=\d+']),'parse_torrent')]
	def parse_torrent(self,response):
		item=SaltItem()
		item['place']=response.xpath('//tr[0]/td[0]').extract()
		item['name']=response.xpath('//tr[0]/td[2]').extract()
		item['money']=response.xpath('//tr[0]/td[3]').extract()
		return item