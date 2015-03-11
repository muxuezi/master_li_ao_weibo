import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['tw.weibo.com']
    start_urls = ["http://tw.weibo.com/2134671703/p/{}".format(n) for n in xrange(1,40)]

    def parse(self, response):
        # filename = response.url.split('/')[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.css('.div_shadow')[3:]:
            item = DmozItem()
            item['title'] = sel.xpath('.//div/p/a/@title').extract()
            item['date'] = sel.xpath('.//span/label/text()').extract()
            # item['link'] = sel.xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            # print title, link, desc
            yield item