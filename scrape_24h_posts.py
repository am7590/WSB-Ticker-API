from utilities import *

DEFAULT_24H_POSTS_SCRAPED = 200


# Grab all WSB posts
def get_wsb_posts(posts_scraped, subreddit):
    df = []
    for post in reddit.subreddit(subreddit).new(limit=posts_scraped):
        utcPostTime = post.created
        submissionDate = datetime.utcfromtimestamp(utcPostTime)

        currentTime = datetime.utcnow()
        submissionDelta = currentTime - submissionDate
        # print(submissionDelta)  # See age of new posts

        if submissionDelta.days < 2:
            content = {
                "title": post.title,
                "text": post.selftext
            }
            df.append(content)
        else:
            df.append({"title": "", "text": ""})
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
        a_file.write(f"WSB Ticker Frequency from posts made in the last 24 hours: {current_time}\n")
        a_file.write(new_line)
        a_file.write("\n\n")


def scrape_24h_posts(subreddit):
    df = get_wsb_posts(DEFAULT_24H_POSTS_SCRAPED, subreddit)
    [word_df, ticker_df] = analyze_word_frequency(df)
    list_tickers(ticker_df, word_df, DEFAULT_24H_POSTS_SCRAPED)
