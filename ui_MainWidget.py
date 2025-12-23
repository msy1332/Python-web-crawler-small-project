# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import MainWidget_rc

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1200, 800)
        MainWidget.setMinimumSize(QSize(1200, 800))
        MainWidget.setMaximumSize(QSize(1200, 800))
        icon = QIcon()
        icon.addFile(u":/login/res/login/Login.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        MainWidget.setWindowIcon(icon)
        MainWidget.setStyleSheet(u"")
        self.mainWidget = QWidget(MainWidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 1200, 800))
        self.mainWidget.setMinimumSize(QSize(1200, 800))
        self.mainWidget.setMaximumSize(QSize(1200, 800))
        self.horizontalLayout_2 = QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navWidget = QWidget(self.mainWidget)
        self.navWidget.setObjectName(u"navWidget")
        self.navWidget.setStyleSheet(u"#navWidget{\n"
"	background-color: rgba(22, 22, 26,0.2);\n"
"	border-radius: 10px;\n"
"	border-right: 1px solid rgba(61, 62, 66,1)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.navWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qHBoxLayout1 = QHBoxLayout()
        self.qHBoxLayout1.setObjectName(u"qHBoxLayout1")
        self.horizontalSpacer1 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.qHBoxLayout1.addItem(self.horizontalSpacer1)

        self.logoLabel1 = QLabel(self.navWidget)
        self.logoLabel1.setObjectName(u"logoLabel1")
        self.logoLabel1.setMinimumSize(QSize(115, 115))
        self.logoLabel1.setMaximumSize(QSize(115, 115))
        self.logoLabel1.setPixmap(QPixmap(u":/login/res/login/Login.png"))
        self.logoLabel1.setScaledContents(True)

        self.qHBoxLayout1.addWidget(self.logoLabel1)

        self.horizontalSpacer2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.qHBoxLayout1.addItem(self.horizontalSpacer2)


        self.verticalLayout.addLayout(self.qHBoxLayout1)

        self.qHBoxLayout2 = QHBoxLayout()
        self.qHBoxLayout2.setObjectName(u"qHBoxLayout2")
        self.horizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.qHBoxLayout2.addItem(self.horizontalSpacer3)

        self.titleLabel1 = QLabel(self.navWidget)
        self.titleLabel1.setObjectName(u"titleLabel1")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.titleLabel1.setFont(font)
        self.titleLabel1.setStyleSheet(u"QLabel{\n"
"	color: #cbcbcb;\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")

        self.qHBoxLayout2.addWidget(self.titleLabel1)

        self.horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.qHBoxLayout2.addItem(self.horizontalSpacer4)


        self.verticalLayout.addLayout(self.qHBoxLayout2)

        self.NavListWidget = QListWidget(self.navWidget)
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/icons/\u9996\u9875.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        __qlistwidgetitem = QListWidgetItem(self.NavListWidget)
        __qlistwidgetitem.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/icons/\u529f\u80fd\u7ba1\u7406.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.NavListWidget)
        __qlistwidgetitem1.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/icons/res/icons/\u7279\u70b9_\u95ea\u7535\u53d1\u8d27.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.NavListWidget)
        __qlistwidgetitem2.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/icons/res/icons/\u5173\u4e8e.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.NavListWidget)
        __qlistwidgetitem3.setIcon(icon4);
        self.NavListWidget.setObjectName(u"NavListWidget")
        self.NavListWidget.setMinimumSize(QSize(170, 0))
        self.NavListWidget.setMaximumSize(QSize(170, 16777215))
        self.NavListWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"	border: 0px;\n"
"	outline: none;		\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"	height: 50px;\n"
"	padding: 0px 15px;\n"
"	border-radius: 6px;\n"
"	color: #cbcbcb;\n"
"}\n"
"\n"
"QListWidget::item:selected{\n"
"	border-right: 2px solid #e1b9e8;\n"
"	background-color: rgba(35, 36, 41,0.3);\n"
"}")
        self.NavListWidget.setIconSize(QSize(23, 23))

        self.verticalLayout.addWidget(self.NavListWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 12)

        self.horizontalLayout_2.addWidget(self.navWidget)

        self.mainStackedWidget = QStackedWidget(self.mainWidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainStackedWidget.setStyleSheet(u"#ChargingWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.HomeWidget = QWidget()
        self.HomeWidget.setObjectName(u"HomeWidget")
        self.HomeWidget.setStyleSheet(u"#HomeWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.HomeWidget)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.homeHorizontalSpacer1 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.homeHorizontalSpacer1)

        self.homeVerticalLayout1 = QVBoxLayout()
        self.homeVerticalLayout1.setObjectName(u"homeVerticalLayout1")
        self.homeVerticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.homeVerticalLayout1.addItem(self.homeVerticalSpacer1)

        self.homeHorizontalLayout1 = QHBoxLayout()
        self.homeHorizontalLayout1.setObjectName(u"homeHorizontalLayout1")
        self.homeHorizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout1.addItem(self.homeHorizontalSpacer3)

        self.homeLogoLabel1 = QLabel(self.HomeWidget)
        self.homeLogoLabel1.setObjectName(u"homeLogoLabel1")
        self.homeLogoLabel1.setMinimumSize(QSize(154, 154))
        self.homeLogoLabel1.setMaximumSize(QSize(154, 154))
        self.homeLogoLabel1.setPixmap(QPixmap(u":/login/res/login/Login.png"))
        self.homeLogoLabel1.setScaledContents(True)

        self.homeHorizontalLayout1.addWidget(self.homeLogoLabel1)

        self.homeHorizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout1.addItem(self.homeHorizontalSpacer4)


        self.homeVerticalLayout1.addLayout(self.homeHorizontalLayout1)

        self.homeHorizontalLayout2 = QHBoxLayout()
        self.homeHorizontalLayout2.setObjectName(u"homeHorizontalLayout2")
        self.homeHorizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout2.addItem(self.homeHorizontalSpacer5)

        self.homeTitleLabel1 = QLabel(self.HomeWidget)
        self.homeTitleLabel1.setObjectName(u"homeTitleLabel1")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.homeTitleLabel1.setFont(font1)
        self.homeTitleLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255,255,255,0.0)\n"
"}")

        self.homeHorizontalLayout2.addWidget(self.homeTitleLabel1)

        self.homeHorizontalSpacer6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout2.addItem(self.homeHorizontalSpacer6)


        self.homeVerticalLayout1.addLayout(self.homeHorizontalLayout2)

        self.homeHorizontalLayout3 = QHBoxLayout()
        self.homeHorizontalLayout3.setObjectName(u"homeHorizontalLayout3")
        self.homeHorizontalSpacer7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout3.addItem(self.homeHorizontalSpacer7)

        self.homeHorizontalLayout4 = QHBoxLayout()
        self.homeHorizontalLayout4.setObjectName(u"homeHorizontalLayout4")
        self.homeIconLabel1 = QLabel(self.HomeWidget)
        self.homeIconLabel1.setObjectName(u"homeIconLabel1")
        self.homeIconLabel1.setMinimumSize(QSize(30, 30))
        self.homeIconLabel1.setMaximumSize(QSize(30, 30))
        self.homeIconLabel1.setPixmap(QPixmap(u":/icons/res/icons/\u8f6f\u4ef6\u4ecb\u7ecd.png"))
        self.homeIconLabel1.setScaledContents(True)

        self.homeHorizontalLayout4.addWidget(self.homeIconLabel1)

        self.homeTitleLabel2 = QLabel(self.HomeWidget)
        self.homeTitleLabel2.setObjectName(u"homeTitleLabel2")
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.homeTitleLabel2.setFont(font2)
        self.homeTitleLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255,255,255,0.0)\n"
