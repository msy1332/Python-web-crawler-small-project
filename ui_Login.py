# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import rc_MainWidget

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(619, 433)
        LoginWidget.setMinimumSize(QSize(619, 433))
        LoginWidget.setMaximumSize(QSize(619, 433))
        icon = QIcon()
        icon.addFile(u":/login/res/login/Login.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        LoginWidget.setWindowIcon(icon)
        LoginWidget.setStyleSheet(u"#LoginWidget{\n"
"	background-color: #f0f0f0;\n"
"}")
        self.loginWidget = QWidget(LoginWidget)
        self.loginWidget.setObjectName(u"loginWidget")
        self.loginWidget.setGeometry(QRect(0, 0, 619, 433))
        self.loginWidget.setMinimumSize(QSize(619, 433))
        self.loginWidget.setMaximumSize(QSize(619, 433))
        self.verticalLayout_2 = QVBoxLayout(self.loginWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer3)

        self.logoLabel = QLabel(self.loginWidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(100, 100))
        self.logoLabel.setMaximumSize(QSize(100, 100))
        self.logoLabel.setPixmap(QPixmap(u":/login/res/login/Login.png"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.logoLabel)

        self.horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer5)

        self.titleLabel = QLabel(self.loginWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"QLabel{\n"
"	color: #cbcbcb;\n"
"}")

        self.horizontalLayout_5.addWidget(self.titleLabel)

        self.horizontalSpacer6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer7)

        self.keyLineEdit = QLineEdit(self.loginWidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setMinimumSize(QSize(200, 30))
        self.keyLineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.keyLineEdit.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout.addWidget(self.keyLineEdit)

        self.horizontalSpacer8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer9 = QSpacerItem(160, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer9)

        self.loginPushButton = QPushButton(self.loginWidget)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setMinimumSize(QSize(200, 35))
        self.loginPushButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.loginPushButton)

        self.horizontalSpacer10 = QSpacerItem(160, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer10)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer11)

        self.linkLabel1 = QLabel(self.loginWidget)
        self.linkLabel1.setObjectName(u"linkLabel1")
        self.linkLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkLabel1.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.linkLabel1)

        self.horizontalSpacer12 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer12)

        self.TextLabel1 = QLabel(self.loginWidget)
        self.TextLabel1.setObjectName(u"TextLabel1")

        self.horizontalLayout_2.addWidget(self.TextLabel1)

        self.horizontalSpacer13 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer13)

        self.linkLabel2 = QLabel(self.loginWidget)
        self.linkLabel2.setObjectName(u"linkLabel2")
        self.linkLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkLabel2.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.linkLabel2)

        self.horizontalSpacer14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer14)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer1 = QSpacerItem(95, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer1)

        self.horizontalSpacer2 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer2)

        self.backgroundLabel1 = QLabel(LoginWidget)
        self.backgroundLabel1.setObjectName(u"backgroundLabel1")
        self.backgroundLabel1.setGeometry(QRect(0, 0, 619, 433))
        self.backgroundLabel1.setMinimumSize(QSize(619, 433))
        self.backgroundLabel1.setMaximumSize(QSize(619, 433))
        self.backgroundLabel1.setPixmap(QPixmap(u":/background/res/background/background.png"))
        self.backgroundLabel1.setScaledContents(True)
        self.backgroundLabel1.raise_()
        self.loginWidget.raise_()

        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Login", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("LoginWidget", u"Uang Asura", None))
        self.keyLineEdit.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"\u8bf7\u8f93\u5165\u5bc6\u94a5", None))
        self.loginPushButton.setText(QCoreApplication.translate("LoginWidget", u"\u767b\u5f55", None))
        self.linkLabel1.setText(QCoreApplication.translate("LoginWidget", u"<a href=\"https://qun.qq.com/universal-share/share?ac=1&authKey=VbKjg3QhTPZXx20FDg1PCyXf0ErU4LluiYPXDLrbEEPuW2IX4TxLgX0ll6DSW4LF&busi_data=eyJncm91cENvZGUiOiIxMDc1MDEwNTg3IiwidG9rZW4iOiJ6MU41dGRKaW10ZDBuOTJiNFp5THRKVk1BalpFdmhrbW5VSkp0RGpTejAxclEydDkxSmhIaVFPcll6MGp1bWFvIiwidWluIjoiMjA1NTIyOTI1MiJ9&data=RSgkeK1jDmhkMVCoBg5P41oYFqB5ftL4yLbL5UsGUgLMZYb9PHtW2cBGkDIqPZN-M6sbfR3KHA9AicRexIaH_Q&svctype=4&tempid=h5_group_info\">\u52a0\u5165QQ\u7fa4</a>", None))
        self.TextLabel1.setText(QCoreApplication.translate("LoginWidget", u"|", None))
        self.linkLabel2.setText(QCoreApplication.translate("LoginWidget", u"<a href=\"https://www.ghnb66.cn\">\u5b98\u7f51</a>", None))
        self.backgroundLabel1.setText("")
    # retranslateUi

