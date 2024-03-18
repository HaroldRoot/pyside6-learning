from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QVBoxLayout,
                               QFileDialog, QPushButton)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        btn = QPushButton('选择单个文件')
        btn.clicked.connect(
            lambda: print(
                QFileDialog.getOpenFileName(self, '标题：选择单个文件', '.', 'All Files(*);;py文件(*.py *.pyd)')))

        btn2 = QPushButton('选择多个文件')
        btn2.clicked.connect(
            lambda: print(
                QFileDialog.getOpenFileNames(self, '标题：选择多个文件', '.', '所有文件(*);;音频文件(*.mp3 *.music)')))

        btn3 = QPushButton('选择一个目录')
        btn3.clicked.connect(
            lambda: print(
                QFileDialog.getExistingDirectory(self, '标题：选择一个目录', '.')))

        btn4 = QPushButton('保存文件')
        btn4.clicked.connect(
            lambda: print(
                QFileDialog.getSaveFileName(self, '标题：保存文件', '.', '所有文件(*);;音频文件(*.mp3 *.music)')))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(btn)
        self.mainLayout.addWidget(btn2)
        self.mainLayout.addWidget(btn3)
        self.mainLayout.addWidget(btn4)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
