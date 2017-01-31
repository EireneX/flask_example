from flask import Flask
from pymongo import MongoClient

app = Flask('__main__')
api = app


@app.route('/')
def index():
    return "<h1 style='color: blue'>Hello flask</h1>"

if __name__ == "__main__":
    app.run()