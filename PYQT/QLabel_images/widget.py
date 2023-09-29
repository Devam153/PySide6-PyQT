from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("qlabel with imaage")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("corpse.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)