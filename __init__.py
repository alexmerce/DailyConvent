from PyQt5.QtWidgets import QApplication
import sys
import os
sys.path.append(os.getcwd())
from src.mainWiget import mainWiget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QApplication.setQuitOnLastWindowClosed(False)
    main = mainWiget()
    sys.exit(app.exec_())
