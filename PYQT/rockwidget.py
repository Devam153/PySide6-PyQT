from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout 
class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROCKWIDGET")

        x = int(input("How many buttons do you want? "))
        button_layout = QVBoxLayout()

        for i in range(x):
            button = QPushButton(f"Button {i+1}")
            button.clicked.connect(self.button_clicked)
            button_layout.addWidget(button)
        
        self.setLayout(button_layout)

    def button_clicked(self):
        sender = self.sender()
        button_text = sender.text()
        print(f"{button_text} clicked")
