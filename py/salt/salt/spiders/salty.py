import scrapy
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


def SaltySpider(Spider):
	name="salty"
	allowed_domains=['saltybet.com']
	start_urls=['http://www.saltybet.com/bank']
	rules=[Rule(LinkExtractor(allow=['/bank?page=\d+']),'parse_torrent')]
	def parse_torrent(self,response):
		item=Fight()
		item['place']=response.xpath('//tr/td[0]').extract()
		item['name']=response.xpath('//tr/td[2]').extract()
		item['money']=response.xpath('//tr/td[3]').extract()
		return item

