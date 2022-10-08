import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
            'titulos' : filmes.css('.titleColumn a::text').get(), #onde tem 'filmes' é pq vai referente do domínio css do 'response.css'. Esse e o próximo pertencem a mesma "caixa"
            'anos' : filmes.css('.secondaryInfo::text').get(),
            #'anos' : filmes.css('.secondaryInfo::text').get()[1:-1] para tirar os parentes
            'avaliacao' : response.css('strong::text').get() #esse aqui não se encontra na mesma caixa dos anteriores
        }
