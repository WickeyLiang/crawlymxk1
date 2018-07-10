#coding=utf-8
import scrapy
import json


class GamerskySpider(scrapy.Spider):
    name = 'gamersky'
    allowed_domains = ['ku.gamersky.com']
    start_urls = ["http://ku.gamersky.com/SearchGameLibAjax.aspx?jsondata={rootNodeId:20039,pageIndex:"+str(i+1)+",pageSize:36,sort:'00'}" for i in range(376)]

    def __init__(self, totalpage=10, *args, **kwargs):
        super(GamerskySpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://ku.gamersky.com/SearchGameLibAjax.aspx?jsondata={rootNodeId:20039,pageIndex:"+str(i+1)+",pageSize:36,sort:'00'}" for i in range(int(totalpage))]

    def parse(self, response):
        gg = response.body_as_unicode()
        jsonobj = json.loads(gg[1:-2])

        res = jsonobj['result']

        for article in res:
            url = article['itemUrl']

            request = scrapy.Request(url, callback=self.blogParse)
            item = dict()

            request.meta['item'] = item
            yield request


    def blogParse(self, response):
        item = response.meta['item']
        item['cnName'] = response.css('.tit_CH::text').extract_first()
        item['enName'] = response.css('.tit_EN::text').extract_first()
        item['cover'] = response.css('.YXXX-L a img::attr(src)').extract()
        item['platform'] = response.css('.win a::text').extract()
        item['producer'] = response.css('.div3 .tt2 .txt::text').extract()
        item['type'] = response.css('.div3 .tt2 .tag a::text').extract()
        item['publishTime'] = response.css('.win a::attr(data-time)').extract()
        item['introduce'] = response.css('.con-hide p::text').extract()

        yield item