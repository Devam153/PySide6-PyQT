from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


def button_clicked():
    print("fdegdf")

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("button hold")
        button = QPushButton("fuck me ")
        button.clicked.connect(button_clicked)