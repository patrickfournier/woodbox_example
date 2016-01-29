# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from woodbox import create_app as create_woodbox
from woodbox.session import add_session_management_urls

from .config import config

def create_app(config_name):
    config_obj = config[config_name]
    app = create_woodbox(config_obj)

    from .api_v1 import blueprint as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    add_session_management_urls(app)

    return app
