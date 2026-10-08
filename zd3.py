import sys
from PyQt5.QtWidgets import *

def toggle_visibility(state, widget):
    widget.setVisible(state == 2)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Управление видимостью")
window.setGeometry(300, 300, 400, 200)

line_edit = QLineEdit()
line_edit.setPlaceholderText("Поле для ввода")

button = QPushButton("Кнопка")

label = QLabel("Метка")
label.setStyleSheet("border: 1px solid gray; padding: 5px;")

cb1 = QCheckBox("Показать поле")
cb1.setChecked(True)
cb1.stateChanged.connect(lambda state: toggle_visibility(state, line_edit))

cb2 = QCheckBox("Показать кнопку")
cb2.setChecked(True)
cb2.stateChanged.connect(lambda state: toggle_visibility(state, button))

cb3 = QCheckBox("Показать метку")
cb3.setChecked(True)
cb3.stateChanged.connect(lambda state: toggle_visibility(state, label))

layout = QVBoxLayout()
for widget, checkbox in [(line_edit, cb1), (button, cb2), (label, cb3)]:
    h_layout = QHBoxLayout()
    h_layout.addWidget(widget)
    h_layout.addWidget(checkbox)
    layout.addLayout(h_layout)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())