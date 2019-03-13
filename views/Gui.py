import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication, QPushButton)
from controllers import controller


class Calc(QWidget):

    def __init__(self):
        super().__init__()

        self.qle = QLineEdit(self)
        self.lbl = QLabel(self)
        self.initUI()

    def initUI(self):

        self.lbl.move(145, 57)

        self.qle.move(60, 10)

        btn = QPushButton(" = ", self)
        btn.resize(btn.sizeHint())
        btn.move(60, 52)
        btn.clicked.connect(lambda: self.res())

        self.setGeometry(300, 300, 480, 100)
        self.setWindowTitle('Calculator')
        self.show()

    def res(self):
        try:
            result = str(controller.calculate(str(self.qle.text())))
            self.lbl.setText(result)
            self.lbl.adjustSize()
        except Exception:
            self.lbl.setText("Unfortunately, an error has appeared. Try something else.")
            self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    sys.exit(app.exec_())
