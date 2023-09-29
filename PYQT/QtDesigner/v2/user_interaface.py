from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("untitled.ui", None)
        self.ui.setWindowTitle("user data")
        self.ui.push_Button1.clicked.connect(self.do_something)
    
    def show(self):
        self.ui.show()

    def do_something(self):
        print(self.ui.lineEdit1.text(), "is a", self.ui.lineEdit_2.text())