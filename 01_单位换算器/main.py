from PySide6.QtWidgets import QApplication, QWidget
from ui_unit_converter import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 用于存储数据类型的字典
        self.lengthVar = {'米': 100, '千米': 100000, '厘米': 1, '分米': 10}
        self.weightVar = {'克': 1, '千克': 1000, '斤': 500}

        self.typeDict = {'长度': self.lengthVar, '质量': self.weightVar}

        self.comboBox.addItems(self.typeDict.keys())
        self.comboBox_2.addItems(self.lengthVar.keys())
        self.comboBox_3.addItems(self.lengthVar.keys())
        self.bind()

    def bind(self):
        self.comboBox.currentTextChanged.connect(self.typeChanged)
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        bigType = self.comboBox.currentText()
        # 获取第一个输入框的值
        value = self.lineEdit_1.text()
        if value == '':
            return

        currentType = self.comboBox_2.currentText()
        goalType = self.comboBox_3.currentText()

        standardization = float(value) * self.typeDict[bigType][currentType]
        result = standardization / self.typeDict[bigType][goalType]

        self.originalData.setText(f'{value} {currentType} =')
        self.convertedData.setText(f'{result} {goalType}')
        self.lineEdit_2.setText(str(result))

    def typeChanged(self, text):
        self.comboBox_2.clear()
        self.comboBox_3.clear()

        self.comboBox_2.addItems(self.typeDict[text].keys())
        self.comboBox_3.addItems(self.typeDict[text].keys())

        self.lineEdit_1.clear()
        self.lineEdit_2.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
