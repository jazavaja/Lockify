from PyQt6.QtWidgets import QPushButton

def create_button(text, on_click):
    button = QPushButton(text)
    button.setStyleSheet("""
        QPushButton {
            background-color: #2E86C1;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
            border: none;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        QPushButton:hover {
            background-color: #27AE60;
        }
        QPushButton:pressed {
            background-color: #1E8449;
        }
    """)
    button.clicked.connect(on_click)
    return button