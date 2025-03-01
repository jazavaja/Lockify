from PyQt6.QtWidgets import QLabel


def linkedin_label_widget():
    # لینک LinkedIn
    linkedin_label = QLabel('<a href="https://www.linkedin.com/in/your-linkedin-profile">LinkedIn Me</a>')
    linkedin_label.setStyleSheet("""
                font-size: 12px;
                color: #2E86C1;
                text-decoration: none;
            """)
    linkedin_label.setOpenExternalLinks(True)  # اجازه باز کردن لینک در مرورگر
    return linkedin_label