# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevWXKXZ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"}\n"
"#leftMenuContainer{\n"
"	background-color:#16191d;\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 7px 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#home, #profile, #help, #settings{\n"
"	background-color: #1f232a;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuContainer.setLayoutDirection(Qt.LeftToRight)
        self.leftMenuContainer.setAutoFillBackground(False)
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 228, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.leftMenuContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame_2)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setEnabled(True)
        self.homeButton.setStyleSheet(u"QPushButton {\n"
"	border-left: 2px solid #C6A052;\n"
"	border-bottom: 2px solid #C6A052;\n"
"	border-top: 2px solid #C6A052;\n"
"	background-color: #1f232a;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C6A052;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/Qss/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)

        self.verticalLayout_3.addWidget(self.homeButton)

        self.profileButton = QPushButton(self.frame_2)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setStyleSheet(u"QPushButton {\n"
"	border-left: 2px solid transparent;\n"
"	border-top: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	background-color: #16191d;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C6A052;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Qss/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.profileButton)

        self.helpButton = QPushButton(self.frame_2)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setStyleSheet(u"QPushButton {\n"
"	border-left: 2px solid transparent;\n"
"	border-top: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	background-color: #16191d;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C6A052;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Qss/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon2)
        self.helpButton.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.helpButton)

        self.settingsButton = QPushButton(self.frame_2)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setEnabled(True)
        self.settingsButton.setStyleSheet(u"QPushButton {\n"
"	border-left: 2px solid transparent;\n"
"	border-top: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	background-color: #16191d;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #C6A052;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Qss/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.settingsButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_7 = QFrame(self.leftMenuContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.quitButton = QPushButton(self.frame_7)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #C6A052;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Qss/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quitButton.setIcon(icon4)

        self.verticalLayout_9.addWidget(self.quitButton, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #C6A052;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gamcoinImage = QLabel(self.frame_6)
        self.gamcoinImage.setObjectName(u"gamcoinImage")
        self.gamcoinImage.setMaximumSize(QSize(20, 20))
        self.gamcoinImage.setPixmap(QPixmap(u"images/gamcoin.png"))
        self.gamcoinImage.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.gamcoinImage)

        self.gamcoinText = QLabel(self.frame_6)
        self.gamcoinText.setObjectName(u"gamcoinText")
        font = QFont()
        font.setBold(True)
        self.gamcoinText.setFont(font)

        self.horizontalLayout_11.addWidget(self.gamcoinText)


        self.horizontalLayout_9.addWidget(self.frame_6)

        self.horizontalSpacer_5 = QSpacerItem(628, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.frame_8)
        self.minimizeButton.setObjectName(u"minimizeButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Qss/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.minimizeButton, 0, Qt.AlignRight)

        self.fullscreenButton = QPushButton(self.frame_8)
        self.fullscreenButton.setObjectName(u"fullscreenButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Qss/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreenButton.setIcon(icon6)
        self.fullscreenButton.setIconSize(QSize(16, 16))
        self.fullscreenButton.setFlat(False)

        self.horizontalLayout_10.addWidget(self.fullscreenButton, 0, Qt.AlignRight)

        self.closeButton = QPushButton(self.frame_8)
        self.closeButton.setObjectName(u"closeButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Qss/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.closeButton, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_6 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomQStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bottomMenuSubContainer = QWidget(self.home)
        self.bottomMenuSubContainer.setObjectName(u"bottomMenuSubContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bottomMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.bottomMenuSubContainer.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.bottomMenuSubContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topMenuSubContainer = QWidget(self.bottomMenuSubContainer)
        self.topMenuSubContainer.setObjectName(u"topMenuSubContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.topMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.topMenuSubContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.topMenuSubContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.topMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.CPUText = QLabel(self.frame)
        self.CPUText.setObjectName(u"CPUText")

        self.horizontalLayout_4.addWidget(self.CPUText)

        self.CPUProgressBar = QProgressBar(self.frame)
        self.CPUProgressBar.setObjectName(u"CPUProgressBar")
        self.CPUProgressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #1f232a;\n"
"	border-style: solid;\n"
"	border-color:  #16191d;\n"
"	border-radius: 7px;\n"
"	border-width: 2px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"QProgressBar::Chunk {\n"
"	background-color: #f0f0f0;\n"
"	width: 2px;\n"
"	margin: 1px;\n"
"}")
        self.CPUProgressBar.setValue(24)

        self.horizontalLayout_4.addWidget(self.CPUProgressBar)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.topMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.GPUText = QLabel(self.frame_3)
        self.GPUText.setObjectName(u"GPUText")

        self.horizontalLayout_5.addWidget(self.GPUText)

        self.GPUProgressBar = QProgressBar(self.frame_3)
        self.GPUProgressBar.setObjectName(u"GPUProgressBar")
        self.GPUProgressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #1f232a;\n"
"	border-style: solid;\n"
"	border-color:  #16191d;\n"
"	border-radius: 7px;\n"
"	border-width: 2px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"QProgressBar::Chunk {\n"
"	background-color: #f0f0f0;\n"
"	width: 2px;\n"
"	margin: 1px;\n"
"}")
        self.GPUProgressBar.setValue(24)

        self.horizontalLayout_5.addWidget(self.GPUProgressBar)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.topMenuSubContainer)


        self.verticalLayout_7.addWidget(self.bottomMenuSubContainer)

        self.mainBodySubContainer = QWidget(self.home)
        self.mainBodySubContainer.setObjectName(u"mainBodySubContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainBodySubContainer.sizePolicy().hasHeightForWidth())
        self.mainBodySubContainer.setSizePolicy(sizePolicy5)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodySubContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.mainBodySubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_5.setToolTipDuration(-1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.startButton = QPushButton(self.frame_5)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy6)
        self.startButton.setSizeIncrement(QSize(300, 300))
        font1 = QFont()
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.startButton.setFont(font1)
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.startButton.setMouseTracking(False)
        self.startButton.setFocusPolicy(Qt.StrongFocus)
        self.startButton.setToolTipDuration(1)
        self.startButton.setStyleSheet(u"QPushButton {\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"images/gamcoin_silver.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon8)
        self.startButton.setIconSize(QSize(300, 300))
        self.startButton.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.startButton)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.mainBodySubContainer)

        self.frame_4 = QFrame(self.home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.coinCounter = QLCDNumber(self.frame_4)
        self.coinCounter.setObjectName(u"coinCounter")
        self.coinCounter.setDigitCount(1)
        self.coinCounter.setSegmentStyle(QLCDNumber.Filled)
        self.coinCounter.setProperty("value", 0.000000000000000)

        self.horizontalLayout_6.addWidget(self.coinCounter)

        self.horizontalSpacer = QSpacerItem(222, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.mainPages.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_10 = QVBoxLayout(self.settings)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.mainPages.addWidget(self.settings)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_2 = QVBoxLayout(self.profile)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.profile)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.mainPages.addWidget(self.profile)
        self.help = QWidget()
        self.help.setObjectName(u"help")
        self.verticalLayout_8 = QVBoxLayout(self.help)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.help)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.mainPages.addWidget(self.help)

        self.verticalLayout_6.addWidget(self.mainPages)


        self.verticalLayout_4.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)

        self.fullscreenButton.setDefault(True)
        self.mainPages.setCurrentIndex(0)
        self.startButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText("")
#if QT_CONFIG(tooltip)
        self.profileButton.setToolTip(QCoreApplication.translate("MainWindow", u"help", None))
#endif // QT_CONFIG(tooltip)
        self.profileButton.setText("")
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText("")
#if QT_CONFIG(tooltip)
        self.settingsButton.setToolTip(QCoreApplication.translate("MainWindow", u"settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsButton.setText("")
#if QT_CONFIG(tooltip)
        self.quitButton.setToolTip(QCoreApplication.translate("MainWindow", u"quit", None))
#endif // QT_CONFIG(tooltip)
        self.quitButton.setText("")
        self.gamcoinImage.setText("")
        self.gamcoinText.setText(QCoreApplication.translate("MainWindow", u"GAMcoin miner", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"minimize app", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreenButton.setToolTip(QCoreApplication.translate("MainWindow", u"make app full screen", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreenButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"close app", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.CPUText.setText(QCoreApplication.translate("MainWindow", u"CPU Usage:", None))
        self.GPUText.setText(QCoreApplication.translate("MainWindow", u"GPU Usage:", None))
#if QT_CONFIG(tooltip)
        self.frame_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start Button", None))
#endif // QT_CONFIG(tooltip)
        self.startButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

