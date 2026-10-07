import os, sys
BASE = os.path.dirname(__file__)
if BASE not in sys.path:
    sys.path.insert(0, BASE)
from app import app as application
