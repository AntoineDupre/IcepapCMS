# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogpreferences.ui'
#
# Created: Thu Dec 17 11:52:46 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogPreferences(object):
    def setupUi(self, DialogPreferences):
        DialogPreferences.setObjectName("DialogPreferences")
        DialogPreferences.resize(558, 468)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 237, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 117, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 157, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 148, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 237, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 117, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 157, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 148, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 237, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 117, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 157, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 123, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        DialogPreferences.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogPreferences.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(DialogPreferences)
        self.gridlayout.setObjectName("gridlayout")
        self.listWidget = QtGui.QListWidget(DialogPreferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 70))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.listWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget.setIconSize(QtCore.QSize(44, 44))
        self.listWidget.setFlow(QtGui.QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", QtCore.QVariant(False))
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName("listWidget")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/small_icons/IcepapCfg Icons/Icepapicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon2)
        self.gridlayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(DialogPreferences)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageStorage = QtGui.QWidget()
        self.pageStorage.setObjectName("pageStorage")
        self.gridlayout1 = QtGui.QGridLayout(self.pageStorage)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem, 4, 0, 1, 1)
        self.lblModules = QtGui.QLabel(self.pageStorage)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lblModules.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblModules.setFont(font)
        self.lblModules.setObjectName("lblModules")
        self.gridlayout1.addWidget(self.lblModules, 3, 0, 1, 1)
        self.gbLocal = QtGui.QGroupBox(self.pageStorage)
        self.gbLocal.setObjectName("gbLocal")
        self.hboxlayout = QtGui.QHBoxLayout(self.gbLocal)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtGui.QLabel(self.gbLocal)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.txtLocalFolder = QtGui.QLineEdit(self.gbLocal)
        self.txtLocalFolder.setMaximumSize(QtCore.QSize(1666666, 16777215))
        self.txtLocalFolder.setObjectName("txtLocalFolder")
        self.hboxlayout.addWidget(self.txtLocalFolder)
        self.btnBrowser = QtGui.QToolButton(self.gbLocal)
        self.btnBrowser.setObjectName("btnBrowser")
        self.hboxlayout.addWidget(self.btnBrowser)
        self.gridlayout1.addWidget(self.gbLocal, 1, 0, 1, 1)
        self.gbRemote = QtGui.QGroupBox(self.pageStorage)
        self.gbRemote.setObjectName("gbRemote")
        self.gridlayout2 = QtGui.QGridLayout(self.gbRemote)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")
        spacerItem1 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem1, 1, 5, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gbRemote)
        self.txtPassword.setMinimumSize(QtCore.QSize(150, 0))
        self.txtPassword.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.gridlayout2.addWidget(self.txtPassword, 1, 3, 1, 2)
        self.txtPort = QtGui.QLineEdit(self.gbRemote)
        self.txtPort.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txtPort.setObjectName("txtPort")
        self.gridlayout2.addWidget(self.txtPort, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.gbRemote)
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3, 0, 2, 1, 1)
        self.txtHost = QtGui.QLineEdit(self.gbRemote)
        self.txtHost.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtHost.setObjectName("txtHost")
        self.gridlayout2.addWidget(self.txtHost, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem2, 0, 4, 1, 2)
        self.label_2 = QtGui.QLabel(self.gbRemote)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gbRemote)
        self.label_4.setObjectName("label_4")
        self.gridlayout2.addWidget(self.label_4, 1, 0, 1, 1)
        self.txtUser = QtGui.QLineEdit(self.gbRemote)
        self.txtUser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtUser.setObjectName("txtUser")
        self.gridlayout2.addWidget(self.txtUser, 1, 1, 1, 1)
        self.txPasswo = QtGui.QLabel(self.gbRemote)
        self.txPasswo.setObjectName("txPasswo")
        self.gridlayout2.addWidget(self.txPasswo, 1, 2, 1, 1)
        self.gridlayout1.addWidget(self.gbRemote, 2, 0, 1, 1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.rbsqlite = QtGui.QRadioButton(self.pageStorage)
        self.rbsqlite.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/sqlite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbsqlite.setIcon(icon3)
        self.rbsqlite.setIconSize(QtCore.QSize(50, 50))
        self.rbsqlite.setObjectName("rbsqlite")
        self.hboxlayout1.addWidget(self.rbsqlite)
        self.rbmysql = QtGui.QRadioButton(self.pageStorage)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/mysql.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbmysql.setIcon(icon4)
        self.rbmysql.setIconSize(QtCore.QSize(50, 50))
        self.rbmysql.setObjectName("rbmysql")
        self.hboxlayout1.addWidget(self.rbmysql)
        self.rbpostgres = QtGui.QRadioButton(self.pageStorage)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/postgresql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbpostgres.setIcon(icon5)
        self.rbpostgres.setIconSize(QtCore.QSize(40, 40))
        self.rbpostgres.setObjectName("rbpostgres")
        self.hboxlayout1.addWidget(self.rbpostgres)
        self.gridlayout1.addLayout(self.hboxlayout1, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageStorage)
        self.pageIcepap = QtGui.QWidget()
        self.pageIcepap.setObjectName("pageIcepap")
        self.gridlayout3 = QtGui.QGridLayout(self.pageIcepap)
        self.gridlayout3.setObjectName("gridlayout3")
        self.groupBox = QtGui.QGroupBox(self.pageIcepap)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout4 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout4.setObjectName("gridlayout4")
        self.chkDebug = QtGui.QCheckBox(self.groupBox)
        self.chkDebug.setObjectName("chkDebug")
        self.gridlayout4.addWidget(self.chkDebug, 0, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridlayout4.addWidget(self.label_5, 1, 0, 1, 1)
        self.sbDebugLevel = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbDebugLevel.sizePolicy().hasHeightForWidth())
        self.sbDebugLevel.setSizePolicy(sizePolicy)
        self.sbDebugLevel.setMinimum(1)
        self.sbDebugLevel.setMaximum(1)
        self.sbDebugLevel.setObjectName("sbDebugLevel")
        self.gridlayout4.addWidget(self.sbDebugLevel, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(261, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem3, 1, 2, 1, 2)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridlayout4.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtLogFolder = QtGui.QLineEdit(self.groupBox)
        self.txtLogFolder.setMaximumSize(QtCore.QSize(1666666, 16777215))
        self.txtLogFolder.setObjectName("txtLogFolder")
        self.gridlayout4.addWidget(self.txtLogFolder, 2, 1, 1, 2)
        self.btnLogBrowser = QtGui.QToolButton(self.groupBox)
        self.btnLogBrowser.setObjectName("btnLogBrowser")
        self.gridlayout4.addWidget(self.btnLogBrowser, 2, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridlayout4.addWidget(self.label_7, 3, 0, 1, 1)
        self.txtFirmwareFolder = QtGui.QLineEdit(self.groupBox)
        self.txtFirmwareFolder.setMaximumSize(QtCore.QSize(1666666, 16777215))
        self.txtFirmwareFolder.setObjectName("txtFirmwareFolder")
        self.gridlayout4.addWidget(self.txtFirmwareFolder, 3, 1, 1, 2)
        self.btnFirmwareBrowser = QtGui.QToolButton(self.groupBox)
        self.btnFirmwareBrowser.setObjectName("btnFirmwareBrowser")
        self.gridlayout4.addWidget(self.btnFirmwareBrowser, 3, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridlayout4.addWidget(self.label_8, 4, 0, 3, 1)
        self.txtConfigsFolder = QtGui.QLineEdit(self.groupBox)
        self.txtConfigsFolder.setMaximumSize(QtCore.QSize(1666666, 16777215))
        self.txtConfigsFolder.setObjectName("txtConfigsFolder")
        self.gridlayout4.addWidget(self.txtConfigsFolder, 4, 1, 1, 2)
        self.btnConfigsBrowser = QtGui.QToolButton(self.groupBox)
        self.btnConfigsBrowser.setObjectName("btnConfigsBrowser")
        self.gridlayout4.addWidget(self.btnConfigsBrowser, 4, 3, 2, 1)
        self.txtTemplatesFolder = QtGui.QLineEdit(self.groupBox)
        self.txtTemplatesFolder.setMaximumSize(QtCore.QSize(1666666, 16777215))
        self.txtTemplatesFolder.setObjectName("txtTemplatesFolder")
        self.gridlayout4.addWidget(self.txtTemplatesFolder, 5, 1, 3, 2)
        self.btnTemplatesBrowser = QtGui.QToolButton(self.groupBox)
        self.btnTemplatesBrowser.setObjectName("btnTemplatesBrowser")
        self.gridlayout4.addWidget(self.btnTemplatesBrowser, 6, 3, 2, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridlayout4.addWidget(self.label_9, 7, 0, 1, 1)
        self.gridlayout3.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(522, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout3.addItem(spacerItem4, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageIcepap)
        self.gridlayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem5 = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem5)
        self.closeButton = QtGui.QPushButton(DialogPreferences)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/IcepapCfg Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon6)
        self.closeButton.setIconSize(QtCore.QSize(22, 22))
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout2.addWidget(self.closeButton)
        self.gridlayout.addLayout(self.hboxlayout2, 2, 0, 1, 1)

        self.retranslateUi(DialogPreferences)
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogPreferences)
        DialogPreferences.setTabOrder(self.rbsqlite, self.rbmysql)
        DialogPreferences.setTabOrder(self.rbmysql, self.rbpostgres)
        DialogPreferences.setTabOrder(self.rbpostgres, self.txtLocalFolder)
        DialogPreferences.setTabOrder(self.txtLocalFolder, self.btnBrowser)
        DialogPreferences.setTabOrder(self.btnBrowser, self.txtHost)
        DialogPreferences.setTabOrder(self.txtHost, self.txtPort)
        DialogPreferences.setTabOrder(self.txtPort, self.txtUser)
        DialogPreferences.setTabOrder(self.txtUser, self.txtPassword)
        DialogPreferences.setTabOrder(self.txtPassword, self.closeButton)
        DialogPreferences.setTabOrder(self.closeButton, self.listWidget)

    def retranslateUi(self, DialogPreferences):
        DialogPreferences.setWindowTitle(QtGui.QApplication.translate("DialogPreferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("DialogPreferences", "Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("DialogPreferences", "IcePAP", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lblModules.setText(QtGui.QApplication.translate("DialogPreferences", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:8pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">import modules</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.gbLocal.setTitle(QtGui.QApplication.translate("DialogPreferences", "Local storage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogPreferences", "Local folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowser.setText(QtGui.QApplication.translate("DialogPreferences", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.gbRemote.setTitle(QtGui.QApplication.translate("DialogPreferences", "Remote storage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogPreferences", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogPreferences", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogPreferences", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.txPasswo.setText(QtGui.QApplication.translate("DialogPreferences", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.rbsqlite.setText(QtGui.QApplication.translate("DialogPreferences", "Sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.rbmysql.setText(QtGui.QApplication.translate("DialogPreferences", "MySql", None, QtGui.QApplication.UnicodeUTF8))
        self.rbpostgres.setText(QtGui.QApplication.translate("DialogPreferences", "Postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogPreferences", "Debugging configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDebug.setText(QtGui.QApplication.translate("DialogPreferences", "Debugging enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogPreferences", "Debug level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogPreferences", "Log folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogBrowser.setText(QtGui.QApplication.translate("DialogPreferences", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogPreferences", "Firmware folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFirmwareBrowser.setText(QtGui.QApplication.translate("DialogPreferences", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogPreferences", "Configs folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConfigsBrowser.setText(QtGui.QApplication.translate("DialogPreferences", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTemplatesBrowser.setText(QtGui.QApplication.translate("DialogPreferences", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DialogPreferences", "Templates folder", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("DialogPreferences", "OK", None, QtGui.QApplication.UnicodeUTF8))

import icepapcms_rc
