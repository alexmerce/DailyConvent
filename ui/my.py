# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(767, 790)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMaximumSize(QtCore.QSize(16777215, 790))
        TabWidget.setMouseTracking(True)
        TabWidget.setTabletTracking(True)
        TabWidget.setAcceptDrops(True)
        TabWidget.setWhatsThis("")
        TabWidget.setStyleSheet("")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 731, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.videoInput = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoInput.sizePolicy().hasHeightForWidth())
        self.videoInput.setSizePolicy(sizePolicy)
        self.videoInput.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.videoInput.setMouseTracking(True)
        self.videoInput.setTabletTracking(True)
        self.videoInput.setText("")
        self.videoInput.setReadOnly(True)
        self.videoInput.setObjectName("videoInput")
        self.gridLayout.addWidget(self.videoInput, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.videoOut = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoOut.sizePolicy().hasHeightForWidth())
        self.videoOut.setSizePolicy(sizePolicy)
        self.videoOut.setObjectName("videoOut")
        self.gridLayout.addWidget(self.videoOut, 1, 1, 1, 1)
        self.videoConver1 = QtWidgets.QPushButton(self.layoutWidget)
        self.videoConver1.setObjectName("videoConver1")
        self.gridLayout.addWidget(self.videoConver1, 1, 2, 1, 2)
        self.videoFormat1 = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFormat1.sizePolicy().hasHeightForWidth())
        self.videoFormat1.setSizePolicy(sizePolicy)
        self.videoFormat1.setObjectName("videoFormat1")
        self.videoFormat1.addItem("")
        self.gridLayout.addWidget(self.videoFormat1, 0, 3, 1, 1)
        self.videoAdd = QtWidgets.QPushButton(self.tab)
        self.videoAdd.setGeometry(QtCore.QRect(630, 250, 111, 41))
        self.videoAdd.setObjectName("videoAdd")
        self.videoClear = QtWidgets.QPushButton(self.tab)
        self.videoClear.setGeometry(QtCore.QRect(630, 310, 111, 41))
        self.videoClear.setObjectName("videoClear")
        self.videoDelete = QtWidgets.QPushButton(self.tab)
        self.videoDelete.setGeometry(QtCore.QRect(630, 370, 111, 41))
        self.videoDelete.setObjectName("videoDelete")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(630, 570, 30, 16))
        self.label_3.setObjectName("label_3")
        self.videoFormat2 = QtWidgets.QComboBox(self.tab)
        self.videoFormat2.setEnabled(True)
        self.videoFormat2.setGeometry(QtCore.QRect(630, 600, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFormat2.sizePolicy().hasHeightForWidth())
        self.videoFormat2.setSizePolicy(sizePolicy)
        self.videoFormat2.setMinimumSize(QtCore.QSize(0, 19))
        self.videoFormat2.setBaseSize(QtCore.QSize(0, 0))
        self.videoFormat2.setObjectName("videoFormat2")
        self.videoFormat2.addItem("")
        self.videoConver_2 = QtWidgets.QPushButton(self.tab)
        self.videoConver_2.setGeometry(QtCore.QRect(630, 650, 111, 41))
        self.videoConver_2.setObjectName("videoConver_2")
        self.videoMerge = QtWidgets.QPushButton(self.tab)
        self.videoMerge.setGeometry(QtCore.QRect(630, 470, 111, 41))
        self.videoMerge.setObjectName("videoMerge")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 230, 601, 461))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 700, 591, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 180, 761, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.hideFrame1 = QtWidgets.QFrame(self.tab)
        self.hideFrame1.setGeometry(QtCore.QRect(80, 140, 451, 26))
        self.hideFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hideFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hideFrame1.setObjectName("hideFrame1")
        self.layoutWidget2 = QtWidgets.QWidget(self.hideFrame1)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 0, 207, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vcodec = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcodec.sizePolicy().hasHeightForWidth())
        self.vcodec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vcodec.setFont(font)
        self.vcodec.setObjectName("vcodec")
        self.vcodec.addItem("")
        self.vcodec.addItem("")
        self.horizontalLayout_3.addWidget(self.vcodec)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.acodec = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acodec.sizePolicy().hasHeightForWidth())
        self.acodec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acodec.setFont(font)
        self.acodec.setObjectName("acodec")
        self.acodec.addItem("")
        self.acodec.addItem("")
        self.horizontalLayout_3.addWidget(self.acodec)
        self.reCode = QtWidgets.QCheckBox(self.tab)
        self.reCode.setGeometry(QtCore.QRect(10, 140, 81, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reCode.sizePolicy().hasHeightForWidth())
        self.reCode.setSizePolicy(sizePolicy)
        self.reCode.setObjectName("reCode")
        TabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 40, 741, 101))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.audioConver = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioConver.sizePolicy().hasHeightForWidth())
        self.audioConver.setSizePolicy(sizePolicy)
        self.audioConver.setObjectName("audioConver")
        self.gridLayout_3.addWidget(self.audioConver, 1, 3, 1, 1)
        self.audioOutPath = QtWidgets.QLineEdit(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioOutPath.sizePolicy().hasHeightForWidth())
        self.audioOutPath.setSizePolicy(sizePolicy)
        self.audioOutPath.setObjectName("audioOutPath")
        self.gridLayout_3.addWidget(self.audioOutPath, 1, 1, 1, 1)
        self.audioOut = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioOut.sizePolicy().hasHeightForWidth())
        self.audioOut.setSizePolicy(sizePolicy)
        self.audioOut.setObjectName("audioOut")
        self.gridLayout_3.addWidget(self.audioOut, 1, 0, 1, 1)
        self.audioInput = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioInput.sizePolicy().hasHeightForWidth())
        self.audioInput.setSizePolicy(sizePolicy)
        self.audioInput.setObjectName("audioInput")
        self.gridLayout_3.addWidget(self.audioInput, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.audioInputPath = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.audioInputPath.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioInputPath.sizePolicy().hasHeightForWidth())
        self.audioInputPath.setSizePolicy(sizePolicy)
        self.audioInputPath.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.audioInputPath.setMouseTracking(True)
        self.audioInputPath.setTabletTracking(True)
        self.audioInputPath.setText("")
        self.audioInputPath.setReadOnly(False)
        self.audioInputPath.setObjectName("audioInputPath")
        self.gridLayout_3.addWidget(self.audioInputPath, 0, 1, 1, 1)
        self.audioFormat = QtWidgets.QComboBox(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioFormat.sizePolicy().hasHeightForWidth())
        self.audioFormat.setSizePolicy(sizePolicy)
        self.audioFormat.setObjectName("audioFormat")
        self.audioFormat.addItem("")
        self.gridLayout_3.addWidget(self.audioFormat, 0, 3, 1, 1)
        self.bps = QtWidgets.QComboBox(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.bps.sizePolicy().hasHeightForWidth())
        self.bps.setSizePolicy(sizePolicy)
        self.bps.setObjectName("bps")
        self.bps.addItem("")
        self.gridLayout_3.addWidget(self.bps, 1, 2, 1, 1)
        self.audioList = QtWidgets.QListWidget(self.widget)
        self.audioList.setGeometry(QtCore.QRect(10, 230, 601, 461))
        self.audioList.setMouseTracking(True)
        self.audioList.setTabletTracking(True)
        self.audioList.setAcceptDrops(True)
        self.audioList.setObjectName("audioList")
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 180, 761, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.audioAdd = QtWidgets.QPushButton(self.widget)
        self.audioAdd.setGeometry(QtCore.QRect(630, 250, 111, 41))
        self.audioAdd.setObjectName("audioAdd")
        self.audioClear = QtWidgets.QPushButton(self.widget)
        self.audioClear.setGeometry(QtCore.QRect(630, 310, 111, 41))
        self.audioClear.setObjectName("audioClear")
        self.audioDelete = QtWidgets.QPushButton(self.widget)
        self.audioDelete.setGeometry(QtCore.QRect(630, 370, 111, 41))
        self.audioDelete.setObjectName("audioDelete")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(630, 520, 30, 16))
        self.label_7.setObjectName("label_7")
        self.audioFormat_2 = QtWidgets.QComboBox(self.widget)
        self.audioFormat_2.setEnabled(True)
        self.audioFormat_2.setGeometry(QtCore.QRect(630, 540, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioFormat_2.sizePolicy().hasHeightForWidth())
        self.audioFormat_2.setSizePolicy(sizePolicy)
        self.audioFormat_2.setMinimumSize(QtCore.QSize(0, 19))
        self.audioFormat_2.setBaseSize(QtCore.QSize(0, 0))
        self.audioFormat_2.setObjectName("audioFormat_2")
        self.audioFormat_2.addItem("")
        self.audioConver_2 = QtWidgets.QPushButton(self.widget)
        self.audioConver_2.setGeometry(QtCore.QRect(630, 650, 111, 41))
        self.audioConver_2.setObjectName("audioConver_2")
        self.bps_2 = QtWidgets.QComboBox(self.widget)
        self.bps_2.setGeometry(QtCore.QRect(630, 580, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.bps_2.sizePolicy().hasHeightForWidth())
        self.bps_2.setSizePolicy(sizePolicy)
        self.bps_2.setObjectName("bps_2")
        self.bps_2.addItem("")
        TabWidget.addTab(self.widget, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.subitile_list = QtWidgets.QListWidget(self.tab_3)
        self.subitile_list.setGeometry(QtCore.QRect(20, 30, 601, 461))
        self.subitile_list.setMouseTracking(True)
        self.subitile_list.setTabletTracking(True)
        self.subitile_list.setAcceptDrops(True)
        self.subitile_list.setObjectName("subitile_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 40, 121, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subtitle_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_del.sizePolicy().hasHeightForWidth())
        self.subtitle_del.setSizePolicy(sizePolicy)
        self.subtitle_del.setObjectName("subtitle_del")
        self.verticalLayout.addWidget(self.subtitle_del)
        self.subtitle_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_clear.sizePolicy().hasHeightForWidth())
        self.subtitle_clear.setSizePolicy(sizePolicy)
        self.subtitle_clear.setObjectName("subtitle_clear")
        self.verticalLayout.addWidget(self.subtitle_clear)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(630, 340, 51, 21))
        self.label_9.setObjectName("label_9")
        self.subtitle_targetFormat = QtWidgets.QComboBox(self.tab_3)
        self.subtitle_targetFormat.setEnabled(True)
        self.subtitle_targetFormat.setGeometry(QtCore.QRect(630, 380, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_targetFormat.sizePolicy().hasHeightForWidth())
        self.subtitle_targetFormat.setSizePolicy(sizePolicy)
        self.subtitle_targetFormat.setMinimumSize(QtCore.QSize(0, 19))
        self.subtitle_targetFormat.setBaseSize(QtCore.QSize(0, 0))
        self.subtitle_targetFormat.setObjectName("subtitle_targetFormat")
        self.subtitle_targetFormat.addItem("")
        self.subtitle_convert = QtWidgets.QPushButton(self.tab_3)
        self.subtitle_convert.setGeometry(QtCore.QRect(630, 450, 111, 41))
        self.subtitle_convert.setObjectName("subtitle_convert")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 510, 601, 41))
        self.lineEdit_6.setStyleSheet("border-bottom-style:solid;\n"
"font: 9pt \"Arial\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        TabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 660, 601, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 731, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMouseTracking(True)
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 1, 2, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 3, 1, 1)
        self.stauts = QtWidgets.QLineEdit(self.tab_2)
        self.stauts.setGeometry(QtCore.QRect(-10, 730, 791, 41))
        self.stauts.setText("")
        self.stauts.setObjectName("stauts")
        # TabWidget.addTab(self.tab_2, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.reCode.toggled['bool'].connect(self.hideFrame1.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.pushButton_2.setText(_translate("TabWidget", "视频"))
        self.videoInput.setPlaceholderText(_translate("TabWidget", "可以将文件拖拽到这里"))
        self.label.setText(_translate("TabWidget", "转换为："))
        self.pushButton_3.setText(_translate("TabWidget", "输出文件"))
        self.videoConver1.setText(_translate("TabWidget", "转换"))
        self.videoFormat1.setItemText(0, _translate("TabWidget", "mp4"))
        self.videoAdd.setText(_translate("TabWidget", "添加"))
        self.videoClear.setText(_translate("TabWidget", "清空"))
        self.videoDelete.setText(_translate("TabWidget", "删除"))
        self.label_3.setText(_translate("TabWidget", "格式"))
        self.videoFormat2.setItemText(0, _translate("TabWidget", "mp4"))
        self.videoConver_2.setText(_translate("TabWidget", "转换"))
        self.videoMerge.setText(_translate("TabWidget", "合并"))
        self.label_2.setText(_translate("TabWidget", "批量转换/合并"))
        self.vcodec.setItemText(0, _translate("TabWidget", "libx264"))
        self.vcodec.setItemText(1, _translate("TabWidget", "copy"))
        self.label_8.setText(_translate("TabWidget", "音频:"))
        self.acodec.setItemText(0, _translate("TabWidget", "copy"))
        self.acodec.setItemText(1, _translate("TabWidget", "aac"))
        self.reCode.setText(_translate("TabWidget", "重新编码"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "视频转换/合并"))
        self.audioConver.setText(_translate("TabWidget", "转换"))
        self.audioOut.setText(_translate("TabWidget", "输出文件"))
        self.audioInput.setText(_translate("TabWidget", "音频"))
        self.label_5.setText(_translate("TabWidget", "转换为："))
        self.audioInputPath.setPlaceholderText(_translate("TabWidget", "可以将文件拖拽到这里"))
        self.audioFormat.setItemText(0, _translate("TabWidget", "mp3"))
        self.bps.setItemText(0, _translate("TabWidget", "320k"))
        self.label_6.setText(_translate("TabWidget", "批量转换/合并"))
        self.audioAdd.setText(_translate("TabWidget", "添加"))
        self.audioClear.setText(_translate("TabWidget", "清空"))
        self.audioDelete.setText(_translate("TabWidget", "删除"))
        self.label_7.setText(_translate("TabWidget", "格式"))
        self.audioFormat_2.setItemText(0, _translate("TabWidget", "mp3"))
        self.audioConver_2.setText(_translate("TabWidget", "转换"))
        self.bps_2.setItemText(0, _translate("TabWidget", "320k"))
        TabWidget.setTabText(TabWidget.indexOf(self.widget), _translate("TabWidget", "音频转换"))
        self.subtitle_del.setText(_translate("TabWidget", "删除"))
        self.subtitle_clear.setText(_translate("TabWidget", "清空"))
        self.label_9.setText(_translate("TabWidget", "转换为:"))
        self.subtitle_targetFormat.setItemText(0, _translate("TabWidget", "lrc"))
        self.subtitle_convert.setText(_translate("TabWidget", "转换"))
        self.lineEdit_6.setText(_translate("TabWidget", "输入限制:*.srt *.lrc *.ssa *.vtt"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "字幕转换"))
        self.pushButton_9.setText(_translate("TabWidget", "pandoc支持提示"))
        self.pushButton_10.setText(_translate("TabWidget", "文档"))
        self.lineEdit_4.setPlaceholderText(_translate("TabWidget", "可以将文件拖拽到这里"))
        self.label_4.setText(_translate("TabWidget", "转换为："))
        self.pushButton_11.setText(_translate("TabWidget", "输出文件"))
        self.pushButton_12.setText(_translate("TabWidget", "转换"))
        self.comboBox_3.setItemText(0, _translate("TabWidget", "md"))
        self.comboBox_3.setItemText(1, _translate("TabWidget", "docx"))
        self.comboBox_3.setItemText(2, _translate("TabWidget", "html"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "文档转换"))