"}")

        self.homeHorizontalLayout4.addWidget(self.homeTitleLabel2)


        self.homeHorizontalLayout3.addLayout(self.homeHorizontalLayout4)

        self.homeHorizontalSpacer8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout3.addItem(self.homeHorizontalSpacer8)


        self.homeVerticalLayout1.addLayout(self.homeHorizontalLayout3)

        self.homeHorizontalLayout5 = QHBoxLayout()
        self.homeHorizontalLayout5.setSpacing(0)
        self.homeHorizontalLayout5.setObjectName(u"homeHorizontalLayout5")
        self.homeHorizontalSpacer9 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout5.addItem(self.homeHorizontalSpacer9)

        self.homeIconLabel2 = QLabel(self.HomeWidget)
        self.homeIconLabel2.setObjectName(u"homeIconLabel2")
        self.homeIconLabel2.setMinimumSize(QSize(30, 40))
        self.homeIconLabel2.setMaximumSize(QSize(40, 40))
        self.homeIconLabel2.setPixmap(QPixmap(u":/icons/res/icons/\u5feb\u624b.png"))
        self.homeIconLabel2.setScaledContents(True)
        self.homeIconLabel2.setOpenExternalLinks(True)

        self.homeHorizontalLayout5.addWidget(self.homeIconLabel2)

        self.homeIconLabel3 = QLabel(self.HomeWidget)
        self.homeIconLabel3.setObjectName(u"homeIconLabel3")
        self.homeIconLabel3.setMinimumSize(QSize(30, 40))
        self.homeIconLabel3.setMaximumSize(QSize(40, 40))
        self.homeIconLabel3.setPixmap(QPixmap(u":/icons/res/icons/\u54d4\u54e9\u54d4\u54e9 (2).png"))
        self.homeIconLabel3.setScaledContents(True)
        self.homeIconLabel3.setOpenExternalLinks(True)

        self.homeHorizontalLayout5.addWidget(self.homeIconLabel3)

        self.homeIconLabel4 = QLabel(self.HomeWidget)
        self.homeIconLabel4.setObjectName(u"homeIconLabel4")
        self.homeIconLabel4.setMinimumSize(QSize(30, 40))
        self.homeIconLabel4.setMaximumSize(QSize(40, 40))
        self.homeIconLabel4.setPixmap(QPixmap(u":/icons/res/icons/\u8c46\u74e31.png"))
        self.homeIconLabel4.setScaledContents(True)
        self.homeIconLabel4.setOpenExternalLinks(True)

        self.homeHorizontalLayout5.addWidget(self.homeIconLabel4)

        self.homeIconLabel5 = QLabel(self.HomeWidget)
        self.homeIconLabel5.setObjectName(u"homeIconLabel5")
        self.homeIconLabel5.setMinimumSize(QSize(40, 40))
        self.homeIconLabel5.setMaximumSize(QSize(40, 40))
        self.homeIconLabel5.setTextFormat(Qt.TextFormat.AutoText)
        self.homeIconLabel5.setScaledContents(True)
        self.homeIconLabel5.setWordWrap(False)
        self.homeIconLabel5.setOpenExternalLinks(True)

        self.homeHorizontalLayout5.addWidget(self.homeIconLabel5)

        self.homeIconLabel6 = QLabel(self.HomeWidget)
        self.homeIconLabel6.setObjectName(u"homeIconLabel6")
        self.homeIconLabel6.setMinimumSize(QSize(30, 40))
        self.homeIconLabel6.setMaximumSize(QSize(40, 40))
        self.homeIconLabel6.setPixmap(QPixmap(u":/icons/res/icons/githubb.png"))
        self.homeIconLabel6.setScaledContents(True)
        self.homeIconLabel6.setOpenExternalLinks(True)

        self.homeHorizontalLayout5.addWidget(self.homeIconLabel6)

        self.homeHorizontalSpacer10 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.homeHorizontalLayout5.addItem(self.homeHorizontalSpacer10)


        self.homeVerticalLayout1.addLayout(self.homeHorizontalLayout5)

        self.homeVerticalSpacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.homeVerticalLayout1.addItem(self.homeVerticalSpacer2)


        self.horizontalLayout_27.addLayout(self.homeVerticalLayout1)

        self.homeHorizontalSpacer2 = QSpacerItem(227, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.homeHorizontalSpacer2)

        self.mainStackedWidget.addWidget(self.HomeWidget)
        self.FunctionWidget = QWidget()
        self.FunctionWidget.setObjectName(u"FunctionWidget")
        self.FunctionWidget.setStyleSheet(u"#FunctionWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.FunctionWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.functionHorizontalLayout1 = QHBoxLayout()
        self.functionHorizontalLayout1.setObjectName(u"functionHorizontalLayout1")
        self.functionHorizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout1.addItem(self.functionHorizontalSpacer1)

        self.functionTitleLabel1 = QLabel(self.FunctionWidget)
        self.functionTitleLabel1.setObjectName(u"functionTitleLabel1")
        self.functionTitleLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: 90px \"Terminal\";\n"
"	font-family: \"\u5b8b\u4f53\";\n"
"	font-weight: bold;\n"
"	letter-spacing: -10px;\n"
"}")

        self.functionHorizontalLayout1.addWidget(self.functionTitleLabel1)

        self.functionHorizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout1.addItem(self.functionHorizontalSpacer2)


        self.verticalLayout_2.addLayout(self.functionHorizontalLayout1)

        self.functionHorizontalLayout2 = QHBoxLayout()
        self.functionHorizontalLayout2.setObjectName(u"functionHorizontalLayout2")
        self.functionHorizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout2.addItem(self.functionHorizontalSpacer3)

        self.functionTitleLabel2 = QLabel(self.FunctionWidget)
        self.functionTitleLabel2.setObjectName(u"functionTitleLabel2")
        self.functionTitleLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: 20px \"Terminal\";\n"
"	font-family: \"\u5b8b\u4f53\";\n"
"	font-weight: bold;\n"
"	letter-spacing: 2px;\n"
"}")

        self.functionHorizontalLayout2.addWidget(self.functionTitleLabel2)

        self.functionHorizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout2.addItem(self.functionHorizontalSpacer4)


        self.verticalLayout_2.addLayout(self.functionHorizontalLayout2)

        self.functionWidgetGroupWidget1 = QWidget(self.FunctionWidget)
        self.functionWidgetGroupWidget1.setObjectName(u"functionWidgetGroupWidget1")
        self.functionWidgetGroupSubControl1 = QWidget(self.functionWidgetGroupWidget1)
        self.functionWidgetGroupSubControl1.setObjectName(u"functionWidgetGroupSubControl1")
        self.functionWidgetGroupSubControl1.setGeometry(QRect(10, 30, 951, 601))
        self.functionWidgetGroupSubControl1.setMinimumSize(QSize(0, 0))
        self.functionWidgetGroupSubControl1.setMaximumSize(QSize(16777215, 16777215))
        self.functionWidgetGroupSubControl1.setStyleSheet(u"#functionWidgetGroupSubControl1{\n"
"	background-color: rgba(35, 36, 41,0.2);\n"
"	border-radius: 6px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.functionWidgetGroupSubControl1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 28, -1, -1)
        self.functionHorizontalLayout3 = QHBoxLayout()
        self.functionHorizontalLayout3.setObjectName(u"functionHorizontalLayout3")
        self.functionHorizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout3.addItem(self.functionHorizontalSpacer5)

        self.functionLabel1 = QLabel(self.functionWidgetGroupSubControl1)
        self.functionLabel1.setObjectName(u"functionLabel1")
        self.functionLabel1.setMinimumSize(QSize(120, 40))
        self.functionLabel1.setMaximumSize(QSize(120, 40))
        self.functionLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"	font-weight: bold;\n"
"}")

        self.functionHorizontalLayout3.addWidget(self.functionLabel1)

        self.platformComboBox = QComboBox(self.functionWidgetGroupSubControl1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/res/icons/\u5feb\u624b-copy.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.platformComboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/res/icons/\u54d4\u54e9\u54d4\u54e9-off.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.platformComboBox.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/res/icons/\u8c46\u74e3.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.platformComboBox.addItem(icon7, "")
        self.platformComboBox.setObjectName(u"platformComboBox")
        self.platformComboBox.setEnabled(True)
        self.platformComboBox.setMinimumSize(QSize(0, 40))
        self.platformComboBox.setMaximumSize(QSize(16777215, 40))
        self.platformComboBox.setStyleSheet(u"QComboBox{\n"
"	height: 40px;\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	background-color: rgba(35, 36, 41,0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{	\n"
"	image: url(:/icons/res/icons/\u4e0b\u7bad\u5934.png);\n"
"	width: 35px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border: 1px solid #54A9FF;\n"
"	background-color: rgb(35, 36, 41);\n"
"	color: white;\n"
"}")

        self.functionHorizontalLayout3.addWidget(self.platformComboBox)

        self.functionHorizontalSpacer6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout3.addItem(self.functionHorizontalSpacer6)

        self.functionHorizontalLayout3.setStretch(1, 1)
        self.functionHorizontalLayout3.setStretch(2, 7)

        self.verticalLayout_3.addLayout(self.functionHorizontalLayout3)

        self.functionHorizontalLayout4 = QHBoxLayout()
        self.functionHorizontalLayout4.setObjectName(u"functionHorizontalLayout4")
        self.functionHorizontalSpacer7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout4.addItem(self.functionHorizontalSpacer7)

        self.functionLabel2 = QLabel(self.functionWidgetGroupSubControl1)
        self.functionLabel2.setObjectName(u"functionLabel2")
        self.functionLabel2.setMinimumSize(QSize(120, 40))
        self.functionLabel2.setMaximumSize(QSize(120, 40))
        self.functionLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"	font-weight: bold;\n"
"}")

        self.functionHorizontalLayout4.addWidget(self.functionLabel2)

        self.horizontalLayout9 = QHBoxLayout()
        self.horizontalLayout9.setSpacing(0)
        self.horizontalLayout9.setObjectName(u"horizontalLayout9")
        self.fileLineEdit = QLineEdit(self.functionWidgetGroupSubControl1)
        self.fileLineEdit.setObjectName(u"fileLineEdit")
        self.fileLineEdit.setEnabled(True)
        self.fileLineEdit.setMinimumSize(QSize(0, 1))
        self.fileLineEdit.setMaximumSize(QSize(16777215, 40))
        self.fileLineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")
        self.fileLineEdit.setReadOnly(True)

        self.horizontalLayout9.addWidget(self.fileLineEdit)

        self.morePushButton = QPushButton(self.functionWidgetGroupSubControl1)
        self.morePushButton.setObjectName(u"morePushButton")
        self.morePushButton.setMinimumSize(QSize(100, 40))
        self.morePushButton.setMaximumSize(QSize(100, 16777215))
        self.morePushButton.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	color: white;\n"
