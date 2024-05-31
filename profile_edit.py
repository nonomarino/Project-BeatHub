from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QApplication, QWidget, QFormLayout, QMessageBox, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow  # Import the BaseWindow class

class ProfileWindow(BaseWindow):  # Extend BaseWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Profile")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()
    
    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        subtitle = QLabel("Edit Profile")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter new username")
        self.username_input.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #5C6BC0;")
        form_layout.addRow(QLabel("Username:"), self.username_input)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter new password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #5C6BC0;")
        form_layout.addRow(QLabel("Password:"), self.password_input)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter new email")
        self.email_input.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #5C6BC0;")
        form_layout.addRow(QLabel("Email:"), self.email_input)
        
        layout.addLayout(form_layout)
        
        save_button = QPushButton("Save Changes")
        save_button.setStyleSheet("""
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
        save_button.clicked.connect(self.save_changes)
        
        layout.addWidget(save_button)
        layout.addStretch()
        
        self.addContent(layout)
    
    def save_changes(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        
        # Here you would add the logic to save the changes, for now we show a message box
        QMessageBox.information(self, "Save Changes", f"Username: {username}\nPassword: {password}\nEmail: {email}")

if __name__ == "__main__":
    app = QApplication([])
    window = ProfileWindow()
    window.show()
    app.exec_()
