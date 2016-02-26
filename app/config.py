# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os

class Config(object):
    """Common settings for all configurations."""

    # Flask
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Default Woodbox Secret'
    SESSION_COOKIE_NAME = 'woodbox-session'
    JSONIFY_PRETTYPRINT_REGULAR = True

    # SQLAlchemy

    # Example URI:
    # - sqlite+pysqlite:////tmp/test.sqlite
    # - mysql+mysqldb://woodbox_test:woodbox_test@localhost/woodbox_test
    # - postgresql+psycopg2://woodbox_test:woodbox_test@localhost/woodbox_test
    #SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:////tmp/woodbox.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://woodbox_test:woodbox_test@localhost/woodbox_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Woodbox
    PASSWORD_SALT = 'salt' # Use some random salt

    # Application
    # TODO: Default admin name
    # TODO: Default admin password

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    @classmethod
    def init_app(cls, app):
        # Add an URL to initialize DB with some data.
        from .views import populate_db
        app.add_url_rule('/init', 'init', populate_db)

class ProductionConfig(Config):
    SYSLOG_ADDRESS = os.environ.get('WOODBOX_SYSLOG_ADDRESS') or '/dev/log'

    @classmethod
    def init_app(cls, app):
        # Log messages to syslogd.
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler(address=cls.SYSLOG_ADDRESS)
        syslog_handler.setLevel(logging.WARNING)
        syslog_handler.setFormatter(logging.Formatter(
            '%(name)s %(asctime)s %(levelname)s: %(message)s'))
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
