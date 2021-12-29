from flask import *
import json, time

app = Flask(__name__)


# Default GET call
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Type of post': 'New', 'Content': 'Post content', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# Run API
if __name__ == '__main__':
    app.run(port=7777)
