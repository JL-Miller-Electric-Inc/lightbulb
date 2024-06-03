#!/usr/bin/env bash -x

source .venv/bin/activate

export FLASK_ENV="development"
export LIGHTBULB_SECRET_KEY="0000000000000000000000000"
export FLASK_APP="lightbulb"

flask run --debug

