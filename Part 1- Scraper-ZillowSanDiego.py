# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.loader import ItemLoader
from zillow2.utils import URL, cookie_parser, parse_new_url
from ..items import Zillow2Item


#Handling Captcha
#In Settings(My User Agent, Robotstxtobey=False, Download_Delay to wait until download response)


class ZillowsandiegoSpider(scrapy.Spider):
    #Spider name
    name = 'ZillowSanDiego'
    allowed_domains = ['www.zillow.com']
    
    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookie_parser(),
            meta={
                'currentPage':1
            }
        )

    def parse(self, response):
        current_page=response.meta['currentPage']

        #print(response.body)

        #json will convert it to python dictionary
        json_resp=json.loads(response.body)
        #Looping through the results
        houses= json_resp.get('searchResults').get('listResults')
        for house in houses:
            #Inherit from items.py file
            #instantiate ItemLoader class
            #documentation: https://docs.scrapy.org/en/latest/topics/loaders.html
            loader=ItemLoader(item=Zillow2Item())
            loader.add_value('addressCity', house.get('addressCity'))
            loader.add_value('addressState', house.get('addressState'))
            loader.add_value('price', house.get('price'))
            loader.add_value('baths', house.get('baths'))
            loader.add_value('beds', house.get('beds'))
            loader.add_value('latitude', house.get('latLong').get('latitude'))
            loader.add_value('longitude', house.get('latLong').get('longitude'))
            loader.add_value('area', house.get('area'))
            yield loader.load_item()

        
        #Pagination
        #we have 20 pages of 20
        total_pages=json_resp.get('searchList').get('totalPages')
        #Return next page if available
        if current_page <= total_pages:
            current_page+=1
            #Request to next page
            yield scrapy.Request(
                url=parse_new_url(URL, page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(),
                meta={
                    'currentPage': current_page
                }
            )
