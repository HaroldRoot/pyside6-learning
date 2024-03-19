from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal

"""
1. 创建一个信号
    from PySide6.QtCore import Signal
2. 类中进行定义
    是在 __init__ 函数外面
3. 对信号进行绑定
    信号名称.connect(具体需要激活的函数)
4. 使用 信号名.emit(发送值) 激活信号
"""


class MyWindow(QWidget):
    sendValueToSubWindow = Signal(object)

    def __init__(self):
        super().__init__()

        self.lineEditSend = QLineEdit()
        self.btn = QPushButton('发送数据到子窗口')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSend)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.subWindow = SubWindow()
        self.subWindow.show()
        self.sendValueToSubWindow.connect(self.subWindow.lineEditSub.setText)
        self.btn.clicked.connect(self.sendValue)

    def sendValue(self):
        text = self.lineEditSend.text()
        self.sendValueToSubWindow.emit(text)


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 接收
        self.lineEditSub = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSub)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
