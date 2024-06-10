#!/usr/bin/env bash

source .venv/bin/activate

export LIGHTBULB_SECRET_KEY="9998887773335557771122331111111111111"

export FLASK_APP="lightbulb"
export FLASK_ENV="production"

gunicorn --config /etc/lightbulb/gunicorn.conf.py
