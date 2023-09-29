import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader 

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("untitled.ui", None)

def do_something():
    print(window.lineEdit1.text(), "is a", window.lineEdit_2.text())


window.setWindowTitle("user data")


window.push_Button1.clicked.connect(do_something)
window.show()
app.exec()