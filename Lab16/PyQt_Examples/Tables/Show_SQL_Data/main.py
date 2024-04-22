from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from db.db import DB



def main():
    db = DB()
    db.insert_data() # Insert initial data
    app = QApplication([])
    window = MainWindow(db)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
