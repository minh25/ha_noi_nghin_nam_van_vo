import scrapy


class NomSpider(scrapy.Spider):
    name = 'nom'
    start_urls = [
        'https://hvdic.thivien.net/pop-nom',
    ]

    def parse(self, response):
        for chu_nom in response.xpath('//a[@class="hv-word-item"]'):
            yield {
                # 'href': 'https://hvdic.thivien.net' + chu_nom.xpath('@href').get(),
                'text': chu_nom.xpath('span/text()').get(),
                'mean': chu_nom.xpath('@data-tippy-content').get().split(', ')[0],
            }
