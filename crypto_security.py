import sys
from PyQt6 import QtWidgets, QtCore, QtGui

class CryptoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # تنظیمات پنجره
        self.setWindowTitle("Crypto Security")
        self.setGeometry(100, 100, 400, 300)

        # ایجاد لایه‌های عمودی
        layout = QtWidgets.QVBoxLayout()

        # متن بزرگ "Crypto Security"
        title_label = QtWidgets.QLabel("Crypto Security")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2E86C1;
            margin-bottom: 20px;
        """)
        layout.addWidget(title_label)

        # فیلد متن اول
        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setPlaceholderText("Enter your first input here...")
        self.input1.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #2E86C1;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            QLineEdit:focus {
                border-color: #27AE60;
            }
        """)
        layout.addWidget(self.input1)

        # فیلد متن دوم
        self.input2 = QtWidgets.QLineEdit(self)
        self.input2.setPlaceholderText("Enter your second input here...")
        self.input2.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #2E86C1;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            QLineEdit:focus {
                border-color: #27AE60;
            }
        """)
        layout.addWidget(self.input2)

        # دکمه
        self.button = QtWidgets.QPushButton("Process", self)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #2E86C1;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            QPushButton:pressed {
                background-color: #1E8449;
            }
        """)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # ناحیه نمایش نتیجه
        result_frame = QtWidgets.QFrame()  # ایجاد یک QFrame برای کادر
        result_frame.setFrameStyle(QtWidgets.QFrame.Shape.Box)  # نوع کادر
        result_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #2E86C1;
                border-radius: 10px;  /* گرد کردن حاشیه */
                padding: 10px;       /* فضای داخلی کادر */
                background-color: #F2F3F4;  /* رنگ پس‌زمینه */
            }
        """)
        result_layout = QtWidgets.QVBoxLayout()  # لایه عمودی برای متن داخل کادر

        self.result_label = QtWidgets.QLabel("Result will be shown here...")
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("""
            font-size: 16px;
            color: #27AE60;
        """)
        result_layout.addWidget(self.result_label)

        result_frame.setLayout(result_layout)  # تنظیم لایه داخل QFrame
        layout.addWidget(result_frame)  # اضافه کردن کادر به لایه اصلی

        # اضافه کردن فاصله بین کادر نتیجه و فوتر
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        layout.addItem(spacer)

        # اضافه کردن فوتر
        footer_layout = QtWidgets.QHBoxLayout()

        # متن Donate
        donate_label = QtWidgets.QLabel("Support us by donating USDT(trx):")
        donate_label.setStyleSheet("""
            font-size: 12px;
            color: #5D6D7E;
        """)
        footer_layout.addWidget(donate_label)

        # آدرس کیف پول
        wallet_address = QtWidgets.QLabel("TEDCd37BMNZAgvoc5tZTufFAWQ42UHU7Te")
        wallet_address.setStyleSheet("""
            font-size: 12px;
            color: #2E86C1;
        """)
        footer_layout.addWidget(wallet_address)

        # اضافه کردن فوتر به لایه اصلی
        layout.addLayout(footer_layout)

        # تنظیم لایه برای پنجره
        self.setLayout(layout)

    def on_button_click(self):
        # دریافت مقادیر از فیلدهای ورودی
        input1_text = self.input1.text()
        input2_text = self.input2.text()

        # نمایش نتیجه
        result = f"Input 1: {input1_text}\nInput 2: {input2_text}"
        self.result_label.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())