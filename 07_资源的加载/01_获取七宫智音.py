from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
import rc_hello


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel()
        # self.lb.setPixmap(QPixmap('./qigong.jpg'))
        self.lb.setPixmap(QPixmap(':/images/qigong.jpg'))
        self.lb.setScaledContents(True)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
