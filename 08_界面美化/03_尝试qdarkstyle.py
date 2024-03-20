from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QSpinBox, QSlider, QComboBox, \
    QLabel, QCheckBox, QRadioButton, QButtonGroup, QTextEdit, QPlainTextEdit
from PySide6.QtCore import Qt
import qdarkstyle


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.lb1 = QLabel('标签1')
        self.lb1.setText('标签1被修改了')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn1 = QPushButton('按钮1')

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('请输入内容')
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.cb1 = QComboBox()
        self.cb1.setPlaceholderText('请选择')
        self.cb1.addItems(['选项1', '选项2', '选项3'])
        self.cb1.removeItem(0)

        self.checkBox1 = QCheckBox('复选框1')
        self.checkBox1.setCheckable(False)
        self.checkBox2 = QCheckBox('复选框2')
        self.checkBox2.setChecked(True)

        # 创建单选按钮
        self.genderNan = QRadioButton('男')
        self.genderNv = QRadioButton('女')
        self.genderQt = QRadioButton('其他')

        # 创建按钮组
        self.favoriteGroup = QButtonGroup()
        self.radioBtnMath = QRadioButton('数学')
        self.radioBtnChinese = QRadioButton('语文')
        self.favoriteGroup.addButton(self.radioBtnMath)
        self.favoriteGroup.addButton(self.radioBtnChinese)

        markdownStr = """
# 标题1

```python
def hello():
    return 'hello'
```

- 1
- 2
- 3

---

这是一段正常的文字
        """

        # 创建文本框
        self.richText = QTextEdit()
        self.richText.setPlaceholderText('请输入内容')
        self.richText.setMarkdown(markdownStr)

        self.plainText = QPlainTextEdit()
        self.plainText.setPlainText('这是一段纯文本')

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setRange(0, 100)

        # 布局添加控件
        self.mainLayout.addWidget(self.lb1)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.cb1)
        self.mainLayout.addWidget(self.checkBox1)
        self.mainLayout.addWidget(self.checkBox2)
        self.mainLayout.addWidget(self.genderNan)
        self.mainLayout.addWidget(self.genderNv)
        self.mainLayout.addWidget(self.genderQt)
        self.mainLayout.addWidget(self.radioBtnMath)
        self.mainLayout.addWidget(self.radioBtnChinese)
        self.mainLayout.addWidget(self.richText)
        self.mainLayout.addWidget(self.plainText)
        self.mainLayout.addWidget(self.slider)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.btn1.clicked.connect(self.btn1_clicked)
        self.lineEdit.textChanged.connect(self.lineEditTextChanged)
        self.lineEdit.returnPressed.connect(self.lineEditReturnPressed)
        self.cb1.currentTextChanged.connect(self.cbTextChanged)
        self.checkBox2.stateChanged.connect(self.cb2Changed)
        self.genderNan.clicked.connect(lambda: print('男'))
        self.genderNv.clicked.connect(lambda: print('女'))
        self.genderQt.clicked.connect(lambda: print('其他'))
        self.favoriteGroup.buttonClicked.connect(self.whichButtonClicked)
        self.richText.textChanged.connect(lambda: print('文本框内容发生了变化'))
        self.slider.valueChanged.connect(lambda x: print('滑块的值发生了变化：', x))

    def btn1_clicked(self):
        print('按钮1被点击了')

    def lineEditTextChanged(self, text):
        print('文本框内容发生了变化：', text)

    def lineEditReturnPressed(self):
        print('文本框回车了')
        print('文本框的内容是：', self.lineEdit.text())

    def cbTextChanged(self, text):
        print('下拉框内容发生了变化：', text)

    def cb2Changed(self, state):
        print('复选框2状态发生了变化：', state)

    def whichButtonClicked(self):
        print('单选按钮组被点击了')
        print('选中的是：', self.favoriteGroup.checkedButton().text())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = MyWindow()
    window.show()
    app.exec()
