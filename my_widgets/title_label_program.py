from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from helper.path_helper import resource_path


def title_program(image_path):
    title_label = QLabel()
    pixmap = QPixmap(resource_path(image_path))
    if not pixmap.isNull():
        title_label.setPixmap(pixmap)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    else:
        title_label.setText("Not Find")
        title_label.setStyleSheet("color: red; font-size: 16px;")
    return title_label
