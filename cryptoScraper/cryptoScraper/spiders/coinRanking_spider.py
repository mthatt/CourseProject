import scrapy
from scrapy.exceptions import CloseSpider

class CoinRankingSpider(scrapy.Spider):
    name = "coinRanking"
    #allowed_domains = ["coinmarketcap.com"]

    count = 0
    N = 0

    def __init__(self, pages = 1, urlInput=None, *args, **kwargs):
        super(CoinRankingSpider, self).__init__(*args, **kwargs)
        self.N = pages
        self.urlInput = "https://coinranking.com/"

    def start_requests(self):
        urls = [
            self.urlInput,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        title = response.css('div.profile.profile--light a.profile__link::text').extract()
        print(title.strip("n"))
        # ticker = response.css('tr.cmc-table-row td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--left.cmc-table__cell--sort-by__symbol>div::text').extract()
        # print(ticker)