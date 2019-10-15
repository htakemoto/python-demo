"""
Sample
The main implementation
"""

import sys
from sample.app import App

if __name__ == '__main__':
    print(sys.version)
    print(sys.executable)
    app = App()
    app.run()
