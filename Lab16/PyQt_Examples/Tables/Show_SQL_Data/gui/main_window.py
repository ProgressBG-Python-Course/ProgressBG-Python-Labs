from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, db):
        self.db = db
        super().__init__()
        self.setWindowTitle("SQLAlchemy with PyQt6")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_data()

    def load_data(self):
        users = self.db.fetch_users()
        self.table_widget.setRowCount(len(users))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Email"])

        for i, user in enumerate(users):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(user.id)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(user.name))
            self.table_widget.setItem(i, 2, QTableWidgetItem(user.email))
