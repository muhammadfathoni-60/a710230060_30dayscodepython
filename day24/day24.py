import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class TaxCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Tax Calculator')
        
        self.lbl_income = QLabel('Enter your income:')
        self.edit_income = QLineEdit()
        
        self.btn_calculate = QPushButton('Calculate Tax')
        self.btn_calculate.clicked.connect(self.calculate_tax)
        
        self.lbl_result = QLabel('Tax amount will be shown here.')
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_income)
        vbox.addWidget(self.edit_income)
        vbox.addWidget(self.btn_calculate)
        vbox.addWidget(self.lbl_result)
        
        self.setLayout(vbox)
        
    def calculate_tax(self):
        try:
            income = float(self.edit_income.text())
            if income < 0:
                raise ValueError
            if income <= 10000:
                tax = 0
            elif income <= 50000:
                tax = (income - 10000) * 0.1
            else:
                tax = (income - 50000) * 0.2 + 4000
            
            self.lbl_result.setText(f'Tax to be paid: ${tax:.2f}')
        
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid positive number for income.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = TaxCalculator()
    calculator.show()
    sys.exit(app.exec_())
