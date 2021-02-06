from flask import Flask, jsonify
import kw_lib_crawl

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(kw_lib_crawl.all_seats())


if __name__ == '__main__':
    app.run(host = '0,0,0,0')
