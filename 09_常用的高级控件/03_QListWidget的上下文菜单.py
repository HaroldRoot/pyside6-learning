from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget
from faker import Faker


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')

        self.listWidget = QListWidget()
        self.listWidget.addItems([self.fake.name() for _ in range(20)])

        # 给窗体添加上下文菜单
        self.sayHello = QAction('你好')
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.sayHello)

        # 给控件添加上下文菜单
        self.outputCurrentItem = QAction('输出当前选中的值')
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.addAction(self.outputCurrentItem)

        self.deleteCurrent = QAction('删除当前元素')
        self.listWidget.addAction(self.deleteCurrent)

        # 将第一个元素设置为能够选中的元素
        self.listWidget.item(0).setCheckState(Qt.CheckState.Unchecked)
        self.listWidget.item(0).setFlags(self.listWidget.item(0).flags() | Qt.ItemFlag.ItemIsSelectable)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.sayHello.triggered.connect(lambda: print('你好'))
        self.listWidget.currentItemChanged.connect(self.listChange)
        self.outputCurrentItem.triggered.connect(self.printCurrentItem)
        self.deleteCurrent.triggered.connect(lambda: self.listWidget.takeItem(self.listWidget.currentRow()))
        # self.listWidget.itemChanged.connect(lambda: print(f'被选中了！'))
        self.listWidget.itemChanged.connect(lambda: print(self.listWidget.currentItem().checkState()))

    def printCurrentItem(self):
        print(self.listWidget.currentItem().text())

    def listChange(self, item):
        print(f'当前选中的值是{item.text()}')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
