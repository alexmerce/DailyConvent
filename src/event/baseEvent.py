import os

from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit, QListWidget, QDialog, QComboBox
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtCore import QThread

from src import MT
import src.ffmlib.ffmOperation as ffmOperation
from src.pageData import pageData


# 单个视频添加 窗口,文件路径展示框,输出路径展示框,需求格式下拉框,文件格式限制


def addFile(wiget: QWidget, line: QLineEdit, outLine: QLineEdit, combox: QComboBox, formart=MT.fileFormat.videoFormat):
    fileName = fileWindow(wiget, formart)
    if fileName=='':return #未选择文件不处理
    line.setText(os.path.abspath(fileName))
    outLine.setText(changeName(fileName, combox.currentText()))


def addFiles(wiget: QWidget, outWiget: QListWidget, formart=MT.fileFormat.videoFormat):
    files = filesWindow(wiget, formart)
    for file in files:
        if (checkFileRepect(outWiget, file)):
            outWiget.addItem(os.path.abspath(file))


def fileWindow(wiget, formart):
    fileInfo = QFileDialog.getOpenFileName(wiget, "打开", ".", formart)
    return fileInfo[0]


def filesWindow(wiget, formart):
    fileInfo = QFileDialog.getOpenFileNames(wiget, "打开", '.', formart)
    return fileInfo[0]


def changeName(name: str, suffix=""):
    if name == None or name == "":
        return
    index = name.rindex(".")
    if (suffix == ""):
        str = name[0:index] + suffix + name[index:]
    else:
        str = name[0:index+1]+suffix
    return str
# 更新输出名


def updateOutName(intiName: str, outWiget, suffix: str):
    prefix = r"file:///"
    if intiName.startswith(prefix):
        intiName = intiName.replace(prefix, '')
    outWiget.setText(changeName(intiName, suffix))

# 文件拖拽拦截


def dragEnterEvent(e: QDragEnterEvent, inputWiget, baseFormat=MT.fileFormat.videoFormat, outWiget=None, selectWiget: QComboBox = None):

    urls = e.mimeData().urls()
    for url in urls:
        fileName = os.path.realpath(url.toLocalFile())
        index = fileName.rindex('.')
        if isinstance(inputWiget, QListWidget):
            if (baseFormat.__contains__(fileName[index:]) and checkFileRepect(inputWiget, fileName)):
                inputWiget.addItem(fileName)
            else:
                e.ignore()
        elif isinstance(inputWiget, QLineEdit):
            if (not baseFormat.__contains__(fileName[index:])):
                e.ignore()
                continue
            inputWiget.clear()
            inputWiget.setText(changeName(fileName))
            if (outWiget != None and selectWiget != None):  # 更新输出
                updateOutName(fileName, outWiget, selectWiget.currentText())
        else:
            continue
    e.accept()
#    文件拖拽获取，一直获取失败,直接拦截获取


def dropEvent(e: QDropEvent):
    urls = e.mimeData().urls()
    for url in urls:

        fileName = url.toLocalFile()
        # print(fileName)
        # if (checkFile(listWigt, fileName)):
        #  listWigt.addItem(fileName)


def checkFileRepect(listWiget: QListWidget, name):
    for i in range(0, listWiget.count()):
        if (name == listWiget.item(i).text()):
            return False
    return True

#视频合并
class videoMerge(QThread):
    def __init__(self,pageData:pageData):
        super(videoMerge, self).__init__()
        self.pageData = pageData

    def run(self):
        pageData = self.pageData
        videoList = pageData.videoList
        if (len(videoList) < 1):
            return
        mergeName = getMergeName(videoList[0])
        pageData.mergeName = mergeName
        # 显示日志窗口
        preLogDeal(self.pageData,mergeName)

        out = ffmOperation.videoMerge(pageData)
        if (errorEnd(pageData, mergeName, out)):
            return
        changeEnd(pageData, mergeName)


