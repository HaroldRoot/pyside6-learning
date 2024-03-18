from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPlainTextEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # textEdit = QTextEdit()
        # textEdit.setHtml('<h1>这是标题</h1><b>这是粗体</b><i>这是斜体</i>')
        # textEdit.setMarkdown('# 这是 Markdown 大标题')
        # textEdit.setPlainText('这是纯文本')

        textEdit = QPlainTextEdit()
        textEdit.setPlainText('这是一个标题')
        textEdit.appendPlainText('这是一个段落')
        btn = QPushButton('追加文本')
        btn.clicked.connect(lambda: textEdit.appendPlainText('这是一个段落'))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(textEdit)
        self.mainLayout.addWidget(btn)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()