Here’s a Python desktop application using **PyQt** with multiple modules and files to give you a practical example. This application will include:

- A **main window** with a menu and navigation.
- A **form** for user input.
- A **display** area for output.
- Modular code split across multiple `.py` files.

---

### **Project Structure**

```plaintext
my_app/
├── main.py           # Entry point of the application
├── ui/
│   ├── main_window.py # Main window logic
│   ├── form.py        # Form handling logic
│   ├── display.py     # Display handling logic
├── utils/
│   ├── data_handler.py # Utility for handling data
├── assets/           # Icons or additional resources
└── installer/        # Installer files (to be generated later)
```

---

### **Code**

#### 1. **`main.py`** (Entry Point)

```python
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```

---

#### 2. **`ui/main_window.py`** (Main Window)

```python
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
```

---

#### 3. **`ui/form.py`** (Form Handling)

```python
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
```

---

#### 4. **`ui/display.py`** (Display Widget)

```python
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class DisplayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("This is the display area.")
        self.layout.addWidget(self.label)
```

---

#### 5. **`utils/data_handler.py`** (Utility Module)

```python
def process_data(data):
    return data.upper()
```

---

### **Convert to `.exe`**

1. **Install `pyinstaller`:**

   ```bash
   pip install pyinstaller
   ```

2. **Generate Executable:**
   Run this command in the terminal:

   ```bash
   pyinstaller --noconfirm --onefile --windowed main.py
   ```

   - `--noconfirm`: Automatically overwrite previous builds.
   - `--onefile`: Bundle everything into a single `.exe`.
   - `--windowed`: Hides the console window (useful for GUI apps).

   The `.exe` file will be generated in the `dist/` folder.

---

### **Create a Windows Installer**

1. **Install `NSIS`:**
   Download and install NSIS from [NSIS Official Website](https://nsis.sourceforge.io/Download).

2. **Create Installer Script (`installer_script.nsi`):**
   Example script:

   ```nsi
   OutFile "MyAppInstaller.exe"
   InstallDir "$PROGRAMFILES\MyApp"
   RequestExecutionLevel admin

   Section
       SetOutPath "$INSTDIR"
       File "dist\main.exe"
       CreateShortcut "$DESKTOP\MyApp.lnk" "$INSTDIR\main.exe"
   SectionEnd
   ```

3. **Compile Installer:**
   Open NSIS, load the `.nsi` script, and compile it to generate the installer.

---

This application demonstrates modularity and can be scaled to more complex functionalities. Let me know if you'd like further details or enhancements!
