from PyQt6.QtWidgets import QPushButton, QMessageBox

def about_us_btn_click():
    about_us = QPushButton('About project')

    def show_about_dialog():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("About Project")
        msg_box.setText("This is a Crypto Security application.\nDeveloped by: Your Name\nVersion: 1.0")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    about_us.clicked.connect(show_about_dialog)

    return about_us
