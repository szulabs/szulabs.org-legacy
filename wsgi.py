#!/usr/bin/env python


from flask import Flask, render_template
application = app = Flask('wsgi')


@app.route('/')
def welcome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
