#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>First Flask App</h1>'

@app.route('/<string:myname>')
def name(myname):
    return f'<h4> App belongs to <h1>{myname}</h1>  </h4>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)