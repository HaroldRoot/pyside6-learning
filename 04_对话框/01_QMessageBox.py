from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.btn = QPushButton('按钮')
        self.btn.clicked.connect(self.btnClicked)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        # QMessageBox.information(self, 'information', '你好，世界！')
        # QMessageBox.question(self, 'question', '你好，世界！')
        # QMessageBox.warning(self, 'warning', '你好，世界！')
        # QMessageBox.critical(self, 'critical', '你好，世界！')
        # QMessageBox.about(self, 'about', '你好，世界！')

        replay = QMessageBox.information(self, '标题', '内容',
                                         QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No |
                                         QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Discard,
                                         QMessageBox.StandardButton.Ok)

        if replay == QMessageBox.StandardButton.Ok:
            print('你点击了OK')
        elif replay == QMessageBox.StandardButton.No:
            print('你点击了No')
        elif replay == QMessageBox.StandardButton.Discard:
            print('你点击了Discard')
        elif replay == QMessageBox.StandardButton.Apply:
            print('你点击了Apply')


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
