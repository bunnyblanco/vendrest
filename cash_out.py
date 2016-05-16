"""
    Example usage of vendcli
"""
import os
import vendcli

from flask import Flask
from flask_script import Command, Manager

app = Flask(__name__)
app.config.from_pyfile('config.py')
manager = Manager(app)


