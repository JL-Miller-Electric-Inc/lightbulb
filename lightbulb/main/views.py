from flask import (
    Blueprint, render_template, redirect, url_for, request, current_app, send_from_directory
)

from .data import meta_description, meta_keywords

main_blueprint = Blueprint('main', __name__, url_prefix='/', template_folder='templates')

@main_blueprint.route('/', methods=['GET'])
def index():
    current_app.logger.debug("main.index()")
    current_app.logger.debug(str(request))
    return render_template('main/index.html', meta_description=meta_description['index'], meta_keywords=meta_keywords['index'])

@main_blueprint.route('/about', methods=['GET'])
def about():
    current_app.logger.debug("main.about()")
    current_app.logger.debug(str(request))
    return render_template('main/about.html', meta_description=meta_description['about'], meta_keywords=meta_keywords['about'])

@main_blueprint.route('/services/', methods=['GET'])
@main_blueprint.route('/services', methods=['GET'])
def services():
    current_app.logger.debug("main.services()")
    current_app.logger.debug(str(request))
    return render_template('main/services.html', meta_description=meta_description['services'], meta_keywords=meta_keywords['services'])

@main_blueprint.route('/terminology/', methods=['GET'])
@main_blueprint.route('/terminology', methods=['GET'])
def terminology():
    current_app.logger.debug("main.terminology()")
    current_app.logger.debug(str(request))
    return render_template('main/terminology.html', meta_description=meta_description['terminology'], meta_keywords=meta_keywords['terminology'])

@main_blueprint.route('/favicon.ico')
@main_blueprint.route('/robots.txt')
@main_blueprint.route('/sitemap.xml')
def static_from_root():
    current_app.logger.debug("main.static_from_root(): " + str(request))
    current_app.logger.debug(f"main.static_from_root(): root_path = {current_app.root_path} request.path[1:] = {request.path[1:]}")
    return send_from_directory(current_app.root_path, request.path[1:])
