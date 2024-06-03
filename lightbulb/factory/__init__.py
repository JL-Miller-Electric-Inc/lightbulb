from flask import Flask, request, has_request_context, session
from lightbulb.logging import handler

import logging

class Lightbulb(object):
    def __init__(self, app=None):
        
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):

        app.logger.addHandler(handler)

        werkzueg_logger = logging.getLogger('werkzeug')
        werkzueg_logger.setLevel('ERROR')
        

