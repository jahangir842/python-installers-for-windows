from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class DisplayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("This is the display area.")
        self.layout.addWidget(self.label)
