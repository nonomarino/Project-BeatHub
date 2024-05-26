from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QApplication, QWidget, QFormLayout, QMessageBox, QLineEdit, QMainWindow, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 800)
        self.setWindowTitle("BeatHub")
        self.setWindowIcon(QIcon("images/Screenshot 2024-05-25 181127.png"))
        self.initUI()

    def initUI(self):
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add blue header image at the top
        self.add_top_image()

    def add_top_image(self):
        header_label = QLabel(self)
        pixmap = QPixmap('images/Screenshot 2024-05-25 181127.png')  # Add the correct path to your image
        # Scale the pixmap to fit the width of the window
        header_label.setPixmap(pixmap.scaled(self.width(), 150, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        header_label.setAlignment(Qt.AlignTop)
        header_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header_label.setFixedHeight(150)

        self.main_layout.addWidget(header_label, alignment=Qt.AlignTop)

    def addContent(self, layout):
        self.main_layout.addLayout(layout)

class ProfileWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Αλλαγή Κωδικού και Username")
        
        self.layout = QFormLayout()
        
        self.current_password = QLineEdit()
        self.current_password.setEchoMode(QLineEdit.Password)
        self.new_password = QLineEdit()
        self.new_password.setEchoMode(QLineEdit.Password)
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.username = QLineEdit()
        
        self.layout.addRow("Τρέχον Κωδικός:", self.current_password)
        self.layout.addRow("Νέος Κωδικός:", self.new_password)
        self.layout.addRow("Επιβεβαίωση Νέου Κωδικού:", self.confirm_password)
        self.layout.addRow("Νέο Username:", self.username)
        
        self.submit_button = QPushButton("Υποβολή")
        self.submit_button.clicked.connect(self.change_credentials)
        self.layout.addWidget(self.submit_button)
        
        self.addContent(self.layout)
    
    def change_credentials(self):
        current_password = self.current_password.text()
        new_password = self.new_password.text()
        confirm_password = self.confirm_password.text()
        username = self.username.text()
        
        if new_password != confirm_password:
            QMessageBox.warning(self, "Σφάλμα", "Οι νέοι κωδικοί δεν ταιριάζουν.")
            return
        
        # Εδώ θα πρέπει να γίνει ο έλεγχος του τρέχοντος κωδικού και η αλλαγή του username και κωδικού.
        # Προσωρινά, ας υποθέσουμε ότι ο έλεγχος και η αλλαγή ήταν επιτυχής.
        
        QMessageBox.information(self, "Επιτυχία", "Τα στοιχεία ενημερώθηκαν επιτυχώς.")
        self.accept()

class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Στοιχεία Επικοινωνίας")
        
        layout = QVBoxLayout()
        
        title_label = QLabel("Στοιχεία Επικοινωνίας")
        layout.addWidget(title_label)
        
        self.name_label = QLabel("Ονοματεπώνυμο: John Doe")
        self.phone_label = QLabel("Τηλέφωνο: 123-456-7890")
        self.email_label = QLabel("Email: john.doe@example.com")
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.email_label)
        
        self.change_credentials_button = QPushButton("Αλλαγή Κωδικού και Username")
        self.change_credentials_button.clicked.connect(self.open_change_credentials_dialog)
        layout.addWidget(self.change_credentials_button)
        
        self.music_preferences_button = QPushButton("Μουσικές Προτιμήσεις")
        self.music_preferences_button.clicked.connect(self.show_music_preferences)
        layout.addWidget(self.music_preferences_button)
        
        self.favorite_events_button = QPushButton("Αγαπημένα Events και Καλλιτέχνες")
        self.favorite_events_button.clicked.connect(self.show_favorite_events)
        layout.addWidget(self.favorite_events_button)
        
        self.booking_history_button = QPushButton("Ιστορικό Κρατήσεων")
        self.booking_history_button.clicked.connect(self.show_booking_history)
        layout.addWidget(self.booking_history_button)
        
        self.rating_history_button = QPushButton("Ιστορικό Αξιολογήσεων")
        self.rating_history_button.clicked.connect(self.show_rating_history)
        layout.addWidget(self.rating_history_button)
        
        self.addContent(layout)
    
    def open_change_credentials_dialog(self):
        self.dialog = ProfileWindow()  # Changed to use ProfileWindow
        self.dialog.show()  # Use show() instead of exec_()
    
    def show_music_preferences(self):
        QMessageBox.information(self, "Μουσικές Προτιμήσεις", "Οι μουσικές προτιμήσεις σας είναι...")

    def show_favorite_events(self):
        QMessageBox.information(self, "Αγαπημένα Events και Καλλιτέχνες", "Τα αγαπημένα σας events και καλλιτέχνες είναι...")

    def show_booking_history(self):
        QMessageBox.information(self, "Ιστορικό Κρατήσεων", "Το ιστορικό κρατήσεών σας είναι...")

    def show_rating_history(self):
        QMessageBox.information(self, "Ιστορικό Αξιολογήσεων", "Το ιστορικό αξιολογήσεών σας είναι...")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
