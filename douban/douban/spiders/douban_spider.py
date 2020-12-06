import time

import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口 URL,写入到调用中
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_name'] = item.xpath(".//div[@class='item']//em//text()").extract_first()
            douban_item['movie_name'] = item.xpath(
                ".//div[@class='info']//div[@class='hd']//span[@class='title']//text()").extract_first()
            intorduce = item.xpath(".//div[@class='info']//div[@class='bd']//p[1]//text()").extract()
            for i in intorduce:
                douban_item['intorduce'] = "".join(i.split())
            douban_item['start'] = item.xpath(".//span[@class='rating_num']//text()").extract_first()
            douban_item['evaluate'] = item.xpath(".//div[@class='star']//span[4]//text()").extract_first()
            douban_item['describe'] = item.xpath(
                ".//div[@class='bd']//p[@class='quote']//span[@class='inq']//text()").extract_first()
            yield douban_item

        next_link = response.xpath("//span[@class='next']//link//@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)

        time.sleep(1)
