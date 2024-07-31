import scrapy
import db_processor


def process_articles(articles):
    cnt = 0
    for article in articles:
        cnt+=1
        print(cnt)
        db_processor.insert_into_articles(article)

class SkkuSpiderSpider(scrapy.Spider):
    name = "skku_spider"
    allowed_domains = ["forensic.skku.edu"]
    start_urls = ["https://forensic.skku.edu/forensic/community/grad_notice.do"]

    def parse(self, response):
        articles = []
        for article in response.css("ul.board-list-wrap > li"):
            data={
                "title": article.css("dl > dt a::text").get().replace("\n","").replace("\t","").replace(" ",""),#함수로 만들면 더 쉬움
                "link": article.css("dl > dt a::attr(href)").get()
            }   
            articles.append(data)
        print(articles)
        process_articles(articles)

        #    for page in response.css('ul.paging-wrap li'):
        #        link = page.css('a::attr(href)').get()
        #        link_text = page.css('a::text').get()

        #        if link_text:
        #            link_text = link_text.strip()
               
        #        if link_text and link_text.isdigit() and int(link_text) <= 3:
        #            yield { 'page_number': link_text, 'link': link }
        #            yield response.follow(link, self.parse)   


            