import scrapy

class IMDBSpider(scrapy.Spider):
    name = "imdb"
    start_urls = [
        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&sort=user_rating,desc&view=advanced"
    ]

    def parse(self, response):

        # Most of the time, the year will be next to the movie like so: Movie Title (YEAR)
        # But sometimes, the movie will have another thing next to it like so: Movie Title (II) (YEAR)
        # So need to just get the year by splitting on space and just returning the second thing
        def parse_year(year):
            temp = year.split(" ")
            if len(temp) > 1:
                return int(temp[1][1:-1])
            else:
                return int(temp[0][1:-1])

        for movie in response.css("div.lister-list div.lister-item"):
            data = {
                "title": movie.css("h3.lister-item-header a::text").get(),
                "year": parse_year(movie.css("h3.lister-item-header span.lister-item-year::text").get()),
                "rating": float(movie.css("div.ratings-imdb-rating strong::text").get()),
                "genres": [x.strip() for x in movie.css("div.lister-item-content p.text-muted span.genre::text").get().split(",")], # Split the genres into a list
                "runtime": int(movie.css("span.runtime::text").get().split(" ")[0]),
                "votes": int(movie.css("div.lister-item-content p.sort-num_votes-visible span[name='nv']::text").get().replace(",", ""))
            }

            yield data
        
        next_page = response.css("div#main div.article div.desc a.next-page::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
