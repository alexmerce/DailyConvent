import os

from PyQt5.QtWidgets import QWidget,QDialog
from PyQt5.QtCore import Qt

from ui import changeSuccess
from src.MT import msg

def sonWindow(ui,windowTitle='Forme'):
    logWindow = QWidget()
    ui.setupUi(logWindow)
    logWindow.setWindowTitle(windowTitle)
    logWindow.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
    return logWindow


def successWiget(outPath):
    endwiget = QDialog()

    ui = changeSuccess.Ui_Dialog()
    ui.setupUi(endwiget)
    ui.fileOutPath.setText(outPath)

    ui.openExplorer.clicked.connect(lambda :startExplorer(outPath,endwiget))
    endwiget.show()
    endwiget.setWindowTitle(msg.fileSaveSuccess)
    return endwiget

def startExplorer(path,wiget):
    os.system(f'explorer /select, %s'%path)
    wiget.close()
