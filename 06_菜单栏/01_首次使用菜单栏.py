from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from ui_menu import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 触发菜单栏的信号
        self.actionOpen.triggered.connect(lambda: print('打开'))
        self.actionExit.triggered.connect(lambda: print('退出'))
        self.actionAdd.triggered.connect(lambda: print('添加'))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
