# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 608)
        self.act_open_doi = QAction(MainWindow)
        self.act_open_doi.setObjectName(u"act_open_doi")
        self.act_save_doi = QAction(MainWindow)
        self.act_save_doi.setObjectName(u"act_save_doi")
        self.act_save_as_doi = QAction(MainWindow)
        self.act_save_as_doi.setObjectName(u"act_save_as_doi")
        self.act_open_manual = QAction(MainWindow)
        self.act_open_manual.setObjectName(u"act_open_manual")
        self.act_about = QAction(MainWindow)
        self.act_about.setObjectName(u"act_about")
        self.act_clear_list = QAction(MainWindow)
        self.act_clear_list.setObjectName(u"act_clear_list")
        self.act_open_settings = QAction(MainWindow)
        self.act_open_settings.setObjectName(u"act_open_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cmb_source = QComboBox(self.groupBox)
        self.cmb_source.setObjectName(u"cmb_source")

        self.gridLayout_2.addWidget(self.cmb_source, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 641, 468))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_dois_list = QVBoxLayout()
#ifndef Q_OS_MAC
        self.layout_dois_list.setSpacing(-1)
#endif
        self.layout_dois_list.setObjectName(u"layout_dois_list")
        self.layout_dois_list.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_2.addLayout(self.layout_dois_list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.btn_open_doi = QPushButton(self.groupBox_2)
        self.btn_open_doi.setObjectName(u"btn_open_doi")

        self.horizontalLayout.addWidget(self.btn_open_doi)

        self.btn_save_doi = QPushButton(self.groupBox_2)
        self.btn_save_doi.setObjectName(u"btn_save_doi")

        self.horizontalLayout.addWidget(self.btn_save_doi)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 667, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.act_open_doi)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_save_doi)
        self.menuFile.addAction(self.act_save_as_doi)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_clear_list)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_open_settings)
        self.menuHelp.addAction(self.act_open_manual)
        self.menuHelp.addAction(self.act_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rapidoi", None))
        self.act_open_doi.setText(QCoreApplication.translate("MainWindow", u"Open doi list file", None))
        self.act_save_doi.setText(QCoreApplication.translate("MainWindow", u"Save doi list", None))
        self.act_save_as_doi.setText(QCoreApplication.translate("MainWindow", u"Save doi list as ...", None))
        self.act_open_manual.setText(QCoreApplication.translate("MainWindow", u"Open manual", None))
        self.act_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.act_clear_list.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
        self.act_open_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"DOI List", None))
        self.btn_open_doi.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_save_doi.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

