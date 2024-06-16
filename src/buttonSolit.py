import src.event.baseEvent as baseEvent
from PyQt5.QtCore import QThreadPool,QRunnable
from src.pageData import pageData
from src.subtitles.subtitlesConvert import subtitle_convert
from src.MT import fileFormat



class buttonSolit:

    def __init__(self,wiget):
        self.threadPool = QThreadPool()
        self.wiget = wiget
        self.pageData = pageData(self.wiget)  # 页面参数汇总


    def ffmSolit(self):
        ui = self.wiget.ui  #删除
        # 添加单个文件
        ui.pushButton_2.clicked.connect(
            lambda: baseEvent.addFile(self.wiget, ui.videoInput, ui.videoOut, ui.videoFormat1))
        ui.audioInput.clicked.connect(lambda : baseEvent.addFile(self.wiget, ui.audioInputPath, ui.audioOutPath, ui.audioFormat,
                                                                 baseEvent.audioFormat))
        # 添加多个文件
        ui.videoAdd.clicked.connect(lambda: baseEvent.addFiles(self.wiget, ui.listWidget))
        ui.audioAdd.clicked.connect(lambda : baseEvent.addFiles(self.wiget, ui.audioList, fileFormat.audioFormat))
        # 清空按钮
        ui.videoClear.clicked.connect(lambda: ui.listWidget.clear())
        ui.audioClear.clicked.connect(lambda :ui.audioList.clear())
        # 删除单个
        ui.videoDelete.clicked.connect(lambda: ui.listWidget.takeItem(ui.listWidget.currentRow()))
        ui.audioDelete.clicked.connect(lambda :ui.audioList.takeItem(ui.audioList.currentRow()))

        # 合并
        ui.videoMerge.clicked.connect(lambda: self.threadStart(baseEvent.videoMerge))
        # 转换会单个文件
        ui.videoConver1.clicked.connect(lambda :self.threadStart(baseEvent.videoConver))

        # 单个声音转换
        ui.audioConver.clicked.connect(lambda :self.threadStart(baseEvent.audioConver))
        #批量转换
        ui.audioConver_2.clicked.connect(lambda :self.threadStart(baseEvent.audioConver_batch))
        ui.videoConver_2.clicked.connect(lambda :self.threadStart(baseEvent.videoConver_bitch))

    def subtitleSolit(self):
        ui = self.wiget.ui
        # 删除单个
        ui.subtitle_del.clicked.connect(lambda :ui.subitile_list.takeItem(ui.subitile_list.currentRow()))
        # 删除全部
        ui.subtitle_clear.clicked.connect(lambda :ui.subitile_list.clear())
        # 批量转换
        # self.worker = subtitle_convert(self.pageData.update())

        ui.subtitle_convert.clicked.connect(lambda :self.threadPool.start(subWork(subtitle_convert,None,self.pageData.update())))




    # 线程问题 必须将线程放入成员变量
    def threadStart(self,threadClass):
        self.thread = threadClass(self.pageData.update())
        self.thread.start()

#   执行子线程
class subWork(QRunnable):
    def __init__(self,func,signal,pageData):
        super().__init__()
        self.func = func
        self.signal = signal
        self.pageData = pageData

    def run(self):
        res = self.func(self.pageData)
        print("aaaa")




