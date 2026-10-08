import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Калькулятор")
w.setGeometry(400, 300, 280, 420)
w.setStyleSheet("background-color: #1a1a2e;")

d = QLineEdit()
d.setReadOnly(True)
d.setAlignment(Qt.AlignRight)
d.setMinimumHeight(60)
d.setStyleSheet("""
    QLineEdit {
        font-size: 28px;
        font-weight: bold;
        padding: 15px;
        background-color: #16213e;
        color: white;
        border: none;
        border-radius: 10px;
    }
""")

cur = ""     
f = None      
o = None     

def click(t):
    global cur, f, o

    if t == "C":
        cur, f, o = "", None, None
        d.setText("")

    elif t == "=":
        if cur and f is not None and o is not None:
            try:
                s = float(cur)

                if o == "/" and s == 0:
                    d.setText("Ошибка: деление на 0")
                    cur, f, o = "", None, None
                    return

                r = eval(f"{f} {o} {s}")
                # убираем лишние нули: 5.0 -> 5
                if r == int(r):
                    r = int(r)
                d.setText(str(r))

                cur = str(r)
                f = None
                o = None
            except Exception:
                d.setText("Ошибка")
                cur, f, o = "", None, None

    elif t in "+-*/":
        if cur:
            if f is not None and o is not None:
                try:
                    s = float(cur)
                    if o == "/" and s == 0:
                        d.setText("Ошибка: деление на 0")
                        cur, f, o = "", None, None
                        return
                    r = eval(f"{f} {o} {s}")
                    if r == int(r):
                        r = int(r)
                    f = float(r)
                    cur = str(r)
                    d.setText(cur)
                except Exception:
                    d.setText("Ошибка")
                    cur, f, o = "", None, None
                    return
            else:
                f = float(cur)

            o = t
            cur = ""

    else:  
        if t == ".":
            if "." not in cur:
                cur += "." if cur else "0."
        else:
            cur += t
        d.setText(cur)

l = QVBoxLayout()
l.setSpacing(10)
l.addWidget(d)

g = QGridLayout()
g.setSpacing(8)

btns = [
    ["C", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for r in range(len(btns)):
    for c, t in enumerate(btns[r]):
        b = QPushButton(t)
        b.setMinimumHeight(55)

        style = """
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                border: none;
                border-radius: 12px;
                color: white;
            }
            QPushButton:hover {
                background-color: #3d3d5a;
            }
            QPushButton:pressed {
                background-color: #4a4a6a;
            }
        """

        if t == "C":
            style += """
                QPushButton {
                    background-color: #e94560;
                }
                QPushButton:hover {
                    background-color: #c73652;
                }
            """
        elif t in "+-*/":
            style += """
                QPushButton {
                    background-color: #0f3460;
                }
                QPushButton:hover {
                    background-color: #1a4a7a;
                }
            """
        elif t == "=":
            style += """
                QPushButton {
                    background-color: #00b894;
                }
                QPushButton:hover {
                    background-color: #00a383;
                }
            """
        else:
            style += """
                QPushButton {
                    background-color: #2d2d44;
                }
                QPushButton:hover {
                    background-color: #3d3d5a;
                }
            """

        b.setStyleSheet(style)
        b.clicked.connect(lambda checked, txt=t: click(txt))
        g.addWidget(b, r, c)

l.addLayout(g)
w.setLayout(l)
w.show()
sys.exit(app.exec_())