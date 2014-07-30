# -*- coding: utf-8 -*-
import scrapy


class ManSpider(scrapy.Spider):
    name = "man"
    allowed_domains = ["google.com"]
    start_urls = (
        'http://www.google.com/',
    )

    def parse(self, response):
        pass
