"""
The flask application package.
"""

from flask import Flask
from notebookOnWeb.config import Config

app = Flask(__name__)
app.config.from_object(Config)

import notebookOnWeb.views
