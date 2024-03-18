# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(533, 276)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(50, 50))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 179, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.autoBtn = QRadioButton(self.layoutWidget)
        self.autoBtn.setObjectName(u"autoBtn")
        self.autoBtn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.autoBtn)

        self.enBtn = QRadioButton(self.layoutWidget)
        self.enBtn.setObjectName(u"enBtn")

        self.horizontalLayout_3.addWidget(self.enBtn)

        self.cnBtn = QRadioButton(self.layoutWidget)
        self.cnBtn.setObjectName(u"cnBtn")

        self.horizontalLayout_3.addWidget(self.cnBtn)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.inputEdit = QTextEdit(Form)
        self.inputEdit.setObjectName(u"inputEdit")

        self.verticalLayout_2.addWidget(self.inputEdit)

        self.transBtn = QPushButton(Form)
        self.transBtn.setObjectName(u"transBtn")

        self.verticalLayout_2.addWidget(self.transBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.outputEdit = QTextEdit(Form)
        self.outputEdit.setObjectName(u"outputEdit")

        self.verticalLayout_3.addWidget(self.outputEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.moreEdit = QTextEdit(Form)
        self.moreEdit.setObjectName(u"moreEdit")

        self.verticalLayout.addWidget(self.moreEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165\u8bed\u8a00", None))
        self.autoBtn.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.enBtn.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.cnBtn.setText(QCoreApplication.translate("Form", u"\u6c49\u8bed", None))
        self.transBtn.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u8f93\u51fa\u8bed\u8a00", None))
        self.moreEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u66f4\u591a", None))
    # retranslateUi

