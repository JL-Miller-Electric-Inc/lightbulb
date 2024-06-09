import os
from flask import Flask, request, g

import time
import datetime
from rfc3339 import rfc3339
import colors
import logging

from lightbulb.main.views import main_blueprint

class CustomRequestFormatter(logging.Formatter):
    def format(self, record):
        return super().format(record)
    

system_handler = logging.StreamHandler()
system_handler.setFormatter(CustomRequestFormatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

lightbulb_logger = logging.getLogger('app')
lightbulb_logger.setLevel(logging.DEBUG)

lightbulb_handler = logging.StreamHandler()
lightbulb_handler.setFormatter(logging.Formatter(''))

lightbulb_logger.addHandler(lightbulb_handler)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.logger.addHandler(system_handler)

    if len(app.logger.handlers) > 1:
        app.logger.removeHandler(app.logger.handlers[0])


    werkzueg_logger = logging.getLogger('werkzeug')
    werkzueg_logger.setLevel('ERROR')

    if os.environ.get('FLASK_ENV') == 'development':
        app.logger.setLevel('DEBUG')
        app.debug = True
    else:
        app.logger.setLevel('INFO')
        app.debug = False

    lightbulb_logger.info(f"VIRTUAL_ENV = {os.environ.get('VIRTUAL_ENV', str(None))}")
    lightbulb_logger.info(f"FLASK_DEBUG = {app.debug}")
    lightbulb_logger.info(f"FLASK_RUN_FROM_CLI = {os.environ.get('FLASK_RUN_FROM_CLI')}")
    lightbulb_logger.info(f"FLASK_ENV = {os.environ.get('FLASK_ENV')}")
    lightbulb_logger.info(f"FLASK_APP = {os.environ.get('FLASK_APP')}")

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('LIGHTBULB_SECRET_KEY', '0000000000000000000000000000000000'),
    )

    lightbulb_logger.info(f"LIGHTBULB_SECRET_KEY: {app.config['SECRET_KEY']}")

    blueprint_start = time.time()
    app.register_blueprint(main_blueprint)
    blueprint_end = time.time()

    blueprint_duration = round(blueprint_end - blueprint_start, 2)

    app.logger.debug(f"blueprints loaded in {blueprint_duration} seconds.")
    
    @app.before_request
    def start_timer():
        g.start = time.time()

    # Log request/response info for each request after the request is processed
    @app.after_request
    def log_request(response):
        if request.path == '/favicon.ico':
            return response
        elif request.path.startswith('/static'):
            return response

        now = time.time()
        duration = round(now - g.start, 2)
        dt = datetime.datetime.fromtimestamp(now)
        timestamp = rfc3339(dt, utc=True)

        ip = request.headers.get('X-Real-IP', request.remote_addr)
        host = request.host.split(':', 1)[0]
        args = dict(request.args)

        log_params = [
            ('method', request.method, 'blue'),
            ('path', request.path, 'blue'),
            ('status', response.status_code, 'yellow'),
            ('duration', duration, 'green'),
            ('time', timestamp, 'magenta'),
            ('ip', ip, 'red'),
            ('host', host, 'red'),
            ('params', args, 'blue')
        ]

        request_id = request.headers.get('X-Request-ID')
        if request_id:
            log_params.append(('request_id', request_id, 'yellow'))

        parts = []

        for name, value, color in log_params:
            part = colors.color("{}={}".format(name, value), fg=color)
            parts.append(part)
            line = " ".join(parts)

        lightbulb_logger.info(line)

        return response
    
    return app

if __name__ == '__main__': 
    app = create_app()
    app.run()