"	font-size: 17px;\n"
"	font-weight: bold;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/res/icons/\u6587\u4ef6\u5939.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.morePushButton.setIcon(icon8)
        self.morePushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout9.addWidget(self.morePushButton)


        self.functionHorizontalLayout4.addLayout(self.horizontalLayout9)

        self.functionHorizontalSpacer8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout4.addItem(self.functionHorizontalSpacer8)

        self.functionHorizontalLayout4.setStretch(1, 1)
        self.functionHorizontalLayout4.setStretch(2, 7)

        self.verticalLayout_3.addLayout(self.functionHorizontalLayout4)

        self.formStackedWidget = QStackedWidget(self.functionWidgetGroupSubControl1)
        self.formStackedWidget.setObjectName(u"formStackedWidget")
        self.formStackedWidget.setStyleSheet(u"QStackedWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"#page1{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.page1)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.functionHorizontalLayout5 = QHBoxLayout()
        self.functionHorizontalLayout5.setObjectName(u"functionHorizontalLayout5")
        self.functionHorizontalSpacer9 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout5.addItem(self.functionHorizontalSpacer9)

        self.functionHorizontalLayout6 = QHBoxLayout()
        self.functionHorizontalLayout6.setObjectName(u"functionHorizontalLayout6")
        self.functionLabel3 = QLabel(self.page1)
        self.functionLabel3.setObjectName(u"functionLabel3")
        self.functionLabel3.setMinimumSize(QSize(120, 40))
        self.functionLabel3.setMaximumSize(QSize(120, 40))
        self.functionLabel3.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"	font-weight: bold;\n"
"}")

        self.functionHorizontalLayout6.addWidget(self.functionLabel3)

        self.videoLineEdit1 = QLineEdit(self.page1)
        self.videoLineEdit1.setObjectName(u"videoLineEdit1")
        self.videoLineEdit1.setMinimumSize(QSize(0, 1))
        self.videoLineEdit1.setMaximumSize(QSize(16777215, 40))
        self.videoLineEdit1.setStyleSheet(u"QLineEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")

        self.functionHorizontalLayout6.addWidget(self.videoLineEdit1)


        self.functionHorizontalLayout5.addLayout(self.functionHorizontalLayout6)

        self.functionHorizontalSpacer10 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout5.addItem(self.functionHorizontalSpacer10)


        self.verticalLayout_6.addLayout(self.functionHorizontalLayout5)

        self.functionLogTextEdit1 = QTextEdit(self.page1)
        self.functionLogTextEdit1.setObjectName(u"functionLogTextEdit1")
        self.functionLogTextEdit1.setStyleSheet(u"QTextEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	color: white;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")
        self.functionLogTextEdit1.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.functionLogTextEdit1)

        self.formStackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setStyleSheet(u"#page2{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.page2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.functionHorizontalLayout7 = QHBoxLayout()
        self.functionHorizontalLayout7.setSpacing(0)
        self.functionHorizontalLayout7.setObjectName(u"functionHorizontalLayout7")
        self.functionHorizontalSpacer11 = QSpacerItem(42, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout7.addItem(self.functionHorizontalSpacer11)

        self.functionHorizontalLayout8 = QHBoxLayout()
        self.functionHorizontalLayout8.setObjectName(u"functionHorizontalLayout8")
        self.functionLabel4 = QLabel(self.page2)
        self.functionLabel4.setObjectName(u"functionLabel4")
        self.functionLabel4.setMinimumSize(QSize(125, 40))
        self.functionLabel4.setMaximumSize(QSize(125, 40))
        self.functionLabel4.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"	font-weight: bold;\n"
"}")

        self.functionHorizontalLayout8.addWidget(self.functionLabel4)

        self.videoLineEdit2 = QLineEdit(self.page2)
        self.videoLineEdit2.setObjectName(u"videoLineEdit2")
        self.videoLineEdit2.setMinimumSize(QSize(0, 1))
        self.videoLineEdit2.setMaximumSize(QSize(16777215, 40))
        self.videoLineEdit2.setStyleSheet(u"QLineEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")

        self.functionHorizontalLayout8.addWidget(self.videoLineEdit2)


        self.functionHorizontalLayout7.addLayout(self.functionHorizontalLayout8)

        self.functionHorizontalSpacer12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout7.addItem(self.functionHorizontalSpacer12)


        self.verticalLayout_5.addLayout(self.functionHorizontalLayout7)

        self.functionHorizontalLayout9 = QHBoxLayout()
        self.functionHorizontalLayout9.setSpacing(0)
        self.functionHorizontalLayout9.setObjectName(u"functionHorizontalLayout9")
        self.functionHorizontalSpacer13 = QSpacerItem(42, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout9.addItem(self.functionHorizontalSpacer13)

        self.functionHorizontalLayout10 = QHBoxLayout()
        self.functionHorizontalLayout10.setObjectName(u"functionHorizontalLayout10")
        self.functionLabel5 = QLabel(self.page2)
        self.functionLabel5.setObjectName(u"functionLabel5")
        self.functionLabel5.setMinimumSize(QSize(125, 40))
        self.functionLabel5.setMaximumSize(QSize(125, 40))
        self.functionLabel5.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"	font-weight: bold;\n"
"}")

        self.functionHorizontalLayout10.addWidget(self.functionLabel5)

        self.ClarityComboBox = QComboBox(self.page2)
        self.ClarityComboBox.setObjectName(u"ClarityComboBox")
        self.ClarityComboBox.setEnabled(True)
        self.ClarityComboBox.setStyleSheet(u"QComboBox{\n"
"	height: 40px;\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	background-color: rgba(35, 36, 41,0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{	\n"
"	image: url(:/icons/res/icons/\u4e0b\u7bad\u5934.png);\n"
"	width: 35px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border: 1px solid #54A9FF;\n"
"	background-color: rgb(35, 36, 41);\n"
"	color: white;\n"
"}")

        self.functionHorizontalLayout10.addWidget(self.ClarityComboBox)


        self.functionHorizontalLayout9.addLayout(self.functionHorizontalLayout10)

        self.functionHorizontalSpacer14 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout9.addItem(self.functionHorizontalSpacer14)


        self.verticalLayout_5.addLayout(self.functionHorizontalLayout9)

        self.functionLogTextEdit2 = QTextEdit(self.page2)
        self.functionLogTextEdit2.setObjectName(u"functionLogTextEdit2")
        self.functionLogTextEdit2.setStyleSheet(u"QTextEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	color: white;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")
        self.functionLogTextEdit2.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.functionLogTextEdit2)

        self.formStackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.page3.setStyleSheet(u"#page3{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.functionLogTextEdit3 = QTextEdit(self.page3)
        self.functionLogTextEdit3.setObjectName(u"functionLogTextEdit3")
        self.functionLogTextEdit3.setStyleSheet(u"QTextEdit{\n"
"	border: 0px;\n"
"	outline: none;\n"
"	border-radius: 6px;\n"
"	padding: 0px 20px;\n"
"	font-size: 15px;\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	color: white;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border: 1px solid #54A9FF;\n"
"}\n"
"")
        self.functionLogTextEdit3.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.functionLogTextEdit3)

        self.formStackedWidget.addWidget(self.page3)

        self.verticalLayout_3.addWidget(self.formStackedWidget)

        self.functionHorizontalLayout11 = QHBoxLayout()
        self.functionHorizontalLayout11.setObjectName(u"functionHorizontalLayout11")
        self.functionHorizontalSpacer15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout11.addItem(self.functionHorizontalSpacer15)

        self.progressBar = QProgressBar(self.functionWidgetGroupSubControl1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border: 0px;\n"
"	outline: 0px;\n"
"	background-color: rgba(255,255,255,0.0);\n"
"	border-radius: 8px;\n"
"	border: 1px solid rgba(255,255,255,0.3);;\n"
"	color: black;\n"
"	font-size: 13pt;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border-radius: 8px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.functionHorizontalLayout11.addWidget(self.progressBar)

        self.functionHorizontalSpacer16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout11.addItem(self.functionHorizontalSpacer16)


        self.verticalLayout_3.addLayout(self.functionHorizontalLayout11)

        self.functionHorizontalLayout12 = QHBoxLayout()
        self.functionHorizontalLayout12.setObjectName(u"functionHorizontalLayout12")
        self.functionHorizontalSpacer17 = QSpacerItem(300, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout12.addItem(self.functionHorizontalSpacer17)

        self.startPushButton = QPushButton(self.functionWidgetGroupSubControl1)
        self.startPushButton.setObjectName(u"startPushButton")
        self.startPushButton.setMinimumSize(QSize(0, 40))
        self.startPushButton.setStyleSheet(u"QPushButton{\n"
"	border: 0;\n"
"	outline: 0;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	background-color: rgba(35, 36, 41,0.3);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		background-color: rgba(35, 36, 41,0.5);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"		background-color: rgba(35, 36, 41,0.3);\n"
"}")

        self.functionHorizontalLayout12.addWidget(self.startPushButton)

        self.functionHorizontalSpacer18 = QSpacerItem(300, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.functionHorizontalLayout12.addItem(self.functionHorizontalSpacer18)


        self.verticalLayout_3.addLayout(self.functionHorizontalLayout12)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 5)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)

        self.verticalLayout_2.addWidget(self.functionWidgetGroupWidget1)

        self.verticalLayout_2.setStretch(2, 5)
        self.mainStackedWidget.addWidget(self.FunctionWidget)
        self.ChargingWidget = QWidget()
        self.ChargingWidget.setObjectName(u"ChargingWidget")
        self.ChargingWidget.setStyleSheet(u"#ChargingWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.ChargingWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.chargingHorizontalLayout1 = QHBoxLayout()
        self.chargingHorizontalLayout1.setObjectName(u"chargingHorizontalLayout1")
        self.chargingHorizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout1.addItem(self.chargingHorizontalSpacer1)

        self.chargingTitleLabel1 = QLabel(self.ChargingWidget)
        self.chargingTitleLabel1.setObjectName(u"chargingTitleLabel1")
        self.chargingTitleLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 30pt \"Terminal\";\n"
"	font-size: 30pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.chargingTitleLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingHorizontalLayout1.addWidget(self.chargingTitleLabel1)

        self.chargingHorizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout1.addItem(self.chargingHorizontalSpacer2)


        self.verticalLayout_15.addLayout(self.chargingHorizontalLayout1)

        self.chargingHorizontalLayout2 = QHBoxLayout()
        self.chargingHorizontalLayout2.setObjectName(u"chargingHorizontalLayout2")
        self.chargingHorizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout2.addItem(self.chargingHorizontalSpacer3)

        self.chargingTitleLabel2 = QLabel(self.ChargingWidget)
        self.chargingTitleLabel2.setObjectName(u"chargingTitleLabel2")
        self.chargingTitleLabel2.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Microsoft JhengHei"])
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setItalic(False)
        self.chargingTitleLabel2.setFont(font3)
        self.chargingTitleLabel2.setStyleSheet(u"QLabel{\n"
"		color: white;\n"
"}")
        self.chargingTitleLabel2.setMidLineWidth(0)
        self.chargingTitleLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingHorizontalLayout2.addWidget(self.chargingTitleLabel2)

        self.chargingHorizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout2.addItem(self.chargingHorizontalSpacer4)


        self.verticalLayout_15.addLayout(self.chargingHorizontalLayout2)

        self.chargingHorizontalLayout3 = QHBoxLayout()
        self.chargingHorizontalLayout3.setObjectName(u"chargingHorizontalLayout3")
        self.chargingHorizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout3.addItem(self.chargingHorizontalSpacer5)

        self.chargingTextLabel1 = QLabel(self.ChargingWidget)
        self.chargingTextLabel1.setObjectName(u"chargingTextLabel1")
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(16)
        font4.setItalic(True)
        self.chargingTextLabel1.setFont(font4)
        self.chargingTextLabel1.setStyleSheet(u"QLabel{\n"
"		color: white;\n"
"}")
        self.chargingTextLabel1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.chargingTextLabel1.setWordWrap(False)

        self.chargingHorizontalLayout3.addWidget(self.chargingTextLabel1)

        self.chargingHorizontalSpacer6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout3.addItem(self.chargingHorizontalSpacer6)


        self.verticalLayout_15.addLayout(self.chargingHorizontalLayout3)

        self.chargingHorizontalLayout4 = QHBoxLayout()
        self.chargingHorizontalLayout4.setObjectName(u"chargingHorizontalLayout4")
        self.chargingHorizontalSpacer7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout4.addItem(self.chargingHorizontalSpacer7)

        self.chargingVerticalLayout1 = QVBoxLayout()
        self.chargingVerticalLayout1.setObjectName(u"chargingVerticalLayout1")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.chargingVerticalLayout1.addItem(self.verticalSpacer)

        self.chargingHorizontalLayout5 = QHBoxLayout()
        self.chargingHorizontalLayout5.setObjectName(u"chargingHorizontalLayout5")
        self.chargingVerticalLayout2 = QVBoxLayout()
        self.chargingVerticalLayout2.setObjectName(u"chargingVerticalLayout2")
        self.chargingQrcodeLabel1 = QLabel(self.ChargingWidget)
        self.chargingQrcodeLabel1.setObjectName(u"chargingQrcodeLabel1")
        self.chargingQrcodeLabel1.setMinimumSize(QSize(173, 164))
        self.chargingQrcodeLabel1.setMaximumSize(QSize(173, 164))
        self.chargingQrcodeLabel1.setPixmap(QPixmap(u":/QrCode/res/QrCode/wx.png"))
        self.chargingQrcodeLabel1.setScaledContents(True)
        self.chargingQrcodeLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout2.addWidget(self.chargingQrcodeLabel1)

        self.chargingLabel1 = QLabel(self.ChargingWidget)
        self.chargingLabel1.setObjectName(u"chargingLabel1")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.chargingLabel1.setFont(font5)
        self.chargingLabel1.setStyleSheet(u"QLabel{\n"
"	color: #dbffb5;\n"
"}")
        self.chargingLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout2.addWidget(self.chargingLabel1)


        self.chargingHorizontalLayout5.addLayout(self.chargingVerticalLayout2)

        self.chargingHorizontalSpacer9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout5.addItem(self.chargingHorizontalSpacer9)

        self.chargingLabel2 = QLabel(self.ChargingWidget)
        self.chargingLabel2.setObjectName(u"chargingLabel2")
        self.chargingLabel2.setFont(font5)
        self.chargingLabel2.setStyleSheet(u"QLabel{\n"
"	color: #f2dea3;\n"
"}")
        self.chargingLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingHorizontalLayout5.addWidget(self.chargingLabel2)

        self.chargingHorizontalSpacer10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout5.addItem(self.chargingHorizontalSpacer10)

        self.chargingVerticalLayout3 = QVBoxLayout()
        self.chargingVerticalLayout3.setObjectName(u"chargingVerticalLayout3")
        self.chargingQrcodeLabel2 = QLabel(self.ChargingWidget)
        self.chargingQrcodeLabel2.setObjectName(u"chargingQrcodeLabel2")
        self.chargingQrcodeLabel2.setMinimumSize(QSize(173, 164))
        self.chargingQrcodeLabel2.setMaximumSize(QSize(173, 164))
        self.chargingQrcodeLabel2.setPixmap(QPixmap(u":/QrCode/res/QrCode/zfb.jpg"))
        self.chargingQrcodeLabel2.setScaledContents(True)
        self.chargingQrcodeLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout3.addWidget(self.chargingQrcodeLabel2)

        self.chargingLabel3 = QLabel(self.ChargingWidget)
        self.chargingLabel3.setObjectName(u"chargingLabel3")
        self.chargingLabel3.setFont(font5)
        self.chargingLabel3.setStyleSheet(u"QLabel{\n"
"	color: #b1fcff;\n"
"}")
        self.chargingLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout3.addWidget(self.chargingLabel3)


        self.chargingHorizontalLayout5.addLayout(self.chargingVerticalLayout3)


        self.chargingVerticalLayout1.addLayout(self.chargingHorizontalLayout5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.chargingVerticalLayout1.addItem(self.verticalSpacer_2)


        self.chargingHorizontalLayout4.addLayout(self.chargingVerticalLayout1)

        self.chargingHorizontalSpacer8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout4.addItem(self.chargingHorizontalSpacer8)


        self.verticalLayout_15.addLayout(self.chargingHorizontalLayout4)

        self.chargingWidgetGroupWidget1 = QWidget(self.ChargingWidget)
        self.chargingWidgetGroupWidget1.setObjectName(u"chargingWidgetGroupWidget1")
        self.chargingWidgetGroupSubControl1 = QWidget(self.chargingWidgetGroupWidget1)
        self.chargingWidgetGroupSubControl1.setObjectName(u"chargingWidgetGroupSubControl1")
        self.chargingWidgetGroupSubControl1.setGeometry(QRect(0, 20, 921, 191))
        self.chargingWidgetGroupSubControl1.setMinimumSize(QSize(0, 0))
        self.chargingWidgetGroupSubControl1.setMaximumSize(QSize(16777215, 16777215))
        self.chargingWidgetGroupSubControl1.setStyleSheet(u"#chargingWidgetGroupSubControl1{\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border-radius: 6px;\n"
"	color: white;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.chargingWidgetGroupSubControl1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_3 = QSpacerItem(30, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.chargingHorizontalLayout6 = QHBoxLayout()
        self.chargingHorizontalLayout6.setObjectName(u"chargingHorizontalLayout6")
        self.chargingHorizontalSpacer11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout6.addItem(self.chargingHorizontalSpacer11)

        self.chargingHorizontalLayout7 = QHBoxLayout()
        self.chargingHorizontalLayout7.setObjectName(u"chargingHorizontalLayout7")
        self.chargingVerticalLayout4 = QVBoxLayout()
        self.chargingVerticalLayout4.setSpacing(10)
        self.chargingVerticalLayout4.setObjectName(u"chargingVerticalLayout4")
        self.chargingQrcodeLabel3 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingQrcodeLabel3.setObjectName(u"chargingQrcodeLabel3")
        self.chargingQrcodeLabel3.setMinimumSize(QSize(120, 110))
        self.chargingQrcodeLabel3.setMaximumSize(QSize(120, 110))
        self.chargingQrcodeLabel3.setPixmap(QPixmap(u":/QrCode/res/QrCode/wxCode.jpg"))
        self.chargingQrcodeLabel3.setScaledContents(True)
        self.chargingQrcodeLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout4.addWidget(self.chargingQrcodeLabel3)

        self.chargingLabel4 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingLabel4.setObjectName(u"chargingLabel4")
        self.chargingLabel4.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 12pt;\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-weight: bold;\n"
"}")
        self.chargingLabel4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout4.addWidget(self.chargingLabel4)

        self.chargingVerticalLayout4.setStretch(0, 4)
        self.chargingVerticalLayout4.setStretch(1, 1)

        self.chargingHorizontalLayout7.addLayout(self.chargingVerticalLayout4)

        self.chargingHorizontalSpacer12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout7.addItem(self.chargingHorizontalSpacer12)

        self.chargingVerticalLayout5 = QVBoxLayout()
        self.chargingVerticalLayout5.setSpacing(10)
        self.chargingVerticalLayout5.setObjectName(u"chargingVerticalLayout5")
        self.chargingQrcodeLabel4 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingQrcodeLabel4.setObjectName(u"chargingQrcodeLabel4")
        self.chargingQrcodeLabel4.setMinimumSize(QSize(120, 110))
        self.chargingQrcodeLabel4.setMaximumSize(QSize(120, 110))
        self.chargingQrcodeLabel4.setPixmap(QPixmap(u":/QrCode/res/QrCode/qqCode.jpg"))
        self.chargingQrcodeLabel4.setScaledContents(True)
        self.chargingQrcodeLabel4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout5.addWidget(self.chargingQrcodeLabel4)

        self.chargingLabel5 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingLabel5.setObjectName(u"chargingLabel5")
        self.chargingLabel5.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 12pt;\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-weight: bold;\n"
"}")
        self.chargingLabel5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingVerticalLayout5.addWidget(self.chargingLabel5)

        self.chargingVerticalLayout5.setStretch(0, 4)
        self.chargingVerticalLayout5.setStretch(1, 1)

        self.chargingHorizontalLayout7.addLayout(self.chargingVerticalLayout5)


        self.chargingHorizontalLayout6.addLayout(self.chargingHorizontalLayout7)

        self.chargingHorizontalSpacer13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout6.addItem(self.chargingHorizontalSpacer13)

        self.chargingVerticalLayout6 = QVBoxLayout()
        self.chargingVerticalLayout6.setObjectName(u"chargingVerticalLayout6")
        self.chargingHorizontalLayout8 = QHBoxLayout()
        self.chargingHorizontalLayout8.setObjectName(u"chargingHorizontalLayout8")
        self.chargingHorizontalSpacer14 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout8.addItem(self.chargingHorizontalSpacer14)

        self.chargingLabel6 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingLabel6.setObjectName(u"chargingLabel6")
        self.chargingLabel6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 12pt;\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-weight: bold;\n"
"}")
        self.chargingLabel6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.chargingHorizontalLayout8.addWidget(self.chargingLabel6)

        self.chargingHorizontalSpacer15 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout8.addItem(self.chargingHorizontalSpacer15)


        self.chargingVerticalLayout6.addLayout(self.chargingHorizontalLayout8)

        self.chargingHorizontalLayout9 = QHBoxLayout()
        self.chargingHorizontalLayout9.setObjectName(u"chargingHorizontalLayout9")
        self.chargingHorizontalSpacer16 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout9.addItem(self.chargingHorizontalSpacer16)

        self.chargingLabel7 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingLabel7.setObjectName(u"chargingLabel7")
        self.chargingLabel7.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 12pt;\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-weight: bold;\n"
"}")
        self.chargingLabel7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.chargingHorizontalLayout9.addWidget(self.chargingLabel7)

        self.chargingHorizontalSpacer17 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout9.addItem(self.chargingHorizontalSpacer17)


        self.chargingVerticalLayout6.addLayout(self.chargingHorizontalLayout9)

        self.chargingHorizontalLayout10 = QHBoxLayout()
        self.chargingHorizontalLayout10.setSpacing(0)
        self.chargingHorizontalLayout10.setObjectName(u"chargingHorizontalLayout10")
        self.chargingHorizontalSpacer18 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout10.addItem(self.chargingHorizontalSpacer18)

        self.chargingLabel8 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingLabel8.setObjectName(u"chargingLabel8")
        self.chargingLabel8.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 12pt;\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-weight: bold;\n"
