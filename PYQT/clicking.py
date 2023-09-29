from PySide6.QtWidgets import QApplication, QPushButton

def buttong_clicked(data):
    print(":Fudgg", data)

app = QApplication()
button = QPushButton("FUCK ME")
button.setCheckable(True)
#However, if you don't set setCheckable(False) or use setCheckable(True) explicitly, 
# the default behavior is that the button is checkable. In this case, 
# the button remains in a toggled state after each click, alternating between "checked" and "unchecked" states. 
# This behavior is useful for scenarios where you want to toggle a button's state.
button.clicked.connect(buttong_clicked)

button.show()
app.exec()