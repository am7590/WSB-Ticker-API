from flask import *
import json, time
from scrape_hot_posts import *
from scrape_24h_posts import *
from scrape_new_posts import *

app = Flask(__name__)


# Default GET
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Type': 'None', 'Content': 'Loaded the WSB Ticker API', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Hot Posts GET
# Ex. Get 100 hottest posts: /hot/?hot=100/
@app.route('/hot/', methods=['GET'])
def hot_posts():
    user_query = int(request.args.get('hot'))

    h_posts = scrape_hot_posts(user_query, 'wallstreetbets')
    data_set = {'Type': 'Hot', 'Scraped': user_query, 'Content': h_posts,
                'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# New Posts GET
# Ex. Get 100 newest posts: /new/?new=100/
@app.route('/new/', methods=['GET'])
def new_posts():
    user_query = int(request.args.get('new'))

    h_posts = scrape_new_posts(user_query, 'wallstreetbets')
    data_set = {'Type': 'New', 'Scraped': user_query, 'Content': h_posts,
                'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# 24h Posts GET
# Ex. See frequencies from last 24 hours: /24h/
@app.route('/24h/', methods=['GET'])
def get_h_posts():
    h_posts = scrape_24h_posts('wallstreetbets')
    data_set = {'Type': '24h', 'Content': h_posts, 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Run API on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Link to AWS lightsail deployment tutorial:
# https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/?trk=el_a134p000007C5T8AAK&trkCampaign=psc-2021-ec2_lightsail_flask&sc_channel=el&sc_campaign=ec2-lightsail-promo&sc_outcome=Enterprise_Digital_Marketing&sc_geo=NAMER

