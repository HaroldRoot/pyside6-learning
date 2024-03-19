from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMenu, QStyle
from PySide6.QtGui import QAction


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menu = self.menuBar()

        self.openFile = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon), '打开文件')
        self.closeFile = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirClosedIcon), '关闭文件')

        self.fileMenu = QMenu('文件')
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.closeFile)

        self.moreMenu = QMenu('更多')
        self.more1 = QAction('更多1')
        self.moreMenu.addAction(self.more1)
        self.moreMenu.addAction('更多2')
        self.fileMenu.addMenu(self.moreMenu)

        self.menu.addMenu(self.fileMenu)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.menu)
        self.setLayout(self.mainLayout)

        self.openFile.triggered.connect(lambda: print('打开文件'))
        self.closeFile.triggered.connect(lambda: print('关闭文件'))
        self.more1.triggered.connect(lambda: print('更多1'))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
