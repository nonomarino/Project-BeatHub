from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QLineEdit, QFormLayout, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow

class ChangePass(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Αλλαγή Κωδικού και Username")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Change your password and username")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        form_layout = QFormLayout()

        self.current_password = QLineEdit()
        self.current_password.setEchoMode(QLineEdit.Password)
        self.current_password.setStyleSheet("background-color: white; font-size: 18px;")
        self.new_password = QLineEdit()
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setStyleSheet("background-color: white; font-size: 18px;")
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setStyleSheet("background-color: white; font-size: 18px;")
        self.username = QLineEdit()
        self.username.setStyleSheet("background-color: white; font-size: 18px;")

        form_layout.addRow("Current Password:", self.current_password)
        form_layout.addRow("New Password:", self.new_password)
        form_layout.addRow("Confirm New Password:", self.confirm_password)
        form_layout.addRow("New Username:", self.username)

        layout.addLayout(form_layout)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        submit_button.clicked.connect(self.change_credentials)
        layout.addWidget(submit_button)

        self.addContent(layout)

    def change_credentials(self):
        current_password = self.current_password.text()
        new_password = self.new_password.text()
        confirm_password = self.confirm_password.text()
        username = self.username.text()

        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "New passwords do not match.")
            return

        # Here you should add the logic for checking the current password and changing the username and password.
        # For now, let's assume the change was successful.

        QMessageBox.information(self, "Success", "Credentials updated successfully.")
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = ChangePass()
    window.show()
    app.exec_()
