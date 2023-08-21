import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class StylishButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create a regular button
        regular_button = QPushButton("Regular Button")
        layout.addWidget(regular_button)

        # Create a stylish button using a stylesheet
        stylish_button = QPushButton("Stylish Button")
        stylish_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #3498db;"
            "   color: white;"
            "   border: none;"
            "   padding: 10px 20px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #2980b9;"
            "}"
        )
        layout.addWidget(stylish_button)

        self.setLayout(layout)
        self.setWindowTitle("Stylish Button Example")
        self.setGeometry(100, 100, 300, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StylishButtonExample()
    window.show()
    sys.exit(app.exec())
