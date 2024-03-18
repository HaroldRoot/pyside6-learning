from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QLabel, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 登录界面

        self.mainLayout = QVBoxLayout()  # 垂直控件

        # self.userLayout = QHBoxLayout()  # 水平控件
        # self.userLayout.addWidget(QLabel('用户名'))
        # self.userLayout.addWidget(QLineEdit())
        # self.mainLayout.addLayout(self.userLayout)
        #
        # self.passwordLayout = QHBoxLayout()
        # self.passwordLayout.addWidget(QLabel('密码'))
        # self.passwordLayout.addWidget(QLineEdit())
        # self.mainLayout.addLayout(self.passwordLayout)

        # self.formLayout = QFormLayout()
        # self.formLayout.addRow('用户名', QLineEdit())
        # self.formLayout.addRow('密码', QLineEdit())
        # self.formLayout.addWidget(QPushButton('登录'))
        # self.mainLayout.addLayout(self.formLayout)

        self.gridLayout = QGridLayout()  # 网格控件
        self.gridLayout.addWidget(QPushButton('1'), 0, 0)
        self.gridLayout.addWidget(QPushButton('2'), 0, 1)
        self.gridLayout.addWidget(QPushButton('3'), 0, 2)
        self.gridLayout.addWidget(QPushButton('4'), 1, 0, 1, 3)
        self.mainLayout.addLayout(self.gridLayout)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
