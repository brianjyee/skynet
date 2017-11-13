"""Run the recsvc with the builtin flask web server.

This script bypasses our usual gunicorn/greenlet/gevent webstack in favor of
running the service single-threaded in flask's development web server. While
this will never be a desirable production configurarion, this can be useful
while in development mode. In particular, by setting debug=True, the service
will autoload changes automatically.
"""
import skynet
server = skynet.create_app()
server.run(host='0.0.0.0', port=8497, debug=True)
