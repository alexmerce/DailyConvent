from src.buttonSolit import buttonSolit
import src.event.pandocEvent as pandocEvent

from PyQt5.QtWidgets import QTabWidget, QMessageBox
from PyQt5.QtGui import QIcon,QMovie
from PyQt5.QtCore import pyqtSignal
from ui import my, pandocNote, log
import src.event.baseEvent as baseEvent
import src.sonWindow as sonWindow
from src.MT import logType,fileFormat,basePath


class mainWiget(QTabWidget):
    showLogWiget = pyqtSignal(dict)
    loadImg = pyqtSignal(dict)

    def __init__(self):
        super(mainWiget, self).__init__()
        self.start()

    def start(self):

        self.ui = my.Ui_TabWidget()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(basePath.icon))
        self.setWindowTitle("初号机")
        # self.threadPool = QThreadPool()
        # 按钮信号
        self.buttonSolit = buttonSolit(self)

        self.logWigetList = {}  #日志窗口列表

        self._buttonSolit()   # 按钮信号绑定
        self.listDragEnterSeting()  # 文件拖拽设置
        self.signalConnect() # 主线程信号绑定

        self.ui.hideFrame1.hide()




        self.pandocNote = baseEvent.sonDialog(pandocNote.Ui_Dialog())

        self.show()

    def signalConnect(self):
        self.showLogWiget.connect(self.showlog) #日志窗口信号
        self.loadImg.connect(self.loadingGifChange) #loading图标信号

    def _buttonSolit(self):

        # ffmpeg区
        self.buttonSolit.ffmSolit()
        # subtitle区
        self.buttonSolit.subtitleSolit()

        # pandoc区
        # 格式提示
        # self.ui.pushButton_9.clicked.connect(lambda :baseEvent.sonDialog(pandocNote.Ui_Dialog()).show())
        self.ui.pushButton_9.clicked.connect(lambda: self.pandocNote.show())
        self.ui.pushButton_10.clicked.connect(lambda: baseEvent.addFile(
            self, self.ui.lineEdit_4, self.ui.lineEdit_5, self.ui.comboBox_3, baseEvent.docFormat))
        self.ui.comboBox_3.currentTextChanged.connect(lambda boxselect: baseEvent.updateOutName(
            self.ui.lineEdit_4.text(), self.ui.lineEdit_5, boxselect))
        # 单文件转换
        self.ui.pushButton_12.clicked.connect(
            lambda: pandocEvent.conver(self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text(), self.ui.stauts))

    def listDragEnterSeting(self):
        ui = self.ui
        # 筛选拖拽
        ui.listWidget.dragEnterEvent = lambda e: baseEvent.dragEnterEvent(e, ui.listWidget)
        # 单个视频输入
        ui.videoInput.dragEnterEvent = lambda e: baseEvent.dragEnterEvent(
            e,ui.videoInput,outWiget=ui.videoOut,selectWiget=ui.videoFormat1
        )
        # 单音频输入
        ui.audioInputPath.dragEnterEvent = lambda e: baseEvent.dragEnterEvent(
            e,ui.audioInputPath, fileFormat.audioFormat,ui.audioOutPath,ui.audioFormat
        )
        ui.audioInputPath.dropEvent = baseEvent.dropEvent
        ui.lineEdit_4.dragEnterEvent = lambda e: baseEvent.dragEnterEvent(
            e, ui.lineEdit_4, baseEvent.docFormat, ui.lineEdit_5, ui.comboBox_3)
        # 多音频输入
        ui.audioList.dragEnterEvent = lambda e: baseEvent.dragEnterEvent(e, self.ui.audioList, fileFormat.audioFormat, None, ui.audioFormat_2)
        # 多字幕输入
        ui.subitile_list.dragEnterEvent = lambda  e: baseEvent.dragEnterEvent(e, self.ui.subitile_list,fileFormat.subtitleFormat, None, ui.subtitle_convert)

    # loading图标状态
    def loadingGifChange(self,logParam:dict):
        logWigetName = logParam['logWigetName']
        currentGif = self.logWigetList[logWigetName]['QMovie']
        currentGif.start()


    # 日志窗口信号提交/修改
    def showlog(self,logParam:dict):
        logWigetName = logParam['logWigetName']
        if(logWigetName in self.logWigetList):
            wigetInfo = self.logWigetList[logWigetName] #获取当前日志窗口
            if 'type' in logParam:
                if logParam['type'] == logType.endIng:
                    # 关闭loading窗口
                    wigetInfo['wiget'].close()
                    self.logWigetList.pop(logWigetName)
                    # 开启结束窗口
                    self.endwiget = sonWindow.successWiget(logWigetName)
                if (logParam['type'] == logType.error):
                    self.msg_box = QMessageBox.warning(self, logParam['logWigetName'], logParam['msg'])
                    self.logWigetList[logWigetName]['wiget'].close()
                    self.logWigetList.pop(logWigetName)

        elif 'type' in logParam and logParam['type'] == logType.warning:
            # 新建提示窗口
            self.msg_box = QMessageBox.warning(self,logParam['logWigetName'],logParam['msg'])
        else:
            # 新建日志窗口
            logui = log.Ui_loading()
            logWiget = sonWindow.sonWindow(logui, logWigetName)

            loading = QMovie(basePath.app+'/img/loading.gif')
            logui.load.setMovie(loading)
            logWiget.show()
            loading.start()
            currentWigetInfo = {'wiget':logWiget,'QMovie':loading,'logui':logui}
            self.logWigetList[logWigetName] = currentWigetInfo
            print("新建窗口:" + logWigetName)
