import re
from src.pandoc import pandocOperation
from PyQt5.QtWidgets import QWidget, QLineEdit
pandocPath = r''
format = ".*(docx)|(md)|(html)$"


def conver(source: str, target: str, outWiget: QWidget):
    if not checkFormat(source):
        showStatus(source[source.rindex('.'):]+"不支持该格式", outWiget)
        return
    msg = pandocOperation.converDoc(source, target)
    if msg == None or msg == "":
        msg = target + "导出成功"
    showStatus(msg, outWiget)


def showStatus(message: str, lineEdit: QLineEdit):
    lineEdit.setText(message)


def checkFormat(source: str,):
    flag = re.match(format, source, re.I)
    if flag == None:
        return False
