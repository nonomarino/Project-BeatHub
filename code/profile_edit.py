from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QLineEdit, QApplication, QMainWindow, QWidget, QMessageBox, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow  # Import the BaseWindow class

class ProfileEdit(BaseWindow):  # Extend BaseWindow
    def __init__(self, username="User"):
        super().__init__()
        self.setWindowTitle("Profile Edit")
        self.username = username
        self.email = "mail@example.com"  # Example email
        self.password = "password123"  # Example password
        self.setStyleSheet("background-color: #363636; color: white;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        welcome_label = QLabel(f"Welcome, {self.username}")
        welcome_label.setFont(QFont('Arial', 18, QFont.Bold))
        welcome_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(welcome_label, alignment=Qt.AlignCenter)

        self.contact_btn = QPushButton("Στοιχεια επικοινωνιας")
        self.contact_btn.setFont(QFont('Arial', 14))
        self.contact_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.contact_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.contact_btn.clicked.connect(self.show_contact_details)
        layout.addWidget(self.contact_btn)

        self.preferences_btn = QPushButton("Προτιμήσεις-φίλτρα")
        self.preferences_btn.setFont(QFont('Arial', 14))
        self.preferences_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.preferences_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.preferences_btn.clicked.connect(self.show_preferences_filters)
        layout.addWidget(self.preferences_btn)

        self.favorites_btn = QPushButton("Λιστα αγαπημενων")
        self.favorites_btn.setFont(QFont('Arial', 14))
        self.favorites_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.favorites_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.favorites_btn)

        self.rating_history_btn = QPushButton("Ιστορικό αξιολογήσεων")
        self.rating_history_btn.setFont(QFont('Arial', 14))
        self.rating_history_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.rating_history_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.rating_history_btn)

        layout.addStretch()

        self.addContent(layout)

    def show_contact_details(self):
        self.contact_details_window = ContactDetailsWindow(self.username, self.email, self.password)
        self.contact_details_window.show()

    def show_preferences_filters(self):
        self.preferences_filters_window = PreferencesFiltersWindow()
        self.preferences_filters_window.show()



class ContactDetailsWindow(BaseWindow):
    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password
        self.setStyleSheet("background-color: #363636; color: white;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        contact_label = QLabel("Στοιχεια επικοινωνιας")
        contact_label.setFont(QFont('Arial', 18, QFont.Bold))
        contact_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(contact_label, alignment=Qt.AlignCenter)

        self.username_field = QLineEdit(self.username)
        self.username_field.setFont(QFont('Arial', 14))
        self.username_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        self.username_field.setReadOnly(True)
        layout.addWidget(self.username_field)

        self.email_field = QLineEdit(self.email)
        self.email_field.setFont(QFont('Arial', 14))
        self.email_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        self.email_field.setReadOnly(True)
        layout.addWidget(self.email_field)

        self.password_field = QLineEdit(self.password)
        self.password_field.setFont(QFont('Arial', 14))
        self.password_field.setEchoMode(QLineEdit.Normal)
        self.password_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        self.password_field.setReadOnly(True)
        layout.addWidget(self.password_field)

        self.edit_btn = QPushButton("Edit")
        self.edit_btn.setFont(QFont('Arial', 14))
        self.edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.edit_btn.clicked.connect(self.open_edit_contact_details_window)
        layout.addWidget(self.edit_btn)

        layout.addStretch()

        self.addContent(layout)

    def open_edit_contact_details_window(self):
        self.edit_contact_details_window = EditContactDetailsWindow(self.username, self.email, self.password)
        self.edit_contact_details_window.show()
        self.close()

class EditContactDetailsWindow(BaseWindow):
    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password
        self.setStyleSheet("background-color: #363636; color: white;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        contact_label = QLabel("Edit Contact Details")
        contact_label.setFont(QFont('Arial', 18, QFont.Bold))
        contact_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(contact_label, alignment=Qt.AlignCenter)

        self.current_password_field = QLineEdit()
        self.current_password_field.setPlaceholderText("Current Password")
        self.current_password_field.setFont(QFont('Arial', 14))
        self.current_password_field.setEchoMode(QLineEdit.Normal)
        self.current_password_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.current_password_field)

        self.new_password_field = QLineEdit()
        self.new_password_field.setPlaceholderText("New Password")
        self.new_password_field.setFont(QFont('Arial', 14))
        self.new_password_field.setEchoMode(QLineEdit.Normal)
        self.new_password_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.new_password_field)

        self.confirm_new_password_field = QLineEdit()
        self.confirm_new_password_field.setPlaceholderText("Confirm New Password")
        self.confirm_new_password_field.setFont(QFont('Arial', 14))
        self.confirm_new_password_field.setEchoMode(QLineEdit.Normal)
        self.confirm_new_password_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.confirm_new_password_field)

        self.new_username_field = QLineEdit()
        self.new_username_field.setPlaceholderText("New Username")
        self.new_username_field.setFont(QFont('Arial', 14))
        self.new_username_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.new_username_field)
        
        
        self.new_email_field = QLineEdit(self.email)
        self.new_email_field.setFont(QFont('Arial', 14))
        self.new_email_field.setPlaceholderText("New Email")
        self.new_email_field.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.new_email_field)

        self.confirm_btn = QPushButton("Confirm Changes")
        self.confirm_btn.setFont(QFont('Arial', 14))
        self.confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        self.confirm_btn.clicked.connect(self.confirm_changes)
        layout.addWidget(self.confirm_btn)

        layout.addStretch()

        self.addContent(layout)

    def confirm_changes(self):
        current_password = self.current_password_field.text()
        new_password = self.new_password_field.text()
        confirm_new_password = self.confirm_new_password_field.text()
        new_username = self.new_username_field.text()
        new_email = self.new_email_field.text()
        self.email = new_email
        # self.email_field.setText(self.email)

        if current_password != self.password:
            QMessageBox.warning(self, "Error", "Current password is incorrect.")
        elif new_password != confirm_new_password:
            QMessageBox.warning(self, "Error", "New password and confirm new password do not match.")
        else:
            self.password = new_password
            self.username = new_username
            QMessageBox.information(self, "Success", "Profile updated successfully.")
            self.close()
            self.contact_details_window = ContactDetailsWindow(self.username, self.email, self.password)
            self.contact_details_window.show()
            
class PreferencesFiltersWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Προτιμήσεις-φίλτρα")
        self.setStyleSheet("background-color: #363636; color: white;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        preferences_label = QLabel("Προτιμήσεις")
        preferences_label.setFont(QFont('Arial', 18, QFont.Bold))
        preferences_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(preferences_label, alignment=Qt.AlignCenter)

        preferences = ["Ζωντανή μουσική", "Εμφανίσεις DJ", "Συναυλία καλλιτέχνη", "Θεματικές βραδιές"]
        for preference in preferences:
            preference_button = QPushButton(preference)
            preference_button.setFont(QFont('Arial', 14))
            preference_button.setStyleSheet("""
                QPushButton {
                    background-color: #5C6BC0;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #7986CB;
                }
                QPushButton:pressed {
                    background-color: #3F51B5;
                }
            """)
            preference_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            layout.addWidget(preference_button)

        select_filter_button = QPushButton("Επιλογή φίλτρου")
        select_filter_button.setFont(QFont('Arial', 14))
        select_filter_button.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        layout.addWidget(select_filter_button, alignment=Qt.AlignCenter)

        layout.addStretch()

        self.addContent(layout)
            
            

if __name__ == "__main__":
    app = QApplication([])
    window = ProfileEdit()
    window.show()
    app.exec_()
