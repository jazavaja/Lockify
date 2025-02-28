import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel

from logic.main import process_inputs
from my_widgets.btn_custom import create_button
from my_widgets.input_str import create_input_field
from my_widgets.title_label_program import title_program


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

        title_label = title_program()
        layout.addWidget(title_label)

        # فیلد متن اول
        # self.input1 = QtWidgets.QLineEdit(self)
        # self.input1.setPlaceholderText("Enter your first input here...")
        # self.input1.setStyleSheet("""
        #     QLineEdit {
        #         padding: 10px;
        #         font-size: 14px;
        #         border: 2px solid #2E86C1;
        #         border-radius: 5px;
        #         margin-bottom: 10px;
        #     }
        #     QLineEdit:focus {
        #         border-color: #27AE60;
        #     }
        # """)

        # فیلد متن اول
        self.input1 = create_input_field("Enter your first input here...")
        layout.addWidget(self.input1)

        # فیلد متن دوم
        self.input2 = create_input_field("Enter your second input here...")
        layout.addWidget(self.input2)

        # دکمه
        self.button = create_button("Process", lambda: process_inputs(self.input1.text(), self.input2.text(), self.result_label))
        layout.addWidget(self.button)

        # ناحیه نمایش نتیجه
        result_frame = QtWidgets.QFrame()
        result_frame.setFrameStyle(QtWidgets.QFrame.Shape.NoFrame)
        result_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #2E86C1;
                border-radius: 10px;
                padding: 10px;
                background-color: #F2F3F4;
            }
        """)
        result_layout = QtWidgets.QVBoxLayout()

        self.result_label = QtWidgets.QLabel("Result will be shown here...")
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("""
            font-size: 16px;
            color: #27AE60;
        """)
        result_layout.addWidget(self.result_label)

        result_frame.setLayout(result_layout)
        layout.addWidget(result_frame)

        # اضافه کردن فاصله بین نتیجه و فوتر
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        layout.addItem(spacer)

        # اضافه کردن فوتر
        footer_layout = QtWidgets.QHBoxLayout()
        footer_layout.setSpacing(5)  # فاصله بین المان‌ها
        footer_layout.setContentsMargins(0, 0, 0, 0)  # حذف حاشیه‌های اطراف لایه

        # متن Donate
        donate_label = QtWidgets.QLabel("Support us by donating USDT(trx): ")
        donate_label.setStyleSheet("""
            font-size: 12px;
            color: #5D6D7E;
            padding: 0px;
            margin: 0px;
        """)
        footer_layout.addWidget(donate_label)

        # آدرس کیف پول
        self.wallet_address = QtWidgets.QLabel("TEDCd37BMNZAgvoc5tZTufFAWQ42UHU7Te")
        self.wallet_address.setStyleSheet("""
            font-size: 12px;
            color: #2E86C1;
            padding: 0px;
            margin: 0px;
        """)
        footer_layout.addWidget(self.wallet_address)

        # دکمه کپی
        copy_button = QtWidgets.QPushButton("📋")
        copy_button.setStyleSheet("""
            font-size: 12px;
            padding: 5px;
            border: none;
            background-color: transparent;
            color: #2E86C1;
        """)
        copy_button.clicked.connect(self.copy_to_clipboard)
        footer_layout.addWidget(copy_button)

        layout.addLayout(footer_layout)

        # اضافه کردن لینک‌های LinkedIn و GitHub
        social_layout = QtWidgets.QHBoxLayout()
        social_layout.setSpacing(10)  # فاصله بین لینک‌ها
        social_layout.setContentsMargins(0, 0, 0, 0)  # حذف حاشیه‌های اطراف لایه

        # لینک LinkedIn
        linkedin_label = QtWidgets.QLabel('<a href="https://www.linkedin.com/in/your-linkedin-profile">LinkedIn Me</a>')
        linkedin_label.setStyleSheet("""
            font-size: 12px;
            color: #2E86C1;
            text-decoration: none;
        """)
        linkedin_label.setOpenExternalLinks(True)  # اجازه باز کردن لینک در مرورگر
        social_layout.addWidget(linkedin_label)

        # لینک GitHub
        github_label = QtWidgets.QLabel('<a href="https://github.com/your-github-profile">My GitHub</a>')
        github_label.setStyleSheet("""
            font-size: 12px;
            color: #2E86C1;
            text-decoration: none;
        """)
        github_label.setOpenExternalLinks(True)  # اجازه باز کردن لینک در مرورگر
        social_layout.addWidget(github_label)

        # اضافه کردن لینک‌ها به لایه اصلی
        layout.addLayout(social_layout)

        # تنظیم لایه برای پنجره
        self.setLayout(layout)

    def on_button_click(self):
        # دریافت مقادیر از فیلدهای ورودی
        input1_text = self.input1.text()
        input2_text = self.input2.text()

        # نمایش نتیجه
        result = f"Input 1: {input1_text}\nInput 2: {input2_text}"
        self.result_label.setText(result)

    def copy_to_clipboard(self):
        # کپی کردن متن آدرس به کلیپ‌بورد
        clipboard = QApplication.clipboard()
        clipboard.setText(self.wallet_address.text())

        # نمایش پیام "Copied!"
        self.show_toast("Copied!")

    def show_toast(self, message):
        # ایجاد یک QLabel برای نمایش پیام
        toast = QLabel(message, self)
        toast.setStyleSheet("""
            background-color: #2E86C1;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
        """)
        toast.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        toast.setGeometry(10, 10, 100, 30)  # موقعیت و اندازه پیام
        toast.show()

        # پنهان کردن پیام پس از 2 ثانیه
        QTimer.singleShot(2000, toast.close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())
