import os
import app.src.config as config

from flask import Flask


def create(environment):
    config_map = {
        'development': config.Development(),
        'testing': config.Testing(),
        'production': config.Production
    }

    config_obj = config_map[environment.lower()]

    app = Flask(__name__)
    app.config.from_object(config_obj)

    app.add_url_rule('/', 'home', home)

    return app


def home():
    return dict(name='Server running..')
