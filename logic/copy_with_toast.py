from PyQt6 import QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel


def copy_to_clipboard(text_wannt_copy, parent_window):
    clipboard = QApplication.clipboard()
    clipboard.setText(text_wannt_copy.text())

    show_toast("Copied!", parent_window)


global_toast = None


def show_toast(message, parent_window):
    global global_toast

    toast = QLabel(message, parent_window)
    toast.setStyleSheet("""
        background-color: #2E86C1;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    """)
    toast.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    parent_geometry = parent_window.geometry()
    x = (parent_geometry.width() - toast.width()) // 2 + parent_geometry.x()
    y = (parent_geometry.height() - toast.height()) // 2 + parent_geometry.y()
    toast.move(x, y)

    toast.show()

    global_toast = toast

    QTimer.singleShot(2000, lambda: close_toast(toast))


def close_toast(toast):
    global global_toast
    if toast == global_toast:
        toast.close()
        global_toast = None
