import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QDialog


class TicketDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Data Tiket Pesawat')

        self.name_label = QLabel('Nama:')
        self.name_edit = QLineEdit()

        self.destination_label = QLabel('Tujuan:')
        self.destination_edit = QLineEdit()

        self.date_label = QLabel('Tanggal Keberangkatan:')
        self.date_edit = QLineEdit()

        self.addButton = QPushButton('Tambah Data')
        self.addButton.clicked.connect(self.add_ticket)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Nama', 'Tujuan', 'Tanggal'])

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.destination_label)
        self.layout.addWidget(self.destination_edit)
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_edit)
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def add_ticket(self):
        name = self.name_edit.text()
        destination = self.destination_edit.text()
        date = self.date_edit.text()

        if not name or not destination or not date:
            QMessageBox.warning(self, 'Peringatan', 'Mohon lengkapi semua data')
            return

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(name))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(destination))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(date))

        self.name_edit.clear()
        self.destination_edit.clear()
        self.date_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TicketDialog()
    dialog.show()
    sys.exit(app.exec_())
