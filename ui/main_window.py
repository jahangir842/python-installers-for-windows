from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton
from ui.form import FormWidget
from ui.display import DisplayWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Module PyQt Application")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Add pages
        self.form_widget = FormWidget(self)
        self.display_widget = DisplayWidget(self)

        self.stack.addWidget(self.form_widget)
        self.stack.addWidget(self.display_widget)

        # Navigation
        self.nav_button = QPushButton("Go to Display")
        self.nav_button.clicked.connect(self.show_display)
        self.layout.addWidget(self.nav_button)

    def show_display(self):
        self.stack.setCurrentWidget(self.display_widget)
