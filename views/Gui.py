import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication, QPushButton)
from controllers import controller


class Calc(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        self.lbl = QLabel(self)
        self.lbl.move(60, 40)


        self.qle = QLineEdit(self)
        self.qle.move(60, 100)


        btn = QPushButton(" = ", self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda: self.res())


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Calculator')
        self.show()


    def res(self):
         result = str(controller.calculate(str(self.qle.text())))
         self.lbl.setText(result)
         self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Calc()
    sys.exit(app.exec_())
