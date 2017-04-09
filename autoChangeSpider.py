import scrapy,re,json
from scrapy.crawler import CrawlerProcess

class autoChangePasswordSpider(scrapy.Spider):
    name = 'autoChangePasswordSpider'

    start_urls=['http://www.ssmianfei.com/']

    def parse(self, response):
        selector = scrapy.Selector(response)
        fileName = selector.xpath('//*[@id="tablepress-3"]/tbody/tr[4]/td[2]').re(r"\w+.txt")[0]
        url = response.url + fileName
        yield scrapy.Request(url, callback=self.changePassword)

    def changePassword(self, response):
        password = response.body.decode('utf-8')
        with open('D:\proxy\shadowsocks\ShadowsocksR-4.1.5-win\gui-config.json', 'rb') as readFile:
            stream = readFile.read()
            dict = json.loads(str(stream, encoding='utf-8'))
            number = len(dict['configs'])
            remarks = ['ShareJP', 'ShareHK', 'ShareUS']
            for i in range(number):
                if dict['configs'][i]['remarks'] in remarks:
                    dict['configs'][i]['password'] = password

        with open('D:\proxy\shadowsocks\ShadowsocksR-4.1.5-win\gui-config.json', 'wb') as writeFile:
            stream = json.dumps(dict, ensure_ascii=False)
            writeFile.write(bytes(stream, encoding='utf-8'))



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(autoChangePasswordSpider)
process.start()