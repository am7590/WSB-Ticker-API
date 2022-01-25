# WSB-Ticker-API
WSB-Ticker-API analyzes the frequency of stock tickers being mentioned in any subreddit. I built a REST API with Flask and Python and deployed it to AWS Lightsail using a Docker image.  

Users can specify how many posts to analyze, and whether look for new or hot posts. You can also get data for all posts over the last 24 hours. Below are some examples:

## Fetch data:

>Get frequency tables on the hottest 100 posts from r/WallStreetBets:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/hot/?subreddit=wallstreetbets&hot=100

>Get frequency tables on the newest 50 posts from r/PennyStocks:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/new/?subreddit=pennystocks&new=50

>Get frequency tables from posts in the last 24 hours from r/Stocks:
Fetch frequency tables on the hottest 20 posts:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/subreddit-hour/?subreddit=stocks&hours=24


## TODO:
- [ ] Return subreddit in API call
