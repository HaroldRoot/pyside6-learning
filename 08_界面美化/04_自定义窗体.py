from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 去除系统标题栏
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 自定义标题栏
        self.titleLabel = QLabel("自定义标题栏")
        self.minimizeButton = QPushButton('最小化')
        self.closeButton = QPushButton('关闭')

        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(self.titleLabel)
        self.hLayout.addWidget(self.minimizeButton)
        self.hLayout.addWidget(self.closeButton)
        self.setLayout(self.hLayout)

        # 将控件的信号与槽函数关联起来
        self.minimizeButton.clicked.connect(self.showMinimized)
        self.closeButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
