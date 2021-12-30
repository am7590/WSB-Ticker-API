from flask import *
import json, time
from scrape_hot_posts import *
from scrape_24h_posts import *
from scrape_new_posts import *

app = Flask(__name__)


# Default GET call
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Type of post': 'None', 'Content': 'Loaded the WSB Ticker API', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Hot Posts GET call
# Ex. Get 100 hottest posts: /hot/?hot=100/
@app.route('/hot/', methods=['GET'])
def hot_posts():
    user_query = int(request.args.get('hot'))

    h_posts = scrape_hot_posts(user_query, 'wallstreetbets')
    data_set = {'Type of post': 'Hot', 'Number of posts scraped': user_query, 'Content': h_posts,
                'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# New Posts GET
# Ex. Get 100 newest posts: /new/?new=100/
@app.route('/new/', methods=['GET'])
def new_posts():
    user_query = int(request.args.get('new'))

    h_posts = scrape_new_posts(user_query, 'wallstreetbets')
    data_set = {'Type of post': 'New', 'Number of posts scraped': user_query, 'Content': h_posts,
                'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# 24h Posts GET
# Ex. See frequencies from last 24 hours: /24h/
@app.route('/24h/', methods=['GET'])
def get_h_posts():
    h_posts = scrape_24h_posts('wallstreetbets')
    data_set = {'Type of post': '24h', 'Content': h_posts, 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Run API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



