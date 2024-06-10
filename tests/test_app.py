import pytest
from unittest.mock import patch, MagicMock
import logging
import os
import time
import datetime
from rfc3339 import rfc3339
from lightbulb import create_app
from lightbulb.main.views import main_blueprint
from flask import g

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'JL Miller Electric, Inc' in response.data
    
def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Our Company' in response.data

def test_services(client):
    response = client.get('/services')
    assert response.status_code == 200
    assert b'Services We Offer' in response.data

def test_terminology(client):
    response = client.get('/terminology')
    assert response.status_code == 200
    assert b'Category' in response.data

def test_nonexistent(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

def test_logger_configuration(app):
    assert len(app.logger.handlers) == 1
    assert isinstance(app.logger.handlers[0], logging.StreamHandler)

def test_remove_inital_handler(app):
    assert len(app.logger.handlers) == 1

@patch.dict('os.environ', {'FLASK_ENV': 'development'})
def test_flask_env_with_development():
    app = create_app()
    assert app.debug
    assert app.logger.level == logging.DEBUG

@patch.dict('os.environ', {'FLASK_ENV': 'production'})
def test_flask_env_with_production():
    app = create_app()
    assert not app.debug
    assert app.logger.level == logging.INFO

@patch.dict('os.environ', {'FLASK_ENV': 'invalid'})
def test_flask_env_with_invalid():
    app = create_app()
    assert not app.debug
    assert app.logger.level == logging.INFO

@patch.dict('os.environ', {'FLASK_ENV': ''})
def test_flask_env_with_empty_string():
    app = create_app()
    assert not app.debug
    assert app.logger.level == logging.INFO

def test_werkzeug_logger_level():
    werkzueg_logger = logging.getLogger('werkzeug')
    assert werkzueg_logger.level == logging.ERROR

@patch.dict('os.environ', {'LIGHTBULB_SECRET_KEY': 'my_secret_key'})
def test_secret_key_with_custom_env_var():
    app = create_app()
    assert app.config['SECRET_KEY'] == 'my_secret_key'

patch.dict('os.environ', {'LIGHTBULB_SECRET_KEY': None})
def test_secret_key_with_no_env_var():
    app = create_app()
    assert app.config['SECRET_KEY'] == '0000000000000000000000000000000000'


def test_blueprint_registration(app):
    assert 'main' in app.blueprints

def test_logger_messages(app, caplog):
    with caplog.at_level(logging.INFO):
        app.logger.info("FLASK_ENV = development")
        app.logger.info("FLASK_APP = lightbulb")
        assert "FLASK_ENV = development" in caplog.text
        assert "FLASK_APP = lightbulb" in caplog.text

def test_time_logging(monkeypatch):
    fake_time = 1234.5678
    monkeypatch.setattr(time, 'time', lambda: fake_time)
    app = create_app()
    with app.test_request_context():
        app.preprocess_request()
        assert g.start == fake_time

