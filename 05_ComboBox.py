from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['李华', '张三', '小王'])

        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
