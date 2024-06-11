# gunicorn.conf.py
# http://docs.gunicorn.org/en/stable/configure.html

# This file is used in the Docker image as the default configuration.

bind = "0.0.0.0:5050"

reload = False
wsgi_app = "run:app"
worker_class = "gevent"
workers = 4

loglevel = "info"

accesslog = "/app/logs/gunicorn-access.log"
errorlog = "/app/logs/gunicorn-error.log"
