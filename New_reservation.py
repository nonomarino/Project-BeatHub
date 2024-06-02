from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QLineEdit, QDateEdit, QTimeEdit, QMainWindow, QWidget, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QIcon, QPixmap, QFont
from backroundWin import BaseWindow  # Import the BaseWindow class

class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 800)
        self.setWindowTitle("BeatHub")
        self.setWindowIcon(QIcon("images/logo_win.png"))
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
        pixmap = QPixmap('images/patra.jpeg')  # Add the correct path to your image
        # Scale the pixmap to fit the width of the window
        header_label.setPixmap(pixmap.scaled(self.width(), 150, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        header_label.setAlignment(Qt.AlignTop)
        header_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header_label.setFixedHeight(150)

        self.main_layout.addWidget(header_label, alignment=Qt.AlignTop)

    def addContent(self, layout):
        self.main_layout.addLayout(layout)


class SearchWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservation Window")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        title_label = QLabel("Make a Reservation")
        title_label.setFont(QFont('Arial', 18, QFont.Bold))
        title_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(title_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Horizontal layout (QHBoxLayout) for input and date picker
        hbox = QHBoxLayout()

        # Label for the input field
        label = QLabel("Input:")
        label.setStyleSheet("color: white;")  # Set text color for visibility
        hbox.addWidget(label)

        # Input field (QLineEdit)
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("background-color: white; color: black;")  # Set background color to white and text color to black
        hbox.addWidget(self.input_field)

        # Date picker (QDateEdit)
        self.date_picker = QDateEdit()
        self.date_picker.setDate(QDate.currentDate())  # Set current date as default
        self.date_picker.setCalendarPopup(True)  # Enable calendar popup
        self.date_picker.setStyleSheet("color: white;")  # Set text color to white
        hbox.addWidget(self.date_picker)

        # Add the horizontal layout to the vertical layout
        layout.addLayout(hbox)

        # Add the photo (QLabel)
        photo_label = QLabel()
        photo = QPixmap("images/patra.jpeg")  # Replace with your image path
        if not photo.isNull():
            # Scale the photo to a specific size
            scaled_photo = photo.scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            photo_label.setPixmap(scaled_photo)
            scaled_photo = photo.scaled(700, 700, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            photo_label.setPixmap(scaled_photo)
        else:
            photo_label.setText("Image not found")
            photo_label.setStyleSheet("color: white;")  # Set text color for visibility
        layout.addWidget(photo_label, alignment=Qt.AlignCenter)

        # Horizontal layout for time edit and button
        time_button_hbox = QHBoxLayout()

        # Time edit (QTimeEdit)
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())  # Set current time as default
        self.time_edit.setStyleSheet("color: white;")  # Set text color to white
        time_button_hbox.addWidget(self.time_edit)

        # Button (QPushButton)
        self.button = QPushButton("Submit")  # Customize button text
        self.button.setStyleSheet("background-color: #5A9; color: white;")  # Button styling
        self.button.clicked.connect(self.on_submit)  # Connect button click to handler
        time_button_hbox.addWidget(self.button)

        # Add the time edit and button layout to the main layout
        layout.addLayout(time_button_hbox)

        # Add spacer items and stretch for better alignment
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Space between items
        layout.addStretch()

        # Add the main layout to the base window's main layout
        self.addContent(layout)

    def on_submit(self):
        input_text = self.input_field.text()
        date = self.date_picker.date().toString()
        time = self.time_edit.time().toString()
        print(f"Input: {input_text}, Date: {date}, Time: {time}")


if __name__ == "__main__":
    app = QApplication([])
    window = SearchWindow()
    window.show()
    app.exec_()
