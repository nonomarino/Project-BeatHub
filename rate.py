from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QApplication, QWidget, QTextEdit, QHBoxLayout, QMessageBox, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5.QtGui import QFont, QIcon
from backroundWin import BaseWindow  # Import the BaseWindow class

class EventListWindow(BaseWindow):  # Extend BaseWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Event List")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        
        subtitle = QLabel("Events Attended")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Example events
        events = [
            {"name": "Event 1", "datetime": QDateTime.currentDateTime().toString()},
            {"name": "Event 2", "datetime": QDateTime.currentDateTime().addDays(-1).toString()},
            {"name": "Event 3", "datetime": QDateTime.currentDateTime().addDays(-2).toString()},
            {"name": "Event 4", "datetime": QDateTime.currentDateTime().addDays(-3).toString()}
        ]
        
        for event in events:
            event_button = QPushButton(f"{event['name']}\n{event['datetime']}")
            event_button.setFont(QFont('Arial', 14))
            event_button.setStyleSheet("""
                QPushButton {
                    background-color: #5C6BC0;
                    color: white;
                    padding: 20px;
                    border-radius: 20px;
                    text-align: center;
                }
                QPushButton:hover {
                    background-color: #7986CB;
                }
                QPushButton:pressed {
                    background-color: #3F51B5;
                }
            """)
            event_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            event_button.clicked.connect(lambda _, e=event: self.open_rating_window(e))
            layout.addWidget(event_button)
        
        layout.addStretch()
        
        self.addContent(layout)
    
    def open_rating_window(self, event):
        self.rating_window = RatingWindow(event)
        self.rating_window.show()
        self.close()


class RatingWindow(BaseWindow):  # Extend BaseWindow
    def __init__(self, event):
        super().__init__()
        self.event = event
        self.setWindowTitle("Rate Event")
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        subtitle = QLabel(self.event['name'])
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        stars_layout = QHBoxLayout()
        self.stars = []
        for i in range(5):
            star_button = QPushButton()
            star_button.setIcon(QIcon("images/Screenshot 2024-05-31 231749.png"))
            star_button.setIconSize(QSize(24, 24))
            star_button.setStyleSheet("background-color: transparent; border: none;")
            star_button.setProperty('rating', i + 1)
            star_button.clicked.connect(lambda _, s=star_button: self.rate_event(s))
            self.stars.append(star_button)
            stars_layout.addWidget(star_button)
        layout.addLayout(stars_layout)

        self.feedback_area = QTextEdit()
        self.feedback_area.setPlaceholderText("Add comments (optional)")
        self.feedback_area.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #5C6BC0;")
        layout.addWidget(self.feedback_area)
        
        rate_button = QPushButton("Submit Rating")
        rate_button.setStyleSheet("""
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
        rate_button.clicked.connect(self.submit_rating)
        
        layout.addWidget(rate_button)
        layout.addStretch()
        
        self.addContent(layout)
    
    def rate_event(self, star_button):
        rating = star_button.property('rating')
        for i, btn in enumerate(self.stars):
            if i < rating:
                btn.setIcon(QIcon("images/Screenshot 2024-05-31 232041.png"))
            else:
                btn.setIcon(QIcon("images/Screenshot 2024-05-31 231749.png"))
        self.rating = rating

    def submit_rating(self):
        feedback = self.feedback_area.toPlainText()
        QMessageBox.information(self, "Rating Submitted", f"Event: {self.event['name']}\nRating: {self.rating} stars\nFeedback: {feedback}")

if __name__ == "__main__":
    app = QApplication([])
    window = EventListWindow()
    window.show()
    app.exec_()
