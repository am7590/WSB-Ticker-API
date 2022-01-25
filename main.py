from flask import *
import json, time

from scrape_any_posts import *
from scrape_hot_posts import *
from scrape_new_posts import *
from datetime import datetime

app = Flask(__name__)


# Default GET
@app.route('/', methods=['GET'])
def home_page():
    current_time = datetime.now()
    hour_min_sec = "%s:%s.%s" % (current_time.hour, current_time.minute, str(current_time.second)[:2])

    data_set = {'type': 'none', 'content': 'Loaded the WSB Ticker API', 'time_called': hour_min_sec}
    json_dump = json.dumps(data_set)

    return json_dump


# Hot Posts GET
# Ex. Get 100 hottest posts: /hot/?subreddit=wallstreetbets&hot=100
@app.route('/hot/', methods=['GET'])
def hot_posts():
    current_time = datetime.now()
    hour_min_sec = "%s:%s.%s" % (current_time.hour, current_time.minute, str(current_time.second)[:2])

    user_subreddit = request.args.get('subreddit', None)
    user_query = int(request.args.get('hot'))

    [h_posts, time_done] = scrape_hot_posts(user_query, user_subreddit)
    data_set = {'type': 'hot', 'posts': user_query, 'content': h_posts, 'time_called': hour_min_sec,
                'time_compiled': time_done}
    json_dump = json.dumps(data_set)

    return json_dump


# New Posts GET
# Ex. Get 100 newest posts: /new/?subreddit=wallstreetbets&new=100
@app.route('/new/', methods=['GET'])
def new_posts():
    current_time = datetime.now()
    hour_min_sec = "%s:%s.%s" % (current_time.hour, current_time.minute, str(current_time.second)[:2])

    user_subreddit = request.args.get('subreddit', None)
    user_query = int(request.args.get('new'))

    [h_posts, time_done] = scrape_new_posts(user_query, user_subreddit)
    data_set = {'type': 'new', 'posts': user_query, 'content': h_posts,
                'time_called': hour_min_sec, 'time_compiled': time_done}
    json_dump = json.dumps(data_set)

    return json_dump


# Any subreddit/hour GET
# Ex. See frequencies from last 24 hours from wallstreetbets: /subreddit-hour/?subreddit=wallstreetbets&hours=24
# Works for any subreddit and any integer hour
@app.route('/subreddit-hour/', methods=['GET'])
def get_h_posts():
    current_time = datetime.now()
    hour_min_sec = "%s:%s.%s" % (current_time.hour, current_time.minute, str(current_time.second)[:2])

    user_subreddit = request.args.get('subreddit', None)
    user_hours = int(request.args.get('hours', None))

    # [h_posts, time_done] = scrape_24h_posts(user_query)
    [h_posts, time_done] = scrape_any_hour_posts(user_subreddit, user_hours)

    data_set = {'type': 'custom', 'content': h_posts, 'time_called': hour_min_sec, 'time_compiled': time_done}
    json_dump = json.dumps(data_set)

    return json_dump


# Run API on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Link to AWS lightsail deployment tutorial:
# https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/?trk=el_a134p000007C5T8AAK&trkCampaign=psc-2021-ec2_lightsail_flask&sc_channel=el&sc_campaign=ec2-lightsail-promo&sc_outcome=Enterprise_Digital_Marketing&sc_geo=NAMER
