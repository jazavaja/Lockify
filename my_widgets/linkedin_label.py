from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QLabel, QPushButton


def linkedin_button_widget():
    # Create a button
    github_button = QPushButton("Linkedin")

    # Connect the button to open the GitHub link
    github_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.linkedin.com/in/javadsarlak/")))

    return github_button