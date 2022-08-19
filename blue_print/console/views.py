"""
@Project: flask_demo
@File: views.py
@Author: Seeker
@Date:  10:56 下午
"""
from flask import Blueprint

console = Blueprint("console", __name__)


# 控制台
@console.route("/")
def index():
    return "hello baby"
