from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QMessageBox

def about_us_btn_click():
    about_us = QPushButton('About project')

    def show_about_dialog():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("About Lockify")
        msg_box.setTextFormat(Qt.TextFormat.RichText) 

        msg_box.setText("""
            <div style='text-align: justify; font-size: 12px; line-height: 1.5;'>
                <h3 style='text-align: center;'>Welcome to Lockify!</h3>
                <p>This application is designed with the goal of helping individuals and organizations protect their sensitive information using advanced encryption techniques. Here are some key features of this tool:</p>
                <ul>
                    <li><b>Fully Offline:</b> This application operates entirely offline. No data is stored, transmitted, or shared with any external servers.</li>
                    <li><b>Open Source:</b> The source code is publicly available on GitHub for transparency and community contributions. You can review it at: 
                        <a href='https://github.com/jazavaja/Lockify'>GitHub Repository</a>.</li>
                    <li><b>Privacy-Focused:</b> Your data remains completely private and secure. We do not collect, store, or transmit any information.</li>
                    <li><b>Community Contribution:</b> Our mission is to contribute to the global community by promoting secure data protection practices.</li>
                </ul>
                <p><b>Developed by:</b> Javad Sarlak<br>
                <b>Version:</b> 1.0</p>
                <p style='text-align: center;'>Thank you for choosing Lockify. Together, we can make the digital world a safer place!</p>
            </div>
            """)

        msg_box.exec()

    about_us.clicked.connect(show_about_dialog)

    return about_us
