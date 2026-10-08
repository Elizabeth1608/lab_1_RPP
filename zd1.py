import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Перекидыватель")
w.setGeometry(500, 300, 400, 80)

t = ""
r = True

f1 = QLineEdit()
f1.setPlaceholderText("Введите")

b = QPushButton("→")
def click():
    global t, r
    if r:
        t = f1.text()
        if t:
            f2.setText(t)
            f1.clear()
            b.setText("<-")
            r = False
    else:
        f1.setText(t)
        f2.clear()
        b.setText("->")
        r = True
b.clicked.connect(click)

f2 = QLineEdit()
f2.setPlaceholderText("Сюда")
f2.setReadOnly(True)

l = QHBoxLayout()
l.addWidget(f1)
l.addWidget(b)
l.addWidget(f2)
w.setLayout(l)

w.show()
sys.exit(app.exec_())