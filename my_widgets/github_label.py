from PyQt6.QtWidgets import QLabel


def github_label_widget():
    github_label = QLabel('<a href="https://github.com/jazavaja">My GitHub</a>')
    github_label.setStyleSheet("""
                font-size: 12px;
                color: #2E86C1;
                text-decoration: none;
            """)
    github_label.setOpenExternalLinks(True)  # اجازه باز کردن لینک در مرورگر
    return github_label