# IMDb Scraper
This Python application uses scrapy to scrape the IMDb feature films list. It scrapes the top 1,000 films by user rating and pulls data from each movie into a JSON object and outputs everything to a JSON file. https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&sort=user_rating,desc&view=advanced


## Prerequisites
1. Have Python and pip installed on your computer.
2. Install scrapy by running `pip install -r requirements.txt` or `pip install scrapy`.
3. Initialize the scrapy project by running `scrapy startproject imdb`


## Documentation
- Scrapy Tutorial https://docs.scrapy.org/en/latest/intro/tutorial.html


## Running the Scraper
1. Navigate to the `imdb` directory
    ```
    cd imdb
    ```
2. Run the following command:
    ```
    scrapy crawl imdb -O imdb.json
    ```
    
    `-O imdb.json` means to output the results to the `imdb.json` file
3. Wait for the scraper to finish, this should take less than 30 seconds.
4. Verify the data in `imdb.json`.
