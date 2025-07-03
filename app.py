from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from pay import send_payment
class PaymentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.recipient_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.pay_button = QPushButton("Pay with Strike")
        self.status_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.recipient_input)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.pay_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        self.pay_button.clicked.connect(self.handle_payment)

    def handle_payment(self):
        recipient = self.recipient_input.text()
        amount = self.amount_input.text()
        result = send_payment(amount, recipient)
        if 'error' in result:
            self.status_label.setText(f"Error: {result['error']}")
        else:
            self.status_label.setText("Payment successful!")

if __name__ == "__main__":
    app = QApplication([])
    window = PaymentWindow()
    window.show()
    app.exec()