from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from faker import Faker
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')

        self.listWidget = QListWidget()
        # for _ in range(20):
        #     self.listWidget.addItem(self.fake.name())
        # for _ in range(20):
        #     self.listWidget.addItem(QListWidgetItem(self.fake.name()))
        self.listWidget.addItems([self.fake.name() for _ in range(20)])

        # 插入一个元素
        self.listWidget.insertItem(2, '100')
        self.listWidget.insertItem(5, QListWidgetItem('100'))
        self.listWidget.insertItems(7, ['100', '200', '300'])

        # 删除
        self.listWidget.takeItem(2)

        # 修改
        # itemGet = self.listWidget.item(0)
        # itemGet.setText('第一个')
        self.listWidget.item(0).setText('第一个')

        # 查找
        result = self.listWidget.findItems('第一', Qt.MatchFlag.MatchContains)
        print(result)
        for i in result:
            print(i.text())

        # 遍历
        for i in range(self.listWidget.count()):
            print(self.listWidget.item(i).text())

        # 清空
        # self.listWidget.clear()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.listWidget.currentItemChanged.connect(self.listChanged)

    # def listChanged(self):
    #     print(self.listWidget.currentItem().text())
    def listChanged(self, item, previous):
        print(f'当前选中的值是{item.text()}，上一个值是{previous.text()}')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
