#!/usr/bin/env bash

source venv/bin/activate

exec gunicorn -b :5000 --access-logfile - --error-logfile - ifood_api:app