import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QTextEdit, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ComboBox and QTextEdit Example')
        self.setGeometry(300, 300, 300, 200)

        # Label untuk instruksi
        self.label = QLabel('Select a language:', self)

        # ComboBox untuk pilihan bahasa
        self.combobox = QComboBox(self)
        self.combobox.addItem('Python')
        self.combobox.addItem('JavaScript')
        self.combobox.addItem('Java')
        self.combobox.addItem('C++')
        self.combobox.addItem('Ruby')
        self.combobox.activated.connect(self.on_combobox_activated)

        # QTextEdit untuk menampilkan teks terkait
        self.textedit = QTextEdit(self)
        self.textedit.setReadOnly(True)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.combobox)
        vbox.addWidget(self.textedit)

        self.setLayout(vbox)

    def on_combobox_activated(self, index):
        selected_language = self.combobox.itemText(index)
        if selected_language == 'Python':
            self.textedit.setPlainText('Python is a powerful programming language.')
        elif selected_language == 'JavaScript':
            self.textedit.setPlainText('JavaScript is a scripting language used for web development.')
        elif selected_language == 'Java':
            self.textedit.setPlainText('Java is a widely used programming language for building enterprise-scale applications.')
        elif selected_language == 'C++':
            self.textedit.setPlainText('C++ is a general-purpose programming language known for its performance and flexibility.')
        elif selected_language == 'Ruby':
            self.textedit.setPlainText('Ruby is a dynamic programming language used primarily for web development and scripting.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
