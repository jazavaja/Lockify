import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QApplication

from helper.path_helper import resource_path
from logic.main import process_encrypt, process_decrypt
from my_widgets.about_us_btn import about_us_btn_click
from my_widgets.btn_custom import create_button
from my_widgets.copy_btn import copy_btn
from my_widgets.donate_text import donate_text_widget
from my_widgets.github_label import github_button_widget
from my_widgets.help_use_btn import help_use_button_widget
from my_widgets.input_str import create_input_field
from my_widgets.linkedin_label import linkedin_button_widget
from my_widgets.result_label_widget import create_result_label
from my_widgets.title_label_program import title_program
from my_widgets.wallet_label import wallet_label


class CryptoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button2 = None
        self.button1 = None
        self.input2 = None
        self.input1 = None
        self.button = None
        self.result_label = None
        self.init_ui()

    def init_ui(self):
        title = "Lockify"
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 500, 300)
        self.setWindowIcon(QIcon("lockify.ico"))

        layout = QtWidgets.QGridLayout()

        title_label = title_program("lockify.ico")
        layout.addWidget(title_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.input1 = create_input_field("Enter the text you want to encrypt or the encrypted data to decrypt")
        layout.addWidget(self.input1, 1, 0, 1, 2)

        self.input2 = create_input_field("Enter the secret key used for encryption/decryption")
        layout.addWidget(self.input2, 2, 0, 1, 2)

        self.button1 = create_button("Encrypt")
        self.button1.clicked.connect(self.handle_encrypt)

        self.button2 = create_button("Decrypt")
        self.button2.clicked.connect(self.handle_decrypt)

        layout.addWidget(self.button1, 3, 0)
        layout.addWidget(self.button2, 3, 1)

        self.result_label = create_result_label(self)
        layout.addWidget(self.result_label, 4, 0, 1, 2)

        # ایجاد یک خط تفکیکی
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.Shape.HLine)
        separator_line.setLineWidth(2)
        separator_line.setStyleSheet("color: blue;")

        layout.addWidget(separator_line, 5, 0, 1, 2)

        footer_layout = QtWidgets.QHBoxLayout()
        footer_layout.setSpacing(5)
        footer_layout.setContentsMargins(0, 100, 0, 0)

        # layout.setVerticalSpacing(20) i do not wannt space in all element

        donate_label = donate_text_widget()
        footer_layout.addWidget(donate_label)

        wallet_address = wallet_label()
        footer_layout.addWidget(wallet_address)

        copy_button = copy_btn(wallet_address, self)
        footer_layout.addWidget(copy_button)

        layout.addLayout(footer_layout, 5, 0, 1, 2)

        social_layout = QtWidgets.QHBoxLayout()
        social_layout.setSpacing(10)
        social_layout.setContentsMargins(0, 0, 0, 0)

        linkedin_label = linkedin_button_widget()
        social_layout.addWidget(linkedin_label)

        github_label = github_button_widget()
        social_layout.addWidget(github_label)

        help_use = help_use_button_widget()
        social_layout.addWidget(help_use)

        about_us = about_us_btn_click()
        social_layout.addWidget(about_us)

        layout.addLayout(social_layout, 6, 0, 1, 2)

        self.setLayout(layout)

    def handle_encrypt(self):
        process_encrypt(self.input1.text(), self.input2.text(), self.result_label)

    def handle_decrypt(self):
        process_decrypt(self.input1.text(), self.input2.text(), self.result_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    stylesheet_path = resource_path("stylesheet.qss")
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Error: Unable to find stylesheet at {stylesheet_path}")
        sys.exit(1)

    window = CryptoApp()
    window.show()
    sys.exit(app.exec())
