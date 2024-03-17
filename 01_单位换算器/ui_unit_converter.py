# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unit_converter.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(294, 279)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(Form)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(0, 40))
        self.lineEdit_1.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.lineEdit_1, 3, 0, 1, 1)

        self.convertedData = QLabel(Form)
        self.convertedData.setObjectName(u"convertedData")
        self.convertedData.setMinimumSize(QSize(200, 40))
        self.convertedData.setMaximumSize(QSize(1000, 40))
        font = QFont()
        font.setPointSize(29)
        font.setBold(True)
        self.convertedData.setFont(font)
        self.convertedData.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.convertedData, 1, 0, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 40))
        self.comboBox_3.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.originalData = QLabel(Form)
        self.originalData.setObjectName(u"originalData")
        self.originalData.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.originalData.setFont(font1)
        self.originalData.setStyleSheet(u"color: rgb(160, 160, 160)")

        self.gridLayout.addWidget(self.originalData, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 40))
        self.comboBox_2.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u".QComboBox{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5355\u4f4d\u6362\u7b97\u5668", None))
        self.convertedData.setText(QCoreApplication.translate("Form", u"0", None))
        self.originalData.setText(QCoreApplication.translate("Form", u"0 =", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

