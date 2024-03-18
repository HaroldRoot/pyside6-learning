from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QColorDialog, QTextEdit, QPushButton
from PySide6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.edit = QTextEdit()
        self.edit.setFont(QFont('微软雅黑', 36))
        self.btn = QPushButton('点我选择颜色')
        self.btn.clicked.connect(self.changeColor)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def changeColor(self):
        color = QColorDialog.getColor()
        print(color)
        self.edit.setTextColor(color)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
