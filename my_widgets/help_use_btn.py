from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QMessageBox

def help_use_button_widget():
    about_us = QPushButton('Help Use')

    def show_about_dialog():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Help to Use Lockify")
        msg_box.setTextFormat(Qt.TextFormat.RichText)

        msg_box.setText("""
                    <div style='text-align: justify; font-size: 12px; line-height: 1.5;'>
                        <h3 style='text-align: center;'>Welcome to Lockify!</h3>
                        <p>This simple yet powerful application is designed to help you protect your sensitive data using encryption. Here’s how to get started:</p>
                        <ol>
                            <li><b>Encrypting Your Text:</b>  
                                <ul>
                                    <li>Enter the text you want to encrypt in the **Input 1** field.</li>
                                    <li>Set your own password in the **Input 2** field—this will act as your encryption key.</li>
                                    <li>Click the **Encrypt** button, and your text will be transformed into an encrypted string.</li>
                                </ul>
                            </li>
                            <li><b>Decrypting Your Text:</b>  
                                <ul>
                                    <li>To decrypt your text, paste the encrypted string into **Input 1**.</li>
                                    <li>Enter the **same password** used for encryption in **Input 2**.</li>
                                    <li>Click **Decrypt** to retrieve your original message.</li>
                                </ul>
                            </li>
                            <li><b>Important Notes:</b>  
                                <ul>
                                    <li>Your data is processed entirely offline and is not shared with external servers.</li>
                                    <li>Lockify uses a strong encryption algorithm to ensure the safety of your data.</li>
                                    <li>Always remember your password, as it’s the only way to decrypt your information.</li>
                                </ul>
                            </li>
                            <li><b>Open Source:</b> You can review the source code on GitHub for transparency and contributions. Check it out at: 
                                <a href='https://github.com/jazavaja/Lockify'>GitHub Repository</a>.</li>
                            <li><b>Security Focused:</b> Lockify is built with privacy in mind. We never store or transmit your data.</li>
                        </ol>
                        <p><b>Developed by:</b> Javad Sarlak<br>
                        <b>Version:</b> 1.0</p>
                        <p style='text-align: center;'>Thank you for choosing Lockify to protect your sensitive information. Let's make your digital world safer together!</p>
                    </div>
                    """)

        msg_box.exec()

    about_us.clicked.connect(show_about_dialog)

    return about_us
