from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QLabel

from logic.copy_with_toast import copy_to_clipboard


class ClickableLabel(QLabel):
    def __init__(self, text=None, parent=None):
        super().__init__(text, parent)
        self.setObjectName("resultLabel")
        self.original_text = text

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.handle_click(self.parent())

    def handle_click(self, parent):
        copy_to_clipboard(self, parent)
        self.setText("Copy Done :)")
        self.setStyleSheet("""
            border: 2px solid #E74C3C;
            background-color: #ECF0F1;
            color: #000000;
        """)

        QTimer.singleShot(2000, self.restore_original_text)

    def restore_original_text(self):
        self.setText(self.original_text)
        self.setStyleSheet("""
            border: 2px solid #2E86C1;
            border-radius: 10px;
            padding: 10px;
            background-color: #F2F3F4;
            font-size: 16px;
            color: #000000;
        """)


def create_result_label(parent):
    label = ClickableLabel("Result Area - Click to Copy",parent)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("""
        border: 2px solid #2E86C1;
        border-radius: 10px;
        padding: 10px;
        background-color: #F2F3F4;
        font-size: 16px;
        color: #000000;
    """)
    label.setWordWrap(True)

    label.setMaximumWidth(450)
    label.setMinimumHeight(50)
    label.setMaximumHeight(50)
    return label