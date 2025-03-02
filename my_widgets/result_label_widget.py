from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

def create_result_label():
    label = QLabel("Result will be shown here...")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setObjectName("resultLabel")
    label.setStyleSheet("""
        border: 2px solid #2E86C1;
        border-radius: 10px;
        padding: 10px;
        background-color: #F2F3F4;
        font-size: 16px;
        color: #27AE60;
    """)
    return label
