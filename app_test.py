import unittest
import flask


app = flask.Flask(__name__)

with app.test_request_context('/'):
    assert flask.request.path == '/'

with app.test_request_context('/connected'):
    assert flask.request.path == '/connected'
