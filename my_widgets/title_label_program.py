from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

def title_program():
    # متن بزرگ "Crypto Security"
    title_label = QLabel("Crypto Security")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("""
                font-size: 24px;
                font-weight: bold;
                color: #2E86C1;
                margin-bottom: 20px;
            """)
    return title_label
