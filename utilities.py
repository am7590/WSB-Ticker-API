import csv
import pandas as pd
import praw
import re
from datetime import datetime

WSB_POSTS_SCRAPED = 100

# Step 1: Print a list of tickers
# Save tickers and company names ['ticker', 'name']
ticker_list = []
with open('tickers.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         ticker_list.append(row[0].split(","))

#for obj in ticker_list:
    # print(obj[0])  # Print ticker name
    # print(obj[1])  # Print company name
    # print(obj[0] + ": " + obj[1])  # Print company + ticker name

# Step 2: Create frequency list of tickers
# Read data from reddit API
reddit = praw.Reddit(
  client_id = "qBibtPUZ69Gi1IUUGhQ87w",
  client_secret = "8mzMqF5BRRa1kEWR9FqpJzhN1-WvBA",
  user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
)



# Analyze word frequency
def analyze_word_frequency(df):
    # (from https://medium.com/@tom.santinelli/scraping-reddits-wall-street-bets-for-popular-stock-tickers-38ed5202affc)
    regex = re.compile('[^a-zA-Z ]')
    word_dict = {}
    for (index, row) in df.iterrows():
        # titles
        title = row['title']
        title = regex.sub('', title)
        title_words = title.split(' ')
        # content
        content = row['text']
        content = regex.sub('', content)
        content_words = content.split(' ')
        # combine
        words = title_words + content_words
        for x in words:
            if x in ['A', 'B', 'GO', 'ARE', 'ON']:
                pass

            elif x in word_dict:
                word_dict[x] += 1
            else:
                word_dict[x] = 1
    word_df = pd.DataFrame.from_dict(list(word_dict.items())).rename(columns={0: "Term", 1: "Frequency"})
    ticker_df = pd.DataFrame(ticker_list).rename(columns={0: "Term", 1: "Name"})

    return [word_df, ticker_df]


