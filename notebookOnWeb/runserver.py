import sys
if '' not in sys.path:
    sys.path.append(".")

from notebookOnWeb import app
from os import environ
port = int(environ.get('PORT',5000))
app.run(port=port)
