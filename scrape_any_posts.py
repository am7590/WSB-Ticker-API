from utilities import *

AVG_DAILY_POSTS = 3000


# Grab all WSB posts
def get_wsb_posts(subreddit, hours):
    df = []
    # lim = hours * int(AVG_DAILY_POSTS / 24)  # Calculate average daily posts per hour
    for post in reddit.subreddit(subreddit).new(limit=hours):
        utc_post_time = post.created
        submission_date = datetime.utcfromtimestamp(utc_post_time)

        current_time = datetime.utcnow()
        submission_delta = current_time - submission_date
        # print(submission_delta.seconds)  # See age of new posts
        if submission_delta.seconds <= (hours * 60 * 60):
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
def list_tickers(ticker_df, word_df):
    string = ""
    stonks_df = pd.merge(ticker_df["Term"], word_df, on="Term")
    final_df = stonks_df.sort_values(by=['Frequency'], ascending=False)
    new_line = final_df.to_string(index=False)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    string += str(new_line)

    return [convert_val(string), current_time]


def scrape_any_hour_posts(subreddit, hours):
    df = get_wsb_posts(subreddit, hours)
    [word_df, ticker_df] = analyze_word_frequency(df)
    return list_tickers(ticker_df, word_df)
