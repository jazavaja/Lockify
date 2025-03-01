from PyQt6.QtWidgets import QPushButton


def about_us_btn_click():
    about_us = QPushButton('About project')
    about_us.setStyleSheet("""
                        font-size: 12px;
                        color: #2E86C1;
                        text-decoration: none;
                    """)

    return about_us