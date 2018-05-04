# -*- coding: utf-8 -*-
import scrapy
from medicine.items import MedicineItem


class MedicineSpider(scrapy.Spider):
    name = "medicine"
    allowed_domains = ["yaofang.cn"]
    start_urls = ["http://www.yaofang.cn/c/channel/index/cjjb"]
    def parse(self, response):
        htmlist = response.xpath('//ul[@class="symptom-ul"]/li/a/@href')
        for li in htmlist:
            print li
            link = li.extract()
            print link
            yield scrapy.Request(link,callback=self.parse_dir_content)
            

    def parse_dir_content(self,response):
        link_next = response.xpath('//div[@class="paging"]/p/a/@href')
        if(len(link_next)==0):
            item = MedicineItem()
            item['illness'] = response.xpath("//div[@class='selectTitle']/i/text()").extract()
            item['name'] = response.xpath("//div[@class='drug_item']/a/text()").extract()
            #print item['illness'][0]
            #print item['name'][0]
            #file.write(str(item['name'][0]).decode('utf-8'))
            yield item
        else:
            for li in link_next:
                print li
                link = li.extract()
                print link
                yield scrapy.Request(link,callback=self.parse_dir_content_havpage)

    def parse_dir_content_havpage(self,response):
        item = MedicineItem()
        item['illness'] = response.xpath("//div[@class='selectTitle']/i/text()").extract()
        item['name'] = response.xpath("//div[@class='drug_item']/a/text()").extract()
        #print item['illness'][0]
        #print item['name'][0]
        #file.write(str(item['name'][0]).decode('utf-8'))
        yield item
