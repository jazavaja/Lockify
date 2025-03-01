from PyQt6.QtWidgets import QLabel


def wallet_label():
    wallet_address = QLabel("TEDCd37BMNZAgvoc5tZTufFAWQ42UHU7Te")
    wallet_address.setStyleSheet("""
                font-size: 12px;
                color: #2E86C1;
                padding: 0px;
                margin: 0px;
            """)
    return wallet_address