def checkFileFormat(fileList):
    suffix = ""
    for fileName in fileList:
        index = fileName.rindex('.')
        suffixTem = fileName[index+1:]
        if (suffix == "" or suffix == suffixTem):
            suffix = suffixTem
        else:
            return False

    return True

class videoConver(QThread):
    def __init__(self,pageData:pageData):
        super(videoConver, self).__init__()
        self.pageData = pageData
    def run(self):
        pageData = self.pageData
        if pageData.videoInput =='' or pageData.videoOut == '':
            return
        preLogDeal(pageData,pageData.videoOut)
        out = ffmOperation.videoConver(vars(pageData))
        if(errorEnd(pageData,pageData.videoOut,out)):
            return
        changeEnd(pageData,pageData.videoOut)


class videoConver_bitch(QThread):
    def __init__(self, pageData: pageData):
        super(videoConver_bitch, self).__init__()
        self.pageData = pageData

    def run(self):
        fileList =self.pageData.videoList
        for inPath in fileList:
            outPath = changeName(inPath,self.pageData.videoFormat2)
            preLogDeal(self.pageData, outPath)
            pageData_t = vars(self.pageData)
            pageData_t['videoInput'] = inPath
            pageData_t['videoOut'] = outPath
            out = ffmOperation.videoConver(pageData_t)
            if (errorEnd(self.pageData, outPath, out)):
                return
            changeEnd(self.pageData, outPath)


class audioConver(QThread):

    def __init__(self,pageData:pageData):
        super(audioConver, self).__init__()
        self.pageData = pageData

    def run(self):
        if not chackPath(self.pageData, MT.changeType.audioChange):
            return

        preLogDeal(self.pageData, self.pageData.audioOutPath)


        out = ffmOperation.audioConver(self.pageData)

        if(errorEnd(self.pageData,self.pageData.audioOutPath,out)):
            return

        changeEnd(self.pageData,self.pageData.audioOutPath)


def preLogDeal(pageData:pageData,outPath):
    # 新建日志窗口
    logParam = {'logWigetName': outPath}
    pageData.logParam = logParam
    pageData.showLogWiget.emit(logParam)








def sonDialog(ui):
    dialog = QDialog()
    ui.setupUi(dialog)
    return dialog

def chackPath(pageData:pageData,changeType,outPath=None):
    #音频转换校验
    if(changeType == MT.changeType.audioChange):
        if pageData.audioInputPath == '' or pageData.audioOutPath == '':
            return False
        if(not os.path.exists(pageData.audioInputPath)):
            pageData.showLogWiget.emit({'type': MT.logType.warning, 'msg': MT.msg.fileNotExist, 'logWigetName':pageData.audioInputPath})
            return False
        if(pageData.audioOutPath in pageData.logWigetList):
            pageData.showLogWiget.emit({'type': MT.logType.warning, 'msg': MT.msg.haveChange, 'logWigetName':pageData.audioOutPath})
            return False
    if(changeType == MT.changeType.audioChange_batch):
        if (outPath in pageData.logWigetList):
            pageData.showLogWiget.emit({'type': MT.logType.warning, 'msg': MT.msg.haveChange, 'logWigetName':outPath})
            return False


    return True


def changeEnd(pageData:pageData,outPath):
    logParam = pageData.logParam
    logParam['msg'] = '文件 %s 已保存' % outPath
    logParam['type'] = MT.logType.endIng
    pageData.showLogWiget.emit(logParam)

def errorEnd(pageData,outPath,out):
    if out.endswith('No such file or directory\r\n'):
        pageData.showLogWiget.emit(
            {'type': MT.logType.error, 'msg': MT.msg.pathError, 'logWigetName': outPath})
        return True

    return False

def getMergeName(inPath,count = 0):
    filePath = inPath[0:inPath.rindex("\\") + 1]
    i = '' if count==0 else count
    mergeName = filePath + "合并" +str(i)+ inPath[inPath.rindex("."):]
    if os.path.exists(mergeName):
        return getMergeName(inPath,count+1)
    else:
        return mergeName


# def showMenue()




