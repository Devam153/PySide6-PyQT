from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app 
        self.setWindowTitle("custom main window")

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("copy")
        edit_menu.addAction("cut")
        edit_menu.addAction("paste")
        edit_menu.addAction("undo")
        edit_menu.addAction("redo")

        #a bunch of other menus
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        #working with toolbars
        toolbar =  QToolBar("my main tool bar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #adding quit action inside the toolbar
        toolbar.addAction(quit_action)

        #adding another action
        action1 = QAction("some action", self)
        action1.setStatusTip("status message")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("aboutIcon.png"), "some other action", self)
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("click here"))

        #working with status bar
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("button me up")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def button1_clicked(self):
        print("button clicked")    

    def quit_app(self):
        ret = QMessageBox.question(self,"Message Title",
                                        "are you sure you want to quit?",
                                        QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes: 
            self.app.quit()
        else : 
            print("okay!")

    def toolbar_button_click(self):
        self.statusBar().showMessage("message from my app", 3000)
