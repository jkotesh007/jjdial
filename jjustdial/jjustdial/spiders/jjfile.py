import scrapy
from w3lib.html import remove_tags


class jjspider(scrapy.Spider):
    name = 'johnsonspider'
    start_urls = ['https://www.justdial.com/Hyderabad/Textile-Manufacturers/nct-10477448']

    def parse(self, response):
        def rem(value):
            def wget(i):
                switcher = {
                    'mobilesv icon-acb': '0',
                    'mobilesv icon-yz': '1',
                    'mobilesv icon-wx': '2',
                    'mobilesv icon-vu': '3',
                    'mobilesv icon-ts': '4',
                    'mobilesv icon-rq': '5',
                    'mobilesv icon-po': '6',
                    'mobilesv icon-nm': '7',
                    'mobilesv icon-lk': '8',
                    'mobilesv icon-ji': '9',
                    'mobilesv icon-fe': '(',
                    'mobilesv icon-hg': ')',
                    'mobilesv icon-ba': '-',
                    'mobilesv icon-dc': '+',
                }
                return switcher.get(i, default='')
            for valu in value:
                return wget(valu)




        for quote in response.selector.xpath('//li[@class="cntanr"]'):
            yield {
                'text': quote.xpath('.//span[@class="lng_cont_name"]/text()').extract_first(),
                'rating': quote.xpath('.//span[@class="green-box"]/text()').extract_first(),
                'address': quote.xpath('.//span[@class="cont_fl_addr"]/text()').extract_first(),
                'tags': quote.xpath('.//span[@class="margin0 addrinftxt"]/a/text()').extract(),
                'contno': quote.xpath('.//p[@class="contact-info "]/span/a/span/@class').extract()

            }
        next_page=response.selector.xpath("//a[@rel='next']/@href").extract_first()
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
