# -*- coding: utf-8 -*-
import scrapy
from ajk.items import AjkItem
import re
#import random
#from ajk.user_agents import agents
class AjkSpider(scrapy.Spider):
    name='ajk'
    allowed_domains=["anjuke.com"]
   
    def start_requests(self):
        start_urls=["https://xa.anjuke.com/sale/xianzhoubianc/"]
        yield scrapy.Request(url=start_urls[0],callback=self.parse_info, headers={
         'User-Agent': "'Mozilla/5.0'",
          })

    def parse_info(self,response):
        pat=r'>(.*)<'
        a=re.compile(pat)
        b=re.compile(r'i>(.*)<')
        item = AjkItem()
        link=response.xpath(".//div[@class='multi-page']/a[@class='aNxt']/@href").extract_first()
        if link is not None:
            yield scrapy.Request(url=link,callback=self.parse_info,headers={
         'User-Agent': "'Mozilla/5.0'",
          })
        else:
            pass
        for i in response.xpath(".//ul[@id='houselist-mod-new']/li"):
            price=i.xpath("./div[@class='pro-price']/span[1]/strong").extract_first()
            name=i.xpath("./div[@class='house-details']/div[1]/a/@title").extract_first()
            structure=i.xpath("./div[2]/div[2]/span[1]").extract_first()
            area=i.xpath("./div[2]/div[2]/span[2]").extract_first()
            unit_price=i.xpath("./div[3]/span[@class='unit-price']").extract_first()
            rise=i.xpath("./div[2]/div[2]/span[3]").extract_first()
            year=i.xpath("./div[2]/div[2]/span[4]").extract_first()
            owner=i.xpath("./div[2]/div[2]/span[5]").extract_first()
            address=i.xpath("./div[2]/div[3]/span/@title").extract_first()
            
            item['price']=a.search(price).group(1)
            item['name']=name
            item['structure']=a.search(structure).group(1)
            item['area']=a.search(area).group(1)
            item['unit_price']=a.search(unit_price).group(1)
            item['rise']=a.search(rise).group(1)
            item['year']=a.search(year).group(1)  
            item['owner']=b.search(owner).group(1)
            item['address']=address     
            yield item