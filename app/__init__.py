"""This is the app demonstrates logging_config configuration and unit testing"""
import logging
import os

from flask import Flask, render_template
from app import logging_config


def create_app(test_config=None):
    logging_config.logging_setup()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        debug=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    @app.route('/portfolio')
    def portfolio():
        return render_template("portfolio.html")

    @app.route('/contact')
    def contact():
        return render_template("contact.html")

    return app
