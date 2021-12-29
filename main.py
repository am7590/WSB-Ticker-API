from flask import *
import json, time
from scrape_hot_posts import *
from scrape_24h_posts import *
from scrape_new_posts import *


app = Flask(__name__)


# Default GET call
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Type of post': 'New', 'Content': 'Post content', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Hot Posts GET call
@app.route('/hot/', methods=['GET'])
def hot_posts():
    h_posts = scrape_hot_posts(50, 'wallstreetbets')
    data_set = {'Type of post': 'New', 'Content': h_posts, 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Run API
if __name__ == '__main__':
    app.run(port=7777)
