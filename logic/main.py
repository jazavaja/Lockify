from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel


def process_inputs(input1, input2, result_label):
    result = f"Input 1: {input1}\nInput 2: {input2}"
    result_label.setText(result)


def copy_to_clipboard(text, parent):
    clipboard = QApplication.clipboard()
    clipboard.setText(text)
    show_toast("Copied!", parent)


def show_toast(message, parent):
    toast = QLabel(message, parent)
    toast.setStyleSheet("""
        background-color: #2E86C1;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    """)
    toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
    toast.setGeometry(10, 10, 100, 30)
    toast.show()
    QTimer.singleShot(2000, toast.close)
