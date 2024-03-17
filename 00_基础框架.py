from PySide6.QtWidgets import QApplication, QWidget, QLineEdit


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        line = QLineEdit(self)
        line.setPlaceholderText('请输入内容')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
