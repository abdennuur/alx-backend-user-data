#!/usr/bin/env python3
""" the Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ to GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ to GET /api/v1/stats
    Return:
      -  number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route("/unauthorized/",
                 strict_slashes=False)
def unauthorized() -> str:
    '''the Route unauthorized requests

    Returns:
        str: 401 status code
    '''
    abort(401)


@app_views.route("/forbidden/",
                 strict_slashes=False)
def forbidden() -> str:
    '''the Route forbidden requests

    Returns:
        str: 403 status code
    '''
    abort(403)