"}")
        self.chargingLabel8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.chargingHorizontalLayout10.addWidget(self.chargingLabel8)

        self.chargingHorizontalSpacer19 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout10.addItem(self.chargingHorizontalSpacer19)


        self.chargingVerticalLayout6.addLayout(self.chargingHorizontalLayout10)


        self.chargingHorizontalLayout6.addLayout(self.chargingVerticalLayout6)

        self.chargingHorizontalSpacer20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout6.addItem(self.chargingHorizontalSpacer20)

        self.chargingBgLabel1 = QLabel(self.chargingWidgetGroupSubControl1)
        self.chargingBgLabel1.setObjectName(u"chargingBgLabel1")
        self.chargingBgLabel1.setMinimumSize(QSize(133, 133))
        self.chargingBgLabel1.setMaximumSize(QSize(133, 133))
        self.chargingBgLabel1.setPixmap(QPixmap(u":/background/res/background/bg4.jpg"))
        self.chargingBgLabel1.setScaledContents(True)
        self.chargingBgLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chargingHorizontalLayout6.addWidget(self.chargingBgLabel1)

        self.chargingHorizontalSpacer21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chargingHorizontalLayout6.addItem(self.chargingHorizontalSpacer21)


        self.verticalLayout_14.addLayout(self.chargingHorizontalLayout6)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.verticalLayout_14.setStretch(0, 2)
        self.verticalLayout_14.setStretch(1, 5)
        self.verticalLayout_14.setStretch(2, 1)

        self.verticalLayout_15.addWidget(self.chargingWidgetGroupWidget1)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 4)
        self.verticalLayout_15.setStretch(3, 6)
        self.verticalLayout_15.setStretch(4, 5)
        self.mainStackedWidget.addWidget(self.ChargingWidget)
        self.AboutWidget = QWidget()
        self.AboutWidget.setObjectName(u"AboutWidget")
        self.AboutWidget.setStyleSheet(u"#AboutWidget{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.AboutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AboutWidgetLeft = QWidget(self.AboutWidget)
        self.AboutWidgetLeft.setObjectName(u"AboutWidgetLeft")
        self.AboutWidgetLeft.setStyleSheet(u"#AboutWidgetLeft{\n"
"	border-right: 1px solid #bbbbbb;\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.aboutTitleLabel1 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel1.setObjectName(u"aboutTitleLabel1")
        self.aboutTitleLabel1.setGeometry(QRect(40, 0, 371, 61))
        self.aboutTitleLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 45pt \"Terminal\";\n"
"	font-size: 45pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutTitleLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutTextLabel3 = QLabel(self.AboutWidgetLeft)
        self.aboutTextLabel3.setObjectName(u"aboutTextLabel3")
        self.aboutTextLabel3.setGeometry(QRect(20, 500, 411, 141))
        font6 = QFont()
        font6.setFamilies([u"\u6977\u4f53"])
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setItalic(True)
        self.aboutTextLabel3.setFont(font6)
        self.aboutTextLabel3.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel3.setWordWrap(True)
        self.aboutTextLabel3.setOpenExternalLinks(False)
        self.aboutTextLabel1 = QLabel(self.AboutWidgetLeft)
        self.aboutTextLabel1.setObjectName(u"aboutTextLabel1")
        self.aboutTextLabel1.setGeometry(QRect(30, 160, 411, 81))
        self.aboutTextLabel1.setFont(font6)
        self.aboutTextLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel1.setWordWrap(True)
        self.aboutIconLabel4 = QLabel(self.AboutWidgetLeft)
        self.aboutIconLabel4.setObjectName(u"aboutIconLabel4")
        self.aboutIconLabel4.setGeometry(QRect(150, 470, 34, 34))
        self.aboutIconLabel4.setMinimumSize(QSize(34, 34))
        self.aboutIconLabel4.setMaximumSize(QSize(34, 34))
        self.aboutIconLabel4.setPixmap(QPixmap(u":/icons/res/icons/\u8b66\u793a \u611f\u53f9\u53f7 \uff012.png"))
        self.aboutIconLabel4.setScaledContents(True)
        self.aboutIconLabel5 = QLabel(self.AboutWidgetLeft)
        self.aboutIconLabel5.setObjectName(u"aboutIconLabel5")
        self.aboutIconLabel5.setGeometry(QRect(280, 470, 34, 34))
        self.aboutIconLabel5.setMinimumSize(QSize(34, 34))
        self.aboutIconLabel5.setMaximumSize(QSize(34, 34))
        self.aboutIconLabel5.setPixmap(QPixmap(u":/icons/res/icons/\u8b66\u793a \u611f\u53f9\u53f7 \uff012.png"))
        self.aboutIconLabel5.setScaledContents(True)
        self.aboutTitleLabel6 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel6.setObjectName(u"aboutTitleLabel6")
        self.aboutTitleLabel6.setGeometry(QRect(180, 470, 91, 31))
        font7 = QFont()
        font7.setFamilies([u"\u6977\u4f53"])
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setItalic(True)
        self.aboutTitleLabel6.setFont(font7)
        self.aboutTitleLabel6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 16pt \"Terminal\";\n"
"	font-size: 16pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutTitleLabel6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutTitleLabel2 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel2.setObjectName(u"aboutTitleLabel2")
        self.aboutTitleLabel2.setGeometry(QRect(80, 60, 301, 21))
        font8 = QFont()
        font8.setFamilies([u"\u6977\u4f53"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(True)
        font8.setUnderline(True)
        self.aboutTitleLabel2.setFont(font8)
        self.aboutTitleLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 12pt \"Terminal\";\n"
"	font-size: 12pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutTitleLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutIconLabel3 = QLabel(self.AboutWidgetLeft)
        self.aboutIconLabel3.setObjectName(u"aboutIconLabel3")
        self.aboutIconLabel3.setGeometry(QRect(10, 250, 28, 28))
        self.aboutIconLabel3.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel3.setMaximumSize(QSize(28, 28))
        self.aboutIconLabel3.setPixmap(QPixmap(u":/icons/res/icons/\u6807\u7b7e.png"))
        self.aboutIconLabel3.setScaledContents(True)
        self.aboutTitleLabel5 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel5.setObjectName(u"aboutTitleLabel5")
        self.aboutTitleLabel5.setGeometry(QRect(40, 260, 101, 16))
        self.aboutTitleLabel5.setFont(font7)
        self.aboutTitleLabel5.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 16pt \"Terminal\";\n"
"	font-size: 16pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutTitleLabel3 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel3.setObjectName(u"aboutTitleLabel3")
        self.aboutTitleLabel3.setGeometry(QRect(110, 90, 281, 31))
        font9 = QFont()
        font9.setFamilies([u"\u6977\u4f53"])
        font9.setPointSize(25)
        font9.setBold(False)
        font9.setItalic(True)
        self.aboutTitleLabel3.setFont(font9)
        self.aboutTitleLabel3.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 25pt \"Terminal\";\n"
"	font-size: 25pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutIconLabel1 = QLabel(self.AboutWidgetLeft)
        self.aboutIconLabel1.setObjectName(u"aboutIconLabel1")
        self.aboutIconLabel1.setGeometry(QRect(50, 80, 50, 40))
        self.aboutIconLabel1.setMinimumSize(QSize(50, 40))
        self.aboutIconLabel1.setMaximumSize(QSize(50, 40))
        self.aboutIconLabel1.setPixmap(QPixmap(u":/icons/res/icons/\u8b66\u544a\u4fe1\u53f7_1765287342.png"))
        self.aboutIconLabel1.setScaledContents(True)
        self.aboutIconLabel2 = QLabel(self.AboutWidgetLeft)
        self.aboutIconLabel2.setObjectName(u"aboutIconLabel2")
        self.aboutIconLabel2.setGeometry(QRect(9, 130, 28, 28))
        self.aboutIconLabel2.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel2.setMaximumSize(QSize(28, 28))
        self.aboutIconLabel2.setPixmap(QPixmap(u":/icons/res/icons/\u6807\u7b7e.png"))
        self.aboutIconLabel2.setScaledContents(True)
        self.aboutTitleLabel4 = QLabel(self.AboutWidgetLeft)
        self.aboutTitleLabel4.setObjectName(u"aboutTitleLabel4")
        self.aboutTitleLabel4.setGeometry(QRect(43, 139, 111, 16))
        self.aboutTitleLabel4.setFont(font7)
        self.aboutTitleLabel4.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 16pt \"Terminal\";\n"
"	font-size: 16pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutTextLabel2 = QLabel(self.AboutWidgetLeft)
        self.aboutTextLabel2.setObjectName(u"aboutTextLabel2")
        self.aboutTextLabel2.setGeometry(QRect(30, 290, 401, 171))
        self.aboutTextLabel2.setFont(font6)
        self.aboutTextLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel2.setWordWrap(True)
        self.aboutTextLabel2.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.AboutWidgetLeft)

        self.AboutWidgeRight = QWidget(self.AboutWidget)
        self.AboutWidgeRight.setObjectName(u"AboutWidgeRight")
        self.AboutWidgeRight.setStyleSheet(u"#AboutWidgeRight{\n"
"	background-color: rgba(255,255,255,0.0);\n"
"}")
        self.aboutTextLabel9 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel9.setObjectName(u"aboutTextLabel9")
        self.aboutTextLabel9.setGeometry(QRect(80, 420, 211, 16))
        font10 = QFont()
        font10.setFamilies([u"\u65b0\u5b8b\u4f53"])
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setItalic(True)
        self.aboutTextLabel9.setFont(font10)
        self.aboutTextLabel9.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel9.setWordWrap(True)
        self.aboutIconLabel12 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel12.setObjectName(u"aboutIconLabel12")
        self.aboutIconLabel12.setGeometry(QRect(45, 410, 31, 31))
        self.aboutIconLabel12.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel12.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel12.setPixmap(QPixmap(u":/icons/res/icons/\u7f16\u7a0b_1765287508.png"))
        self.aboutIconLabel12.setScaledContents(True)
        self.aboutIconLabel10 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel10.setObjectName(u"aboutIconLabel10")
        self.aboutIconLabel10.setGeometry(QRect(50, 300, 41, 41))
        self.aboutIconLabel10.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel10.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel10.setPixmap(QPixmap(u":/icons/res/icons/\u5c3a\u5b50_1765286922.png"))
        self.aboutIconLabel10.setScaledContents(True)
        self.aboutTextLabel7 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel7.setObjectName(u"aboutTextLabel7")
        self.aboutTextLabel7.setGeometry(QRect(90, 300, 381, 61))
        self.aboutTextLabel7.setFont(font10)
        self.aboutTextLabel7.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel7.setWordWrap(True)
        self.aboutTitleLabel8 = QLabel(self.AboutWidgeRight)
        self.aboutTitleLabel8.setObjectName(u"aboutTitleLabel8")
        self.aboutTitleLabel8.setGeometry(QRect(30, 90, 411, 31))
        font11 = QFont()
        font11.setFamilies([u"\u6977\u4f53"])
        font11.setPointSize(20)
        font11.setBold(True)
        font11.setItalic(True)
        self.aboutTitleLabel8.setFont(font11)
        self.aboutTitleLabel8.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTitleLabel8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutIconLabel11 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel11.setObjectName(u"aboutIconLabel11")
        self.aboutIconLabel11.setGeometry(QRect(30, 360, 41, 41))
        self.aboutIconLabel11.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel11.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel11.setPixmap(QPixmap(u":/icons/res/icons/\u670d\u52a1\u5668_1765287820.png"))
        self.aboutIconLabel11.setScaledContents(True)
        self.aboutTextLabel8 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel8.setObjectName(u"aboutTextLabel8")
        self.aboutTextLabel8.setGeometry(QRect(80, 370, 121, 31))
        self.aboutTextLabel8.setFont(font10)
        self.aboutTextLabel8.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel8.setWordWrap(True)
        self.aboutIconLabel6 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel6.setObjectName(u"aboutIconLabel6")
        self.aboutIconLabel6.setGeometry(QRect(330, 0, 81, 71))
        self.aboutIconLabel6.setMinimumSize(QSize(50, 40))
        self.aboutIconLabel6.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel6.setPixmap(QPixmap(u":/icons/res/icons/quill-pen-fill.png"))
        self.aboutIconLabel6.setScaledContents(True)
        self.aboutTitleLabel7 = QLabel(self.AboutWidgeRight)
        self.aboutTitleLabel7.setObjectName(u"aboutTitleLabel7")
        self.aboutTitleLabel7.setGeometry(QRect(90, 10, 231, 61))
        font12 = QFont()
        font12.setFamilies([u"\u6977\u4f53"])
        font12.setPointSize(40)
        font12.setBold(True)
        font12.setItalic(True)
        self.aboutTitleLabel7.setFont(font12)
        self.aboutTitleLabel7.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTitleLabel7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutIconLabel8 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel8.setObjectName(u"aboutIconLabel8")
        self.aboutIconLabel8.setGeometry(QRect(50, 200, 41, 41))
        self.aboutIconLabel8.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel8.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel8.setPixmap(QPixmap(u":/icons/res/icons/\u8718\u86db\u56fe\u6807_1765287604.png"))
        self.aboutIconLabel8.setScaledContents(True)
        self.aboutTextLabel5 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel5.setObjectName(u"aboutTextLabel5")
        self.aboutTextLabel5.setGeometry(QRect(90, 200, 381, 41))
        self.aboutTextLabel5.setFont(font10)
        self.aboutTextLabel5.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel5.setWordWrap(True)
        self.aboutIconLabel9 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel9.setObjectName(u"aboutIconLabel9")
        self.aboutIconLabel9.setGeometry(QRect(30, 250, 41, 41))
        self.aboutIconLabel9.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel9.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel9.setPixmap(QPixmap(u":/icons/res/icons/\u989c\u6599\u8c03\u8272\u76d8_1765286791.png"))
        self.aboutIconLabel9.setScaledContents(True)
        self.aboutTextLabel6 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel6.setObjectName(u"aboutTextLabel6")
        self.aboutTextLabel6.setGeometry(QRect(80, 250, 261, 31))
        self.aboutTextLabel6.setFont(font10)
        self.aboutTextLabel6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel6.setWordWrap(True)
        self.aboutIconLabel7 = QLabel(self.AboutWidgeRight)
        self.aboutIconLabel7.setObjectName(u"aboutIconLabel7")
        self.aboutIconLabel7.setGeometry(QRect(30, 150, 51, 51))
        self.aboutIconLabel7.setMinimumSize(QSize(28, 28))
        self.aboutIconLabel7.setMaximumSize(QSize(16777215, 16777215))
        self.aboutIconLabel7.setPixmap(QPixmap(u":/icons/res/icons/\u7f16\u7a0b_1765287508.png"))
        self.aboutIconLabel7.setScaledContents(True)
        self.aboutTextLabel4 = QLabel(self.AboutWidgeRight)
        self.aboutTextLabel4.setObjectName(u"aboutTextLabel4")
        self.aboutTextLabel4.setGeometry(QRect(80, 160, 271, 41))
        self.aboutTextLabel4.setFont(font10)
        self.aboutTextLabel4.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.aboutTextLabel4.setWordWrap(True)

        self.horizontalLayout.addWidget(self.AboutWidgeRight)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.aboutWidgetGroupWidget1 = QWidget(self.AboutWidget)
        self.aboutWidgetGroupWidget1.setObjectName(u"aboutWidgetGroupWidget1")
        self.aboutWidgetGroupSubControl1 = QWidget(self.aboutWidgetGroupWidget1)
        self.aboutWidgetGroupSubControl1.setObjectName(u"aboutWidgetGroupSubControl1")
        self.aboutWidgetGroupSubControl1.setGeometry(QRect(0, 10, 961, 91))
        self.aboutWidgetGroupSubControl1.setMinimumSize(QSize(0, 0))
        self.aboutWidgetGroupSubControl1.setMaximumSize(QSize(16777215, 16777215))
        self.aboutWidgetGroupSubControl1.setStyleSheet(u"#aboutWidgetGroupSubControl1{\n"
"	background-color: rgba(35, 36, 41,0.4);\n"
"	border-radius: 6px;\n"
"	color: white;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.aboutWidgetGroupSubControl1)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.aboutHorizontalSpacer1 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.aboutHorizontalSpacer1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.aboutIconLabel13 = QLabel(self.aboutWidgetGroupSubControl1)
        self.aboutIconLabel13.setObjectName(u"aboutIconLabel13")
        self.aboutIconLabel13.setMinimumSize(QSize(39, 39))
        self.aboutIconLabel13.setMaximumSize(QSize(39, 39))
        self.aboutIconLabel13.setPixmap(QPixmap(u":/icons/res/icons/\u7f51\u7edc (1).png"))
        self.aboutIconLabel13.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.aboutIconLabel13)

        self.aboutLinkLabel1 = QLabel(self.aboutWidgetGroupSubControl1)
        self.aboutLinkLabel1.setObjectName(u"aboutLinkLabel1")
        self.aboutLinkLabel1.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font: italic 20pt \"Terminal\";\n"
"	font-size: 20pt;\n"
"	font-family: \"\u6977\u4f53\";\n"
"}")
        self.aboutLinkLabel1.setOpenExternalLinks(True)

        self.horizontalLayout_20.addWidget(self.aboutLinkLabel1)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)

        self.aboutHorizontalSpacer2 = QSpacerItem(643, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.aboutHorizontalSpacer2)


        self.verticalLayout_10.addWidget(self.aboutWidgetGroupWidget1)

        self.verticalLayout_10.setStretch(0, 6)
        self.verticalLayout_10.setStretch(1, 1)
        self.mainStackedWidget.addWidget(self.AboutWidget)

        self.horizontalLayout_2.addWidget(self.mainStackedWidget)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.backgroundLabel1 = QLabel(MainWidget)
        self.backgroundLabel1.setObjectName(u"backgroundLabel1")
        self.backgroundLabel1.setGeometry(QRect(0, 0, 1200, 800))
        self.backgroundLabel1.setMinimumSize(QSize(1200, 800))
        self.backgroundLabel1.setMaximumSize(QSize(1200, 800))
        self.backgroundLabel1.setPixmap(QPixmap(u":/background/res/background/background.png"))
        self.backgroundLabel1.setScaledContents(True)
        self.backgroundLabel1.raise_()
        self.mainWidget.raise_()

        self.retranslateUi(MainWidget)

        self.mainStackedWidget.setCurrentIndex(3)
        self.formStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Uang Asura", None))
        self.logoLabel1.setText("")
        self.titleLabel1.setText(QCoreApplication.translate("MainWidget", u"Uang Asura", None))

        __sortingEnabled = self.NavListWidget.isSortingEnabled()
        self.NavListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.NavListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWidget", u"\u9996\u9875", None));
        ___qlistwidgetitem1 = self.NavListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWidget", u"\u529f\u80fd", None));
        ___qlistwidgetitem2 = self.NavListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWidget", u"\u5145\u7535", None));
        ___qlistwidgetitem3 = self.NavListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWidget", u"\u5173\u4e8e", None));
        self.NavListWidget.setSortingEnabled(__sortingEnabled)

        self.homeLogoLabel1.setText("")
        self.homeTitleLabel1.setText(QCoreApplication.translate("MainWidget", u"Uang Asura", None))
        self.homeIconLabel1.setText("")
        self.homeTitleLabel2.setText(QCoreApplication.translate("MainWidget", u"\u8fd9\u4e2a\u662f\u4e00\u4e2a\u722c\u866b\u7a0b\u5e8f\uff0c\u4ee5\u4e0b\u5c31\u662f\u6211\u4eec\u652f\u6301\u7684\u5e73\u53f0\u548c\u5b98\u7f51", None))
        self.homeIconLabel2.setText("")
        self.homeIconLabel3.setText("")
        self.homeIconLabel4.setText("")
        self.homeIconLabel5.setText(QCoreApplication.translate("MainWidget", u"<a href=\"https://www.ghnb66.cn\">\n"
"      <img src=\":/icons/res/icons/\u5730\u7403.png\" width=\"40\" height=\"40\"/>\n"
"</a>", None))
        self.homeIconLabel6.setText("")
        self.functionTitleLabel1.setText(QCoreApplication.translate("MainWidget", u"\u3056\u3053\u3057\u3058\u3087\u3046", None))
        self.functionTitleLabel2.setText(QCoreApplication.translate("MainWidget", u"\u9f50\u9f50&\u5c0f\u9ea6&\u5869\u9b5a/\u5171\u540c\u5f00\u53d1~_(:\u0437\u300d\u2220)_", None))
        self.functionLabel1.setText(QCoreApplication.translate("MainWidget", u"\u5e73\u53f0:", None))
        self.platformComboBox.setItemText(0, QCoreApplication.translate("MainWidget", u"\u5feb\u624b", None))
        self.platformComboBox.setItemText(1, QCoreApplication.translate("MainWidget", u"\u54d4\u54e9\u54d4\u54e9", None))
        self.platformComboBox.setItemText(2, QCoreApplication.translate("MainWidget", u"\u8c46\u74e3\u7535\u5f71(\u4ec5\u6392\u884c\u699c)", None))

        self.functionLabel2.setText(QCoreApplication.translate("MainWidget", u"\u6587\u4ef6\u5b58\u653e\u4f4d\u7f6e\uff1a", None))
        self.morePushButton.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9", None))
        self.functionLabel3.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u7684URL\u5730\u5740\uff1a", None))
        self.functionLabel4.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u7684URL\u5730\u5740\uff1a", None))
        self.functionLabel5.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9\u89c6\u9891\u6e05\u6670\u5ea6\uff1a", None))
        self.startPushButton.setText(QCoreApplication.translate("MainWidget", u"START", None))
        self.chargingTitleLabel1.setText(QCoreApplication.translate("MainWidget", u"\u4e3a\u201c\u3056\u3053\u3057\u3058\u3087\u3046\u201d\u306e\u7c73\u5a1c\u6851\u6dfb\u52a0\u54b8\u9c7c\u80fd\u91cf", None))
        self.chargingTitleLabel2.setText(QCoreApplication.translate("MainWidget", u"\u2014\u2014  \u611f\u8c22\u5404\u4f4d\u6d3b\u7239\u5927\u529b\u652f\u6301  \u2014\u2014", None))
        self.chargingTextLabel1.setText(QCoreApplication.translate("MainWidget", u"\u5728\u94f6\u6cb3\u7eaa\u51432178\u5e74\uff0c\u4eba\u7c7b\u6587\u660e\u5df2\u8de8\u8d8a\u6570\u5343\u5149\u5e74\uff0c\u5efa\u7acb\u4e86\u6a2a\u8de8\u4e09\u4e2a\u65cb\u81c2\u7684\u661f\u9645\u5e1d\u56fd\u3002\n"
"\u91cf\u5b50\u5f15\u64ce\u7684\u8f70\u9e23\u58f0\u56de\u8361\u5728\u66f2\u7387\u901a\u9053\u4e2d\uff0c\u4eff\u751f\u4eba\u8bae\u5458\u4eec\u6b63\u5728\u7b2c\u4e03\u8bae\u4f1a\u5385\u6fc0\u70c8\u8fa9\u8bba\u7740\u201c\u7b2c\u03a9\u53f7\u6b96\u6c11\u6cd5\u6848\u201d\u3002\n"
"\u7a81\u7136\uff0c\u5168\u606f\u661f\u56fe\u4e0a\u7684\u5929\u72fc\u661f\u03b2\u95ea\u70c1\u8d77\u4e0d\u7965\u7684\u7ea2\u8272\u2014\u2014\u90a3\u4e2a\u88ab\u9057\u5f03\u4e24\u767e\u5e74\u7684\u524d\u54e8\u7ad9\uff0c\n"
"\u6b63\u4ee5\u8fdd\u53cd\u71b5\u589e\u5b9a\u5f8b\u7684\u65b9\u5f0f\u5411\u5b87\u5b99\u5e7f\u64ad\u7740\u5706\u5468\u7387\u524d\u767e\u4e07\u4f4d\u7684\u8d28\u6570\u3002\n"
"\u5e1d\u56fd\u9996\u5e2d\u79d1\u5b66\u5bb6\u6276\u6b63\u795e\u7ecf\u63a5\u53e3\u773c\u955c\uff0c\u955c\u7247\u4e0a\u6d41\u8fc7\u7011\u5e03\u822c"
                        "\u7684\u4ee3\u7801\uff1a\u201c\u8bf8\u4f4d\uff0c\u6211\u4eec\u53ef\u80fd\u89e6\u53d1\u4e86\u4e0a\u53e4\u6587\u660e\u7559\u4e0b\u7684\u2026\u201d \n"
"\u6240\u4ee5\u80fd\u4e0d\u80fd\u5148\u501f\u621150\u5757\u4ea4\u4e2a\u66f2\u7387\u822a\u884c\u8fdd\u7ae0\u7f5a\u6b3e\uff1f\u6628\u5929\u9a91\u53cd\u91cd\u529b\u6ed1\u677f\u8f66\u53bb\u4fbf\u5229\u5e97\u4e70\u5408\u6210\u86cb\u767d\u68d2\u7684\u65f6\u5019\u8d85\u901f\u4e86\u3002", None))
        self.chargingQrcodeLabel1.setText("")
        self.chargingLabel1.setText(QCoreApplication.translate("MainWidget", u"VX", None))
        self.chargingLabel2.setText(QCoreApplication.translate("MainWidget", u"OR", None))
        self.chargingQrcodeLabel2.setText("")
        self.chargingLabel3.setText(QCoreApplication.translate("MainWidget", u"zfb", None))
        self.chargingQrcodeLabel3.setText("")
        self.chargingLabel4.setText(QCoreApplication.translate("MainWidget", u"\u2014 VX \u2014", None))
        self.chargingQrcodeLabel4.setText("")
        self.chargingLabel5.setText(QCoreApplication.translate("MainWidget", u"\u2014 QQ\u9891\u9053 \u2014", None))
        self.chargingLabel6.setText(QCoreApplication.translate("MainWidget", u"\\QQ\u9891\u9053\uff1a123456789", None))
        self.chargingLabel7.setText(QCoreApplication.translate("MainWidget", u"\\QQ\u9891\u9053\uff1a123456789", None))
        self.chargingLabel8.setText(QCoreApplication.translate("MainWidget", u"\\\u5b98\u65b9\u5fae\u535a\uff1a123456789", None))
        self.chargingBgLabel1.setText("")
        self.aboutTitleLabel1.setText(QCoreApplication.translate("MainWidget", u"\u3056\u3053\u3057\u3058\u3087\u3046", None))
        self.aboutTextLabel3.setText(QCoreApplication.translate("MainWidget", u"\u4f7f\u7528\u8005\u5e94\u4e25\u683c\u9075\u5b88\u300a\u7f51\u7edc\u5b89\u5168\u6cd5\u300b\u53ca\u76ee\u6807\u7f51\u7ad9\u7528\u6237\u534f\u8bae\uff0c\u4e0d\u5f97\u5b9e\u65bd\u4efb\u4f55\u5e72\u6270\u3001\u7834\u574f\u6216\u4fb5\u6743\u6d3b\u52a8\u3002\n"
"\u4efb\u4f55\u8fdd\u53cd\u672c\u58f0\u660e\u7684\u6ee5\u7528\u884c\u4e3a\u6240\u5f15\u53d1\u7684\u4e00\u5207\u6cd5\u5f8b\u8d23\u4efb\u4e0e\u540e\u679c\uff0c\u5747\u7531\u4f7f\u7528\u8005\u81ea\u884c\u627f\u62c5\uff0c\u5f00\u53d1\u56e2\u961f\u6982\u4e0d\u8d1f\u8d23\u3002\n"
"\u5982\u9047\u95ee\u9898\u6216\u53d1\u73b0\u5b89\u5168\u6f0f\u6d1e\u7b49\uff0c\u8bf7\u8054\u7cfb\u56e2\u961f\u90ae\u7bb1\uff1aqq@ghnb66.cn", None))
        self.aboutTextLabel1.setText(QCoreApplication.translate("MainWidget", u"\u672c\u9879\u76ee\u4e3a\u5e7f\u5dde\u5e02\u767d\u4e91\u5de5\u5546\u6280\u5e08\u5b66\u9662python\u7a0b\u5e8f\u4e8c\u7ec4\u5b9e\u8df5\u9879\u76ee\uff0c\u4ec5\u7528\u4e8e\u6559\u80b2\u7814\u7a76\u53ca\u5b66\u4e60\u76ee\u7684\uff0c\u65e8\u5728\u5b66\u4e60\u6570\u636e\u91c7\u96c6\u4e0e\u5206\u6790\u6280\u672f\uff0c\u4e25\u7981\u7528\u4e8e\u4efb\u4f55\u5546\u4e1a\u3001\u653b\u51fb\u6216\u975e\u6cd5\u7528\u9014\u3002", None))
        self.aboutIconLabel4.setText("")
        self.aboutIconLabel5.setText("")
        self.aboutTitleLabel6.setText(QCoreApplication.translate("MainWidget", u"\u6ce8\u610f\u4e8b\u9879", None))
        self.aboutTitleLabel2.setText(QCoreApplication.translate("MainWidget", u"\u9f50\u9f50&\u5c0f\u9ea6&\u5869\u9b5a/\u5171\u540c\u5f00\u53d1~_(:\u0437\u300d\u2220)_", None))
        self.aboutIconLabel3.setText("")
        self.aboutTitleLabel5.setText(QCoreApplication.translate("MainWidget", u"\u7248\u6743\u58f0\u660e\uff1a", None))
        self.aboutTitleLabel3.setText(QCoreApplication.translate("MainWidget", u"-\u91cd\u8981\u58f0\u660e\u4e0e\u98ce\u9669\u63d0\u793a\u2014\u2014", None))
        self.aboutIconLabel1.setText("")
        self.aboutIconLabel2.setText("")
        self.aboutTitleLabel4.setText(QCoreApplication.translate("MainWidget", u"\u4f7f\u7528\u76ee\u7684:", None))
        self.aboutTextLabel2.setText(QCoreApplication.translate("MainWidget", u"\u9879\u76ee\u5168\u90e8\u4ee3\u7801\u3001\u8bbe\u8ba1\u53ca\u6587\u6863\u7b49\u7248\u6743\u5f52\u5e7f\u5dde\u5e02\u767d\u4e91\u5de5\u5546\u6280\u5e08\u5b66\u966225\u7ea7\u7a0b\u5e8f\u8bbe\u8ba1\u4e2d\u6280\u73edPython\u4e8c\u7ec4\u5171\u540c\u6240\u6709\u3002\u672a\u7ecf\u56e2\u961f\u4e66\u9762\u6388\u6743\uff0c\u7981\u6b62\u4efb\u4f55\u5f62\u5f0f\u7684\u590d\u5236\u3001\u4fee\u6539\u3001\u5206\u53d1\u6216\u5546\u4e1a\u5316\u4f7f\u7528\u3002\u6240\u91c7\u96c6\u7684\u6570\u636e\u9075\u5faa\u6559\u80b2\u7814\u7a76\u4e4b\u5408\u7406\u4f7f\u7528\u539f\u5219\uff0c\u4f7f\u7528\u540e\u8bf7\u572824\u5c0f\u65f6\u5185\u5220\u9664\uff01\uff01\uff01\n"
"\u7248\u6743\u53cd\u9988\u4e0e\u529f\u80fd\u53cd\u9988\uff1a\u5982\u6709\u4efb\u4f55\u7248\u6743\u76f8\u5173\u95ee\u9898\u6216\u529f\u80fd\u53cd\u9988\uff0c\u8bf7\u8054\u7cfb\u56e2\u961f\u90ae\u7bb1\uff1aqq@ghnb66.cn\u3002", None))
        self.aboutTextLabel9.setText(QCoreApplication.translate("MainWidget", u"\uff1a\u8fd0\u7ef4\u3001\u63d0\u4f9b\u5bc6\u94a5\u9a8c\u8bc1", None))
        self.aboutIconLabel12.setText("")
        self.aboutIconLabel10.setText("")
        self.aboutTextLabel7.setText(QCoreApplication.translate("MainWidget", u":\u611f\u8c22\u9b54\u6cd5\u2606\u5869\u9b5a\u5927\u529b\u652f\u6301\u55b5\u2727\u0669(\u02ca\u03c9\u02cb*)\u0648\u2727", None))
        self.aboutTitleLabel8.setText(QCoreApplication.translate("MainWidget", u"\u6ca1\u6709\u4ed6\u4eec\uff0c\u5c31\u6ca1\u6709Uang Asura!!!", None))
        self.aboutIconLabel11.setText("")
        self.aboutTextLabel8.setText(QCoreApplication.translate("MainWidget", u"\u7ec4\u957f&\u9f50\u9f50", None))
        self.aboutIconLabel6.setText("")
        self.aboutTitleLabel7.setText(QCoreApplication.translate("MainWidget", u"\u7279\u522b\u9e23\u8c22", None))
        self.aboutIconLabel8.setText("")
        self.aboutTextLabel5.setText(QCoreApplication.translate("MainWidget", u":\u611f\u8c22\u9ea6\u4e66\u8bb0\u71ac\u591c\u7206\u809d\u7684\u4ee3\u7801\uff01\uff3c(`\u0394\u2019)", None))
        self.aboutIconLabel9.setText("")
        self.aboutTextLabel6.setText(QCoreApplication.translate("MainWidget", u"UI\u6846\u67b6\u652f\u6301&\u5212\u6c34\u306e\u9b5a\uff1a", None))
        self.aboutIconLabel7.setText("")
        self.aboutTextLabel4.setText(QCoreApplication.translate("MainWidget", u"\u6838\u5fc3\u5f00\u53d1&\u7d2f\u6b7b\u306e\u725b\uff1a", None))
        self.aboutIconLabel13.setText("")
        self.aboutLinkLabel1.setText(QCoreApplication.translate("MainWidget", u"<strong><a href=\"www.ghnb66.cn\" style=\"color:white;\">www.ghnb66.cn</a></strong>", None))
        self.backgroundLabel1.setText("")
    # retranslateUi

