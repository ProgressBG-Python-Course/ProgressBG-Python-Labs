# 1. import needed QtWidgets classes
from PyQt6.QtWidgets import QApplication
import PyQt6.QtWidgets as qtw


def click_handler():
    print("Button was clicked")

# 2. the main app instance for our application.
app = QApplication([])

window = qtw.QWidget()
# 3. Create Qt widget, which will be our main window.

# Create a layout manager
layout = qtw.QVBoxLayout()

# Create the button
btnOk = qtw.QPushButton("OK")

# Add the button to the layout
layout.addWidget(btnOk)

# Set the layout for the window
window.setLayout(layout)


btnOk.clicked.connect(click_handler)

# 4. show the window
window.show()

# 5. Start the event loop
app.exec()