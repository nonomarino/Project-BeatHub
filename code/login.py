import sys
from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QLineEdit, QApplication, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow  # Import the BaseWindow class
from screen_main import ScreenMain  # Import the ScreenMain class

class LoginWindow(BaseWindow):  # Extend BaseWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Add spacer
        layout.addStretch()

        # Add username field
        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("username")
        self.username_field.setFont(QFont('Arial', 14))
        self.username_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        self.username_field.setFixedHeight(40)
        self.username_field.setFixedWidth(300)
        layout.addWidget(self.username_field, alignment=Qt.AlignCenter)

        # Add space between fields
        layout.addSpacing(20)

        # Add password field
        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("password")
        self.password_field.setFont(QFont('Arial', 14))
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        self.password_field.setFixedHeight(40)
        self.password_field.setFixedWidth(300)
        layout.addWidget(self.password_field, alignment=Qt.AlignCenter)

        # Add space between fields and login button
        layout.addSpacing(20)

        # Add horizontal layout for login button and sign up link
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        # Add login button
        login_button = QPushButton("log in")
        login_button.setFont(QFont('Arial', 14))
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        login_button.clicked.connect(self.open_screen_main)  # Connect the button click event to the method
        button_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # Add horizontal spacer between button and label
        button_layout.addSpacing(20)

        # Add sign up link
        signup_link = QLabel("Don't have an account?")
        signup_link.setFont(QFont('Arial', 10))
        signup_link.setStyleSheet("color: #9c27b0;")  # Purple color
        button_layout.addWidget(signup_link, alignment=Qt.AlignLeft)

        layout.addLayout(button_layout)

        # Add spacer
        layout.addStretch()

        self.addContent(layout)

    def open_screen_main(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both username and password are required.")
        else:
            self.screen_main = ScreenMain(username)
            self.screen_main.show()
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
