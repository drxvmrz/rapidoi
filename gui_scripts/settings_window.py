# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QListView, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(506, 310)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_rem_src = QPushButton(self.groupBox_2)
        self.btn_rem_src.setObjectName(u"btn_rem_src")

        self.gridLayout_3.addWidget(self.btn_rem_src, 1, 1, 1, 1)

        self.btn_add_src = QPushButton(self.groupBox_2)
        self.btn_add_src.setObjectName(u"btn_add_src")

        self.gridLayout_3.addWidget(self.btn_add_src, 1, 0, 1, 1)

        self.list_srcs = QListView(self.groupBox_2)
        self.list_srcs.setObjectName(u"list_srcs")

        self.gridLayout_3.addWidget(self.list_srcs, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_browse_path = QPushButton(self.groupBox)
        self.btn_browse_path.setObjectName(u"btn_browse_path")

        self.gridLayout_2.addWidget(self.btn_browse_path, 0, 1, 1, 1)

        self.line_path = QLineEdit(self.groupBox)
        self.line_path.setObjectName(u"line_path")

        self.gridLayout_2.addWidget(self.line_path, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Article sources", None))
        self.btn_rem_src.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.btn_add_src.setText(QCoreApplication.translate("Form", u"Add", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Your default web-browser download path", None))
        self.btn_browse_path.setText(QCoreApplication.translate("Form", u"Browse...", None))
    # retranslateUi

