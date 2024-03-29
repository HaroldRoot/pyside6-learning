from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont


class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lbWait = QLabel("加载中……")
        self.lbWait.setFont(QFont("微软雅黑", 50))
        self.lbWait.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lbWait)
        self.setLayout(self.mainLayout)

        QTimer.singleShot(3000, self.openMainWindow)

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")

        self.lbWelcome = QLabel("欢迎使用本软件")
        self.lbWelcome.setFont(QFont("微软雅黑", 50))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lbWelcome)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    window.show()
    app.exec()
