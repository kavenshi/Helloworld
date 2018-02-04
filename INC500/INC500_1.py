"""kavenstone"""
"""Download json string form INC500 website"""

import scrapy
import json
from bs4 import BeautifulSoup

Json_respone = str()

class INC500_1(scrapy.Spider):
    name = 'INC500_1'
    url = "https://www.inc.com/inc5000list/json/inc5000_2017.json"

    def start_requests(self):
        yield self.scrapy_requester.scrapy_requests(self.target_url,self.callback_parse)