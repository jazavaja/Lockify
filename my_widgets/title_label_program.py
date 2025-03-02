from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


def title_program(image_path):
    # ایجاد یک QLabel برای نمایش تصویر
    title_label = QLabel()
    pixmap = QPixmap(image_path)  # بارگذاری تصویر از مسیر مشخص
    if not pixmap.isNull():  # بررسی اینکه تصویر بارگذاری شده است
        title_label.setPixmap(pixmap)  # تنظیم تصویر در QLabel
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # مرکز‌چین کردن تصویر
    else:
        title_label.setText("تصویر یافت نشد!")  # پیام خطا در صورت عدم بارگذاری تصویر
        title_label.setStyleSheet("color: red; font-size: 16px;")
    return title_label
