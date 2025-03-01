from PyQt6.QtWidgets import QLabel


def donate_text_widget():
    # متن Donate
    donate_label = QLabel("Support us by donating USDT(trx): ")
    donate_label.setStyleSheet("""
                font-size: 12px;
                color: #5D6D7E;
                padding: 0px;
                margin: 0px;
            """)
    return donate_label