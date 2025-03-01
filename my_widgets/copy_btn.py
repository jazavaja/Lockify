from PyQt6 import QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel


def copy_btn(widget_wallet_address, parent_window):
    copy_button = QPushButton("📋")
    copy_button.setStyleSheet("""
                font-size: 12px;
                padding: 5px;
                border: none;
                background-color: transparent;
                color: #2E86C1;
            """)
    # استفاده از lambda برای ارسال widget_wallet_address و parent_window به تابع copy_to_clipboard
    copy_button.clicked.connect(lambda: copy_to_clipboard(widget_wallet_address, parent_window))
    return copy_button


def copy_to_clipboard(widget_wallet_address, parent_window):
    # کپی کردن متن آدرس به کلیپ‌بورد
    clipboard = QApplication.clipboard()
    clipboard.setText(widget_wallet_address.text())

    # نمایش پیام "Copied!" در وسط پنجره
    show_toast("Copied!", parent_window)




# متغیر جهانی برای نگهداری مرجع toast
global_toast = None


def show_toast(message, parent_window):
    global global_toast

    # ایجاد یک QLabel برای نمایش پیام
    toast = QLabel(message, parent_window)  # اتصال toast به پنجره اصلی
    toast.setStyleSheet("""
        background-color: #2E86C1;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    """)
    toast.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    # تعیین موقعیت پیام در مرکز پنجره اصلی
    parent_geometry = parent_window.geometry()
    x = (parent_geometry.width() - toast.width()) // 2 + parent_geometry.x()
    y = (parent_geometry.height() - toast.height()) // 2 + parent_geometry.y()
    toast.move(x, y)

    # نمایش پیام
    toast.show()

    # ذخیره مرجع toast در متغیر جهانی
    global_toast = toast

    # پنهان کردن پیام پس از 2 ثانیه
    QTimer.singleShot(2000, lambda: close_toast(toast))


def close_toast(toast):
    global global_toast
    if toast == global_toast:
        toast.close()
        global_toast = None