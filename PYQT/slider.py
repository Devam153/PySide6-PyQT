from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("slider moved to: ", data)

app = QApplication()
slider = QSlider(Qt.Vertical)
#we can do horizontal too with an H and a V case sensitive

slider.setMinimum(1)
slider.setMaximum(200)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()