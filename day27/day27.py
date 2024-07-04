import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Input dan Pesan PyQt5')

        # Membuat line edit (input teks)
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText('Masukkan nama Anda')

        # Membuat tombol
        self.button = QPushButton('Klik Saya!', self)
        self.button.clicked.connect(self.show_message_box)

        # Mengatur layout
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_message_box(self):
        # Mendapatkan teks dari line edit
        name = self.line_edit.text().strip()

        if name:
            # Menampilkan pesan dialog
            QMessageBox.information(self, 'Informasi', f'Halo, {name}! Anda telah mengklik tombol.')
        else:
            # Menampilkan pesan error jika line edit kosong
            QMessageBox.warning(self, 'Peringatan', 'Silakan masukkan nama Anda terlebih dahulu.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
