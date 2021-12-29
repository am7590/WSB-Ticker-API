from utilities import *


# Grab all WSB posts
def get_wsb_posts(posts_scraped, subreddit):
    df = []
    for post in reddit.subreddit(subreddit).new(limit=posts_scraped):
        content = {
            "title": post.title,
            "text": post.selftext
        }
        df.append(content)
    df = pd.DataFrame(df)

    return df


# List of tickers (sorted by frequency)
def list_tickers(ticker_df, word_df, posts_scraped):
    stonks_df = pd.merge(ticker_df["Term"], word_df, on="Term")
    final_df = stonks_df.sort_values(by=['Frequency'], ascending=False)
    new_line = final_df.to_string(index=False)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    with open("output.txt", "a") as a_file:
        a_file.write(f"WSB Ticker Frequency from the newest {posts_scraped} posts: {current_time}\n")
        a_file.write(new_line)
        a_file.write("\n\n")


def scrape_new_posts(posts_scraped, subreddit):
    df = get_wsb_posts(posts_scraped, subreddit)
    [word_df, ticker_df] = analyze_word_frequency(df)
    list_tickers(ticker_df, word_df, posts_scraped)
