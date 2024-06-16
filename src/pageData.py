from src.MT import basePath
import copy
class pageData():
    # loadImg = None
    # showLogWiget = None
    # ffmpegPath = None
    # fileListPath = None

    logParam = None
    def __init__(self,mainWiget):
        self.wiget = mainWiget
        # 主页面信号
        self.loadImg = mainWiget.loadImg
        self.showLogWiget = mainWiget.showLogWiget
        #  常量
        self.ffmpegPath = basePath.ffmpegPath
        self.fileListPath = basePath.fileListPath


    def update(self):
        ui = self.wiget.ui
        self.logWigetList = list(self.wiget.logWigetList.keys())
        # 汇总页面参数
        videoList = []
        for i in range(0, ui.listWidget.count()):
            videoList.append(ui.listWidget.item(i).text())
        self.videoList = videoList
        self.videoInput = ui.videoInput.text()
        self.videoOut = ui.videoOut.text()
        self.videoFormat1 = ui.videoFormat1.currentText()
        self.videoFormat2 = ui.videoFormat2.currentText()
        self.reCode = ui.reCode.checkState()
        self.vcodec = ui.vcodec.currentText()
        self.acodec = ui.acodec.currentText()


        self.audioInputPath = ui.audioInputPath.text()
        self.audioOutPath = ui.audioOutPath.text()
        self.bps = ui.bps.currentText()

        audioList = []
        for i in range(0,ui.audioList.count()):
            audioList.append(ui.audioList.item(i).text())
        self.audioList = audioList
        self.audioFormat_2 = ui.audioFormat_2.currentText()
        self.bps_2 = ui.bps_2.currentText()

        # subtitle区
        subitile_list = []
        for i in range(0,ui.subitile_list.count()):
            subitile_list.append(ui.subitile_list.item(i).text())
        self.subitile_list = subitile_list
        self.subtitle_targetFormat = ui.subtitle_targetFormat.currentText()


        return self
