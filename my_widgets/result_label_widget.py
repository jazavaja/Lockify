from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

def create_result_label():
    label = QLabel("Result will be shown here...")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("""
        font-size: 16px;
        color: #27AE60;
    """)
    return label
