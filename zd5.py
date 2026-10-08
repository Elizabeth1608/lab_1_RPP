import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Заказ")
w.setGeometry(300, 300, 450, 400)

menu = {"Шаурма":350, "Суп":250, "Суши":400, "Пирог":300, "Салат":180, "Шашлык":550}
cb = {}
sp = {}

def update():
    total = 0
    text = "\n   Ваш заказ   \n"
    empty = True
    for dish, price in menu.items():
        if cb[dish].isChecked():
            count = sp[dish].value()
            if count == 0:
                count = 1
                sp[dish].setValue(1)
            total += price * count
            text += f"{dish}: {count} шт. × {price} = {price * count} руб.\n\n"
            empty = False
    text += "Заказ пуст" if empty else "-"*40 + f"\nИТОГО: {total} руб.\n" + "-"*40 + "\nСпасибо!"
    receipt.setPlainText(text)

def clear():
    for dish in menu:
        cb[dish].setChecked(False)
        sp[dish].setValue(0)
        sp[dish].setEnabled(False)
    receipt.clear()

def toggle(dish):
    sp[dish].setEnabled(cb[dish].isChecked())
    if cb[dish].isChecked() and sp[dish].value() == 0:
        sp[dish].setValue(1)
    update()

menu_layout = QVBoxLayout()
for dish, price in menu.items():
    row = QHBoxLayout()
    
    c = QCheckBox()
    c.stateChanged.connect(lambda checked, d=dish: toggle(d))
    cb[dish] = c  
    
    s = QSpinBox()
    s.setRange(0, 10)
    s.setEnabled(False)
    s.valueChanged.connect(update)
    sp[dish] = s
    
    row.addWidget(c)
    row.addWidget(QLabel(f"{dish} - {price} руб."))
    row.addWidget(s)
    menu_layout.addLayout(row)

receipt = QPlainTextEdit()
receipt.setReadOnly(True)
receipt.setMinimumHeight(150)

clear_btn = QPushButton("Очистить")
clear_btn.clicked.connect(clear)

layout = QVBoxLayout()
layout.addWidget(QLabel("Выберите блюда:"))
layout.addLayout(menu_layout)
layout.addWidget(QLabel("Чек:"))
layout.addWidget(receipt)
layout.addWidget(clear_btn)

w.setLayout(layout)
w.show()
sys.exit(app.exec_())