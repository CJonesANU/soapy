# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\AoGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setHandleWidth(4)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.updateTimeSpin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.updateTimeSpin.setEnabled(True)
        self.updateTimeSpin.setDecimals(1)
        self.updateTimeSpin.setMaximum(100.0)
        self.updateTimeSpin.setProperty("value", 15.0)
        self.updateTimeSpin.setObjectName("updateTimeSpin")
        self.horizontalLayout_3.addWidget(self.updateTimeSpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gainLayout = QtWidgets.QHBoxLayout()
        self.gainLayout.setObjectName("gainLayout")
        self.horizontalLayout_3.addLayout(self.gainLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setEnabled(True)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(4)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(4)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.LgsPsfLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.LgsPsfLabel.setObjectName("LgsPsfLabel")
        self.verticalLayout_12.addWidget(self.LgsPsfLabel)
        self.lgsLayout = QtWidgets.QHBoxLayout()
        self.lgsLayout.setObjectName("lgsLayout")
        self.verticalLayout_12.addLayout(self.lgsLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.dmLayout = QtWidgets.QHBoxLayout()
        self.dmLayout.setObjectName("dmLayout")
        self.verticalLayout_5.addLayout(self.dmLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.plotLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.phaseLayout = QtWidgets.QHBoxLayout()
        self.phaseLayout.setObjectName("phaseLayout")
        self.verticalLayout_3.addLayout(self.phaseLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.wfsLayout = QtWidgets.QHBoxLayout()
        self.wfsLayout.setObjectName("wfsLayout")
        self.verticalLayout_4.addLayout(self.wfsLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.residualLayout = QtWidgets.QHBoxLayout()
        self.residualLayout.setObjectName("residualLayout")
        self.verticalLayout_6.addLayout(self.residualLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.instExpRadio = QtWidgets.QRadioButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instExpRadio.sizePolicy().hasHeightForWidth())
        self.instExpRadio.setSizePolicy(sizePolicy)
        self.instExpRadio.setChecked(True)
        self.instExpRadio.setObjectName("instExpRadio")
        self.horizontalLayout_5.addWidget(self.instExpRadio)
        self.longExpRadio = QtWidgets.QRadioButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longExpRadio.sizePolicy().hasHeightForWidth())
        self.longExpRadio.setSizePolicy(sizePolicy)
        self.longExpRadio.setObjectName("longExpRadio")
        self.horizontalLayout_5.addWidget(self.longExpRadio)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.sciLayout = QtWidgets.QHBoxLayout()
        self.sciLayout.setObjectName("sciLayout")
        self.verticalLayout_7.addLayout(self.sciLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(4)
        self.splitter_3.setObjectName("splitter_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.consoleLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.consoleLayout.setContentsMargins(0, 0, 0, 0)
        self.consoleLayout.setObjectName("consoleLayout")
        self.layoutWidget5 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.timeRemaining = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRemaining.sizePolicy().hasHeightForWidth())
        self.timeRemaining.setSizePolicy(sizePolicy)
        self.timeRemaining.setObjectName("timeRemaining")
        self.verticalLayout_10.addWidget(self.timeRemaining)
        self.itersPerSecLabel = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itersPerSecLabel.sizePolicy().hasHeightForWidth())
        self.itersPerSecLabel.setSizePolicy(sizePolicy)
        self.itersPerSecLabel.setObjectName("itersPerSecLabel")
        self.verticalLayout_10.addWidget(self.itersPerSecLabel)
        self.instStrehl = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instStrehl.sizePolicy().hasHeightForWidth())
        self.instStrehl.setSizePolicy(sizePolicy)
        self.instStrehl.setObjectName("instStrehl")
        self.verticalLayout_10.addWidget(self.instStrehl)
        self.longStrehl = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.longStrehl.sizePolicy().hasHeightForWidth())
        self.longStrehl.setSizePolicy(sizePolicy)
        self.longStrehl.setObjectName("longStrehl")
        self.verticalLayout_10.addWidget(self.longStrehl)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.initButton = QtWidgets.QPushButton(self.layoutWidget6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initButton.sizePolicy().hasHeightForWidth())
        self.initButton.setSizePolicy(sizePolicy)
        self.initButton.setObjectName("initButton")
        self.verticalLayout_9.addWidget(self.initButton)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.iMatButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.iMatButton.setObjectName("iMatButton")
        self.horizontalLayout_7.addWidget(self.iMatButton)
        self.newCMat = QtWidgets.QCheckBox(self.layoutWidget6)
        self.newCMat.setObjectName("newCMat")
        self.horizontalLayout_7.addWidget(self.newCMat)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frameButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.frameButton.setObjectName("frameButton")
        self.horizontalLayout_8.addWidget(self.frameButton)
        self.runButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_8.addWidget(self.runButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.resetButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_9.addWidget(self.resetButton)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_9.addWidget(self.stopButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.gridLayout.addWidget(self.splitter_4, 1, 0, 1, 1)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setText("")
        self.progressLabel.setObjectName("progressLabel")
        self.gridLayout.addWidget(self.progressLabel, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionTrue = QtWidgets.QAction(MainWindow)
        self.actionTrue.setObjectName("actionTrue")
        self.actionFalse = QtWidgets.QAction(MainWindow)
        self.actionFalse.setObjectName("actionFalse")
        self.loadParamsAction = QtWidgets.QAction(MainWindow)
        self.loadParamsAction.setObjectName("loadParamsAction")
        self.reloadParamsAction = QtWidgets.QAction(MainWindow)
        self.reloadParamsAction.setObjectName("reloadParamsAction")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_2 = QtWidgets.QAction(MainWindow)
        self.actionClose_2.setObjectName("actionClose_2")
        self.menuFile.addAction(self.loadParamsAction)
        self.menuFile.addAction(self.reloadParamsAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose_2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation Optique Adaptative in Python"))
        self.label_7.setText(_translate("MainWindow", "Plot Update Rate (Hz)"))
        self.label_2.setText(_translate("MainWindow", "Gain -"))
        self.LgsPsfLabel.setText(_translate("MainWindow", "Laser Guide Star PSFs"))
        self.label_6.setText(_translate("MainWindow", "DM Shapes"))
        self.label.setText(_translate("MainWindow", "WFS Phase"))
        self.label_3.setText(_translate("MainWindow", "Wave-front Sensors"))
        self.label_4.setText(_translate("MainWindow", "Residual Phase"))
        self.label_5.setText(_translate("MainWindow", "Science PSFs"))
        self.instExpRadio.setText(_translate("MainWindow", "Instantaneous"))
        self.longExpRadio.setText(_translate("MainWindow", "Long Exposure"))
        self.timeRemaining.setText(_translate("MainWindow", "Time Remaining:"))
        self.itersPerSecLabel.setText(_translate("MainWindow", "Iterations Per Second:"))
        self.instStrehl.setText(_translate("MainWindow", "Instantaneous Strehl:"))
        self.longStrehl.setText(_translate("MainWindow", "Long Exposure Strehl:"))
        self.initButton.setText(_translate("MainWindow", "AO Init"))
        self.iMatButton.setText(_translate("MainWindow", "Make IMat"))
        self.newCMat.setText(_translate("MainWindow", "Force new?"))
        self.frameButton.setText(_translate("MainWindow", "Frame"))
        self.runButton.setText(_translate("MainWindow", "Run!"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionTrue.setText(_translate("MainWindow", "True"))
        self.actionFalse.setText(_translate("MainWindow", "False"))
        self.loadParamsAction.setText(_translate("MainWindow", "Load Configuration File"))
        self.reloadParamsAction.setText(_translate("MainWindow", "Reload Current Configuration File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_2.setText(_translate("MainWindow", "Close"))

