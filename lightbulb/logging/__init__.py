from flask import request, has_request_context, Flask
import logging
import time

class CustomRequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.client_ip = request.headers.get('X-Real-IP', request.remote_addr)
        else:
            record.client_ip = '127.0.0.1'

        return super().format(record)
    

handler = logging.StreamHandler()
handler.setFormatter(CustomRequestFormatter(
    '[%(asctime)s] %(client_ip)s %(levelname)s in %(module)s: %(message)s'
))

class LightbulbLogger(object):
    def __init__(self, app=None):
        
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):

        app.logger.addHandler(handler)

        werkzueg_logger = logging.getLogger('werkzeug')
        werkzueg_logger.setLevel('ERROR')

