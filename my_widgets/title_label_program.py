from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from helper.path_helper import resource_path


def title_program(image_path, width=300, height=100):  # اضافه کردن پارامترهای width و height
    title_label = QLabel()
    pixmap = QPixmap(resource_path(image_path))

    if not pixmap.isNull():
        # مقیاس بندی تصویر به اندازه مشخص
        scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        title_label.setPixmap(scaled_pixmap)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    else:
        title_label.setText("Not Find")
        title_label.setStyleSheet("color: red; font-size: 16px;")

    return title_label
