from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel


def result_frame_q_frame():
    result_frame = QFrame()
    result_frame.setFrameStyle(QFrame.Shape.NoFrame)
    result_frame.setStyleSheet("""
                QFrame {
                    border: 2px solid #2E86C1;
                    border-radius: 10px;
                    padding: 10px;
                    background-color: #F2F3F4;
                }
            """)

    return result_frame