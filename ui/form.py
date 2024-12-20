from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox

class FormWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.name_input = QLineEdit()
        self.layout.addRow("Name:", self.name_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        self.layout.addWidget(self.submit_button)

    def submit_form(self):
        name = self.name_input.text()
        QMessageBox.information(self, "Form Submitted", f"Hello, {name}!")
