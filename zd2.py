import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Калькулятор")
window.setGeometry(500, 300, 500, 80)

def calculate():
    try:
        output_field.setText(str(eval(input_field.text())))
    except:
        output_field.setText("Ошибка")

input_field = QLineEdit()
input_field.setPlaceholderText("Введите выражение")

button = QPushButton("Вычислить")
button.clicked.connect(calculate)

output_field = QLineEdit()
output_field.setPlaceholderText("Результат")
output_field.setReadOnly(True)

layout = QHBoxLayout()
layout.addWidget(input_field)
layout.addWidget(button)
layout.addWidget(output_field)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())