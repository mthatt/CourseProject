import scrapy
from scrapy.exceptions import CloseSpider

class CoinBaseSpider(scrapy.Spider):
    name = "coinBase"
    #allowed_domains = ["coinmarketcap.com"]

    count = 0
    N = 0

    def __init__(self, pages = 1, urlInput=None, *args, **kwargs):
        super(CoinBaseSpider, self).__init__(*args, **kwargs)
        self.N = pages
        self.urlInput = "https://coinmarketcap.com/all/views/all/"

    def start_requests(self):
        urls = [
            self.urlInput,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        title = response.css('div.sc-1kxikfi-0.fjclfm.cmc-table__column-name a.cmc-link::text').extract()
        print(title)
        ticker = response.css('tr.cmc-table-row td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--left.cmc-table__cell--sort-by__symbol>div::text').extract()
        print(ticker)