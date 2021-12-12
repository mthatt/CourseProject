import scrapy
from scrapy.exceptions import CloseSpider

class YahooFinanceSpider(scrapy.Spider):
    name = "yahooFinance"
    #allowed_domains = ["coinmarketcap.com"]

    count = 0
    N = 0

    def __init__(self, pages = 1, urlInput=None, *args, **kwargs):
        super(YahooFinanceSpider, self).__init__(*args, **kwargs)
        self.N = pages
        self.urlInput = "https://finance.yahoo.com/cryptocurrencies"

    def start_requests(self):
        urls = [
            self.urlInput,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        title = response.css('tr.simpTblRow.Bgc($hoverBgColor):h.BdB Bdbc($seperatorColor).Bdbc($tableBorderBlue):h H(32px).Bgc($lv2BgColor)  a.Fw(600).C($linkColor)::text').extract()
        print(title)
        # ticker = response.css('tr.cmc-table-row td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--left.cmc-table__cell--sort-by__symbol>div::text').extract()
        # print(ticker)