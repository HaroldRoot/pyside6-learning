from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog, QLineEdit


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton('获取一个整型数字')
        btn1.clicked.connect(self.getIntDialog)

        btn2 = QPushButton('获取一个浮点数字')
        btn2.clicked.connect(self.getFloatDialog)

        btn3 = QPushButton('获取一个Item')
        btn3.clicked.connect(lambda: print(QInputDialog.getItem(self, '标题', '内容', ['小王', '小丽', '小明'], 0, False)))

        btn4 = QPushButton('获取单行文字')
        btn4.clicked.connect(lambda: print(QInputDialog.getText(self, '标题', '内容', QLineEdit.EchoMode.NoEcho, '默认值')))

        btn5 = QPushButton('获取多行文字')
        btn5.clicked.connect(
            lambda: print(QInputDialog.getMultiLineText(self, '标题', '内容')))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(btn1)
        self.mainLayout.addWidget(btn2)
        self.mainLayout.addWidget(btn3)
        self.mainLayout.addWidget(btn4)
        self.mainLayout.addWidget(btn5)
        self.setLayout(self.mainLayout)

    def getIntDialog(self):
        replay, ok = QInputDialog.getInt(self, '标题', '内容', 1, 0, 100, 1)
        if ok:
            print(replay)

    def getFloatDialog(self):
        replay, ok = QInputDialog.getDouble(self, '标题', '内容', 1.0, 0.0, 100.0, 1)
        if ok:
            print(replay)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
