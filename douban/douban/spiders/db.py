# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

# spider 目录下不能存在相同爬虫名称的文件
class DbSpider(scrapy.Spider):
    name = 'db'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movie_list:
            # item 文件导入
            douban_item = DoubanItem()
            douban_item['serial_number'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()
            for c_item in content:
                # 根据空格分割字符串
                content_s = "".join(c_item.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = item.xpath(".//div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract_first()
            douban_item['descripe'] = item.xpath(".//div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract_first()
            # 你需要将数据 yield 到 pipeline
            yield douban_item
        # 解析下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://movie.douban.com/top250" + next_link, callback=self.parse)
            