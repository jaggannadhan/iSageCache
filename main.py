import os
from flask import Flask, render_template
from src.handlers.DefaultHandler import default
from src.handlers.CacheHandler import cache_handler
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY"),
    SESSION_COOKIE_SECURE=True
)

CORS(app, resources={r"/*": {"origins": ["https://isage-cached-service-v2.streamlit.app"]}})

app.register_blueprint(default)
app.register_blueprint(cache_handler)

@app.errorhandler(404)
def not_found(e):
    return render_template("pageNotFound.html")

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.host = "0.0.0.0"
    app.port = 5000
    app.debug = True
    app.run()