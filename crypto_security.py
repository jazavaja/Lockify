import sys

from PyQt6 import QtWidgets

from logic.main import process_inputs
from my_widgets.about_us_btn import about_us_btn_click
from my_widgets.btn_custom import create_button
from my_widgets.copy_btn import copy_btn
from my_widgets.donate_text import donate_text_widget
from my_widgets.github_label import github_label_widget
from my_widgets.input_str import create_input_field
from my_widgets.linkedin_label import linkedin_label_widget
from my_widgets.result_label_widget import create_result_label
from my_widgets.title_label_program import title_program
from my_widgets.wallet_label import wallet_label


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
        self.input1 = create_input_field("Enter your first input here...")
        layout.addWidget(self.input1)

        # فیلد متن دوم
        self.input2 = create_input_field("Enter your second input here...")
        layout.addWidget(self.input2)

        # دکمه
        self.button = create_button("Process",
                                    lambda: process_inputs(self.input1.text(), self.input2.text(), self.result_label))
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

        self.result_label = create_result_label()
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

        donate_label = donate_text_widget()
        footer_layout.addWidget(donate_label)

        # آدرس کیف پول
        wallet_address = wallet_label()
        footer_layout.addWidget(wallet_address)

        # دکمه کپی
        copy_button = copy_btn(wallet_address, self)
        footer_layout.addWidget(copy_button)

        layout.addLayout(footer_layout)

        # اضافه کردن لینک‌های LinkedIn و GitHub
        social_layout = QtWidgets.QHBoxLayout()
        social_layout.setSpacing(10)  # فاصله بین لینک‌ها
        social_layout.setContentsMargins(0, 0, 0, 0)  # حذف حاشیه‌های اطراف لایه

        linkedin_label = linkedin_label_widget()
        social_layout.addWidget(linkedin_label)

        github_label = github_label_widget()
        social_layout.addWidget(github_label)

        aboutus = about_us_btn_click()
        social_layout.addWidget(aboutus)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())
