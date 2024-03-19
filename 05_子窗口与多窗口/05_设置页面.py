from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)

        self.lbAccount = QLabel("账号")
        self.lbPassword = QLabel("密码")

        self.btnSetValue = QPushButton("设置值")
        self.btnSetValue.clicked.connect(self.setSubWindowValue)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lbAccount)
        self.mainLayout.addWidget(self.lbPassword)
        self.mainLayout.addWidget(self.btnSetValue)
        self.setLayout(self.mainLayout)

        self.subWindow = SubWindow(self)
        self.subWindow.show()

    def setSubWindowValue(self):
        self.subWindow.leGet.setText('这是由主窗口设置的值')


class SubWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.leAccount = QLineEdit()
        self.lePassword = QLineEdit()
        self.btnSend = QPushButton("发送")
        self.btnSend.clicked.connect(self.sendValue)

        self.leGet = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.leAccount)
        self.mainLayout.addWidget(self.lePassword)
        self.mainLayout.addWidget(self.btnSend)
        self.mainLayout.addWidget(self.leGet)
        self.setLayout(self.mainLayout)

    def sendValue(self):
        self.parent.lbAccount.setText(self.leAccount.text())
        self.parent.lbPassword.setText(self.lePassword.text())


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
