import random

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from faker import Faker
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')

        self.listWidget = QListWidget()
        self.listWidget.addItems([str(random.randint(0, 100)) for _ in range(20)])

        # 对列表进行排序（字符串排序，不是数字排序）
        self.listWidget.sortItems(Qt.SortOrder.AscendingOrder)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
