import sys
if '' not in sys.path:
    sys.path.append(".")

from notebookOnWeb import app

app.run()
