# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/AoGui.ui'
#
# Created: Wed Feb 22 22:03:03 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(829, 653)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_4 = QtGui.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setHandleWidth(4)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget = QtGui.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.updateTimeSpin = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.updateTimeSpin.setEnabled(True)
        self.updateTimeSpin.setDecimals(1)
        self.updateTimeSpin.setMaximum(100.0)
        self.updateTimeSpin.setProperty("value", 15.0)
        self.updateTimeSpin.setObjectName(_fromUtf8("updateTimeSpin"))
        self.horizontalLayout_3.addWidget(self.updateTimeSpin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gainLayout = QtGui.QHBoxLayout()
        self.gainLayout.setObjectName(_fromUtf8("gainLayout"))
        self.horizontalLayout_3.addLayout(self.gainLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.splitter_2 = QtGui.QSplitter(self.splitter_4)
        self.splitter_2.setEnabled(True)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(4)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(4)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.LgsPsfLabel = QtGui.QLabel(self.layoutWidget1)
        self.LgsPsfLabel.setObjectName(_fromUtf8("LgsPsfLabel"))
        self.verticalLayout_12.addWidget(self.LgsPsfLabel)
        self.lgsLayout = QtGui.QHBoxLayout()
        self.lgsLayout.setObjectName(_fromUtf8("lgsLayout"))
        self.verticalLayout_12.addLayout(self.lgsLayout)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.dmLayout = QtGui.QHBoxLayout()
        self.dmLayout.setObjectName(_fromUtf8("dmLayout"))
        self.verticalLayout_5.addLayout(self.dmLayout)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.plotLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.plotLayout.setMargin(0)
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.layoutWidget3 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.phaseLayout = QtGui.QHBoxLayout()
        self.phaseLayout.setObjectName(_fromUtf8("phaseLayout"))
        self.verticalLayout_3.addLayout(self.phaseLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.wfsLayout = QtGui.QHBoxLayout()
        self.wfsLayout.setObjectName(_fromUtf8("wfsLayout"))
        self.verticalLayout_4.addLayout(self.wfsLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.layoutWidget4 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_4 = QtGui.QLabel(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.residualLayout = QtGui.QHBoxLayout()
        self.residualLayout.setObjectName(_fromUtf8("residualLayout"))
        self.verticalLayout_6.addLayout(self.residualLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_5 = QtGui.QLabel(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.instExpRadio = QtGui.QRadioButton(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instExpRadio.sizePolicy().hasHeightForWidth())
        self.instExpRadio.setSizePolicy(sizePolicy)
        self.instExpRadio.setChecked(True)
        self.instExpRadio.setObjectName(_fromUtf8("instExpRadio"))
        self.horizontalLayout_5.addWidget(self.instExpRadio)
        self.longExpRadio = QtGui.QRadioButton(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longExpRadio.sizePolicy().hasHeightForWidth())
        self.longExpRadio.setSizePolicy(sizePolicy)
        self.longExpRadio.setObjectName(_fromUtf8("longExpRadio"))
        self.horizontalLayout_5.addWidget(self.longExpRadio)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.sciLayout = QtGui.QHBoxLayout()
        self.sciLayout.setObjectName(_fromUtf8("sciLayout"))
        self.verticalLayout_7.addLayout(self.sciLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(4)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.splitter_3)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.consoleLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.consoleLayout.setMargin(0)
        self.consoleLayout.setObjectName(_fromUtf8("consoleLayout"))
        self.layoutWidget5 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.timeRemaining = QtGui.QLabel(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRemaining.sizePolicy().hasHeightForWidth())
        self.timeRemaining.setSizePolicy(sizePolicy)
        self.timeRemaining.setObjectName(_fromUtf8("timeRemaining"))
        self.verticalLayout_10.addWidget(self.timeRemaining)
        self.itersPerSecLabel = QtGui.QLabel(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itersPerSecLabel.sizePolicy().hasHeightForWidth())
        self.itersPerSecLabel.setSizePolicy(sizePolicy)
        self.itersPerSecLabel.setObjectName(_fromUtf8("itersPerSecLabel"))
        self.verticalLayout_10.addWidget(self.itersPerSecLabel)
        self.instStrehl = QtGui.QLabel(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instStrehl.sizePolicy().hasHeightForWidth())
        self.instStrehl.setSizePolicy(sizePolicy)
        self.instStrehl.setObjectName(_fromUtf8("instStrehl"))
        self.verticalLayout_10.addWidget(self.instStrehl)
        self.longStrehl = QtGui.QLabel(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longStrehl.sizePolicy().hasHeightForWidth())
        self.longStrehl.setSizePolicy(sizePolicy)
        self.longStrehl.setObjectName(_fromUtf8("longStrehl"))
        self.verticalLayout_10.addWidget(self.longStrehl)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.layoutWidget6 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.initButton = QtGui.QPushButton(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initButton.sizePolicy().hasHeightForWidth())
        self.initButton.setSizePolicy(sizePolicy)
        self.initButton.setObjectName(_fromUtf8("initButton"))
        self.verticalLayout_9.addWidget(self.initButton)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.iMatButton = QtGui.QPushButton(self.layoutWidget6)
        self.iMatButton.setObjectName(_fromUtf8("iMatButton"))
        self.horizontalLayout_7.addWidget(self.iMatButton)
        self.newCMat = QtGui.QCheckBox(self.layoutWidget6)
        self.newCMat.setObjectName(_fromUtf8("newCMat"))
        self.horizontalLayout_7.addWidget(self.newCMat)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.frameButton = QtGui.QPushButton(self.layoutWidget6)
        self.frameButton.setObjectName(_fromUtf8("frameButton"))
        self.horizontalLayout_8.addWidget(self.frameButton)
        self.runButton = QtGui.QPushButton(self.layoutWidget6)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout_8.addWidget(self.runButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.resetButton = QtGui.QPushButton(self.layoutWidget6)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_9.addWidget(self.resetButton)
        self.stopButton = QtGui.QPushButton(self.layoutWidget6)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout_9.addWidget(self.stopButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.gridLayout.addWidget(self.splitter_4, 1, 0, 1, 1)
        self.progressLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setText(_fromUtf8(""))
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.gridLayout.addWidget(self.progressLabel, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionTrue = QtGui.QAction(MainWindow)
        self.actionTrue.setObjectName(_fromUtf8("actionTrue"))
        self.actionFalse = QtGui.QAction(MainWindow)
        self.actionFalse.setObjectName(_fromUtf8("actionFalse"))
        self.loadParamsAction = QtGui.QAction(MainWindow)
        self.loadParamsAction.setObjectName(_fromUtf8("loadParamsAction"))
        self.reloadParamsAction = QtGui.QAction(MainWindow)
        self.reloadParamsAction.setObjectName(_fromUtf8("reloadParamsAction"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClose_2 = QtGui.QAction(MainWindow)
        self.actionClose_2.setObjectName(_fromUtf8("actionClose_2"))
        self.menuFile.addAction(self.loadParamsAction)
        self.menuFile.addAction(self.reloadParamsAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation Optique Adaptative in Python", None))
        self.label_7.setText(_translate("MainWindow", "Plot Update Rate (Hz)", None))
        self.label_2.setText(_translate("MainWindow", "Gain -", None))
        self.LgsPsfLabel.setText(_translate("MainWindow", "Laser Guide Star PSFs", None))
        self.label_6.setText(_translate("MainWindow", "DM Shapes", None))
        self.label.setText(_translate("MainWindow", "WFS Phase", None))
        self.label_3.setText(_translate("MainWindow", "Wave-front Sensors", None))
        self.label_4.setText(_translate("MainWindow", "Residual Phase", None))
        self.label_5.setText(_translate("MainWindow", "Science PSFs", None))
        self.instExpRadio.setText(_translate("MainWindow", "Instantaneous", None))
        self.longExpRadio.setText(_translate("MainWindow", "Long Exposure", None))
        self.timeRemaining.setText(_translate("MainWindow", "Time Remaining:", None))
        self.itersPerSecLabel.setText(_translate("MainWindow", "Iterations Per Second:", None))
        self.instStrehl.setText(_translate("MainWindow", "Instantaneous Strehl:", None))
        self.longStrehl.setText(_translate("MainWindow", "Long Exposure Strehl:", None))
        self.initButton.setText(_translate("MainWindow", "AO Init", None))
        self.iMatButton.setText(_translate("MainWindow", "Make IMat", None))
        self.newCMat.setText(_translate("MainWindow", "Force new?", None))
        self.frameButton.setText(_translate("MainWindow", "Frame", None))
        self.runButton.setText(_translate("MainWindow", "Run!", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionTrue.setText(_translate("MainWindow", "True", None))
        self.actionFalse.setText(_translate("MainWindow", "False", None))
        self.loadParamsAction.setText(_translate("MainWindow", "Load Configuration File", None))
        self.reloadParamsAction.setText(_translate("MainWindow", "Reload Current Configuration File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionClose_2.setText(_translate("MainWindow", "Close", None))

