import sys
from PyQt5.QtWidgets import *

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Морзе")
w.setMinimumSize(400, 250)  
w.resize(500, 280)         

out = QLineEdit()
out.setReadOnly(True)
out.setPlaceholderText("Нажмите на букву...")
out.setMinimumHeight(35)

clear = QPushButton("Очистить")
clear.clicked.connect(out.clear)
clear.setMaximumWidth(80)  

def add_morse(letter):
    if out.text():
        out.setText(out.text() + " " + MORSE[letter])
    else:
        out.setText(MORSE[letter])

top = QHBoxLayout()
top.addWidget(out, stretch=1)  
top.addWidget(clear)

# Кнопки букв в 3 ряда
letters = sorted(MORSE.keys())
button_layout = QGridLayout()
button_layout.setSpacing(5)

# Распределяем буквы по рядам
row, col = 0, 0
for letter in letters:
    btn = QPushButton(letter)
    btn.setMinimumHeight(40)
    btn.setMinimumWidth(40)
    btn.clicked.connect(lambda checked, l=letter: add_morse(l))
    button_layout.addWidget(btn, row, col)
    col += 1
    if col > 8:  # 9 букв в ряду
        col = 0
        row += 1

main = QVBoxLayout()
main.addLayout(top)
main.addLayout(button_layout)
w.setLayout(main)

w.show()
sys.exit(app.exec_())