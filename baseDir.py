import sys
import os
def appPath():
    if hasattr(sys,'frozen'):
        return os.path.dirname(__file__)
    return os.path.dirname(__file__)
