from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import *

import sys

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Tamagotchi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()

        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.hbox0.addWidget(self.status_text)
        self.hbox0.addStretch(1)

        self.hbox1.addWidget(QLabel('다마고치'))
        self.character_text = QTextEdit()
        self.character_text.setReadOnly(True)
        self.hbox1.addWidget(self.character_text)

        self.hbox1.addWidget(QLabel('밥주기'))
        self.feed_edit = QLineEdit()
        self.hbox1.addWidget(self.feed_edit)
        self.feedButton = QPushButton('입력')
        self.feedButton.clicked.connect(self.button_clicked)
        self.hbox1.addWidget(self.feedButton)

        self.cleanButton = QPushButton('씻기기')
        self.cleanButton.clicked.connect(self.button_clicked)
        self.sleepButton = QPushButton('재우기')
        self.sleepButton.clicked.connect(self.button_clicked)
        self.playButton = QPushButton('놀아주기')
        self.playButton.clicked.connect(self.button_clicked)
        self.studyButton = QPushButton('공부시키기')
        self.studyButton.clicked.connect(self.button_clicked)

        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.cleanButton)
        self.hbox2.addWidget(self.sleepButton)
        self.hbox2.addWidget(self.playButton)
        self.hbox2.addWidget(self.studyButton)

        self.hbox3.addWidget(QLabel('종합'))
        self.all_text = QTextEdit()
        self.all_text.setReadOnly(True)
        self.hbox3.addWidget(self.all_text)

        self.hbox4.addWidget(QLabel('배부름'))
        self.hunger_text = QTextEdit()
        self.hunger_text.setReadOnly(True)
        self.hbox4.addWidget(self.hunger_text)

        self.hbox5.addWidget(QLabel('청결'))
        self.clean_text = QTextEdit()
        self.clean_text.setReadOnly(True)
        self.hbox5.addWidget(self.clean_text)

        self.hbox6.addWidget(QLabel('피로도'))
        self.tired_text = QTextEdit()
        self.tired_text.setReadOnly(True)
        self.hbox6.addWidget(self.tired_text)

        self.hbox7.addWidget(QLabel('스트레스'))
        self.stress_text = QTextEdit()
        self.stress_text.setReadOnly(True)
        self.hbox7.addWidget(self.stress_text)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle('Tamatgotchi')

        self.show()

    def button_clicked(self):
        key = self.sender().text()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tamagotchi()
    sys.exit(app.exec_())
