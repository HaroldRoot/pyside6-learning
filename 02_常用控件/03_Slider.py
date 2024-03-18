from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PySide6.QtCore import Qt


def showSlider(value):
    print(f'滑条当前的值为：{value}')
    # current_widget = self.sender()
    # print(current_widget.value())


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        slider1 = QSlider(Qt.Orientation.Horizontal)
        slider1.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider1.setTickInterval(5)
        # slider1.setMinimum(0)
        # slider1.setMaximum(100)
        slider1.setRange(0, 100)

        slider1.valueChanged.connect(showSlider)

        self.mainLayout.addWidget(slider1)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
