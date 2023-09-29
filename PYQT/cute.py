import sys
from PySide6.QtWidgets import QApplication
from button import ButtonHolder



app = QApplication(sys.argv)
window = ButtonHolder()

window.show()

app.exec()


