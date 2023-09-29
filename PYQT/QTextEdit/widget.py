from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Demo")

        self.text_Edit = QTextEdit()

        # BUTTONS

        current_text_button = QPushButton("set current text")
        current_text_button.clicked.connect(self.set_current_text)

        copy_button = QPushButton("copy")
        copy_button.clicked.connect(self.text_Edit.copy)

        cut_button = QPushButton("cut")
        cut_button.clicked.connect(self.text_Edit.cut)

        paste_button = QPushButton("paste")
        paste_button.clicked.connect(self.text_Edit.paste)

        undo_button = QPushButton("undo")
        undo_button.clicked.connect(self.text_Edit.undo)

        redo_button = QPushButton("redo")
        redo_button.clicked.connect(self.text_Edit.redo)

        set_plain_text_button = QPushButton("set plain text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("set html")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("clear")
        clear_button.clicked.connect(self.text_Edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_Edit)

        self.setLayout(v_layout)

    def set_current_text(self):
        print(self.text_Edit.toPlainText())

    def set_plain_text(self):
        self.text_Edit.setPlainText("WASSUPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")

    def set_html(self):
        self.text_Edit.setHtml("<!DOCTYPE html><html><head><title>My HTML Example</title></head><body><h1>Hello, World!</h1><p>This is an example of HTML code.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></body></html>")
