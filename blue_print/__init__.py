"""
@Project: flask_demo
@File: __init__.py.py
@Author: Seeker
@Date:  10:41 下午
"""

from flask import Flask


def service():
    """
    服务
    :return:
    """
    app = Flask(__name__)

    from .console.views import console

    app.register_blueprint(console)

    return app
