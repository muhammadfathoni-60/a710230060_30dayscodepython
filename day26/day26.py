# Import modul-modul yang diperlukan
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow  # Import kelas yang dihasilkan oleh pyuic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        current_text = self.ui.labelText.text()
        new_text = "Tombol telah diklik!"
        self.ui.labelText.setText(new_text)
        print(f"Label telah diubah dari '{current_text}' menjadi '{new_text}'")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
