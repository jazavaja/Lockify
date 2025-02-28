from PyQt6.QtWidgets import QLineEdit

def create_input_field(placeholder_text):
    input_field = QLineEdit()
    input_field.setPlaceholderText(placeholder_text)
    input_field.setStyleSheet("""
        QLineEdit {
            padding: 10px;
            font-size: 14px;
            border: 2px solid #2E86C1;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        QLineEdit:focus {
            border-color: #27AE60;
        }
    """)
    return input_field