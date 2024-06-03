import os
from flask import Flask
from logging import getLogger

from lightbulb.logging import handler as lightbulb_handler
from lightbulb.factory import Lightbulb
from lightbulb.main.views import main_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    lightbulb = Lightbulb()

    lightbulb.init_app(app)
    
    if app.logger.handlers:
        app.logger.removeHandler(app.logger.handlers[0])

    if os.environ.get('FLASK_ENV') == 'development':
        app.logger.info('Creating app in development mode')
        app.logger.setLevel('DEBUG')
        app.debug = True
    else:
        app.logger.info('Creating app in production mode')
        app.logger.setLevel('INFO')
        app.debug = False
    

    app.logger.info(f"App: {__name__} | VIRTUAL_ENV = {os.environ.get('VIRTUAL_ENV', str(None))}")
    app.logger.info(f"App: {__name__} | FLASK_DEBUG = {app.debug}")
    app.logger.info(f"App: {__name__} | FLASK_RUN_FROM_CLI = {os.environ.get('FLASK_RUN_FROM_CLI')}")
    app.logger.info(f"App: {__name__} | FLASK_ENV = {os.environ.get('FLASK_ENV')}")
    app.logger.info(f"App: {__name__} | FLASK_APP = {os.environ.get('FLASK_APP')}")

    app.logger.debug("Environment Variables | " + str(os.environ))

    app.logger.info("Setting app.config values")
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('LIGHTBULB_SECRET_KEY', '0000000000000000000000000000000000'),
    )
    app.logger.debug(f"'app.config['SECRET_KEY'] = [LIGHTBULB_SECRET_KEY: {app.config['SECRET_KEY']}]")

    app.logger.info("Registering blueprints")

    app.register_blueprint(main_blueprint)
    app.logger.debug("Registered main_blueprint")
    
    return app

if __name__ == '__main__': 
    app = create_app()
    app.logger.debug("Running app in debug mode")
    app.run()

