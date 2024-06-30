import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)  # Mengatur ukuran dan posisi jendela
        self.setWindowTitle('Contoh Aplikasi PyQt')  # Judul jendela

        # Membuat tombol
        self.button = QPushButton('Klik Saya', self)
        self.button.setGeometry(100, 100, 100, 50)  # Mengatur ukuran dan posisi tombol
        self.button.clicked.connect(self.showDialog)  # Menghubungkan klik tombol dengan metode showDialog

    def showDialog(self):
        QMessageBox.information(self, 'Pesan', 'Halo! Anda telah mengklik tombol.')  # Menampilkan pesan informasi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
