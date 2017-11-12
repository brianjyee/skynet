#!/bin/bash
env FLASK_CONFIG='skynet.settings.local.LocalConfig' gunicorn 'skynet:create_app()' -b:8888 -w 1 -k gevent --worker-connections=2000 --backlog=1000
