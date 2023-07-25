from flask import Flask
from flask_cors import CORS
import logging
from guestToken import guestToken

app = Flask(__name__)
CORS(app)

logger = logging.getLogger(__name__)

app.add_url_rule('/guestToken', view_func=guestToken.guest_token, methods=['GET'])

@app.route("/")
def index():
    flask_response = Flask.response_class()
    flask_response.headers["Access-Control-Allow-Origin"] = "*"
    return flask_response

# remember to deploy in gunicorn nginx
