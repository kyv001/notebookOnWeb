import sys
if '' in sys.path:
    sys.path.append(".")

from notebookOnWeb import app

app.run()
