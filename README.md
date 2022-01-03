# WSB-Ticker-API
WSB-Ticker-API analyzes the frequency of stock tickers being mentioned in WallStreetBets, and can be easily configured work on any subreddit. I built a REST API with Flask and Python and deployed it to AWS Lightsail using a Docker image.  

Users can specify how many posts to analyze, and whether look for new or hot posts. You can also get data for all posts over the last 24 hours. Below are some examples:

## Fetch data:

>Get frequency tables on the hottest 20 posts:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/hot/?hot=20

>Get frequency tables on the newest 50 posts:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/new/?new=50

>Get frequency tables from posts in the last 24 hours:
Fetch frequency tables on the hottest 20 posts:
https://flask-service.bg7bq3bnlj1de.us-east-1.cs.amazonlightsail.com/24h/




