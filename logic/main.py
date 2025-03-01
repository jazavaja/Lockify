from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel


def process_inputs(input1, input2, result_label):
    result = f"Input 1: {input1}\nInput 2: {input2}"
    result_label.setText(result)

