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
        subtitle.setFont(QFont('Arial', 20, QFont.Bold))
        subtitle.setStyleSheet("color: #FFD700;")  # Gold color for the title
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Spacer to move the instruction label down
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        instruction = QLabel("Please choose an event")
        instruction.setFont(QFont('Arial', 12))
        instruction.setStyleSheet("color: white;")
        layout.addWidget(instruction, alignment=Qt.AlignLeft)

        # Example events with different colors and past dates
        events = [
            {"name": "Event 1", "datetime": QDateTime.fromString("2024-04-01 21:00", "yyyy-MM-dd HH:mm").toString("yyyy-MM-dd HH:mm"), "color": "#FF5733"},
            {"name": "Event 2", "datetime": QDateTime.fromString("2023-07-25 20:30", "yyyy-MM-dd HH:mm").toString("yyyy-MM-dd HH:mm"), "color": "#33FF57"},
            {"name": "Event 3", "datetime": QDateTime.fromString("2024-02-20 22:00", "yyyy-MM-dd HH:mm").toString("yyyy-MM-dd HH:mm"), "color": "#FFC300"},
            {"name": "Event 4", "datetime": QDateTime.fromString("2023-09-15 21:45", "yyyy-MM-dd HH:mm").toString("yyyy-MM-dd HH:mm"), "color": "#3498DB"}
        ]
        
        # Spacer at the top
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        for event in events:
            event_button = QPushButton(f"{event['name']}\n{event['datetime']}")
            event_button.setFont(QFont('Arial', 14))
            event_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {event['color']};
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                    text-align: center;
                    margin: 10px 0;
                }}
                QPushButton:hover {{
                    background-color: {self.adjust_color(event['color'], 20)};
                }}
                QPushButton:pressed {{
                    background-color: {self.adjust_color(event['color'], -20)};
                }}
            """)
            event_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            event_button.clicked.connect(lambda _, e=event: self.open_rating_window(e))
            layout.addWidget(event_button)
            
            # Add space between events
            layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Spacer at the bottom
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.addContent(layout)
    
    def open_rating_window(self, event):
        self.rating_window = RatingWindow(event)
        self.rating_window.show()
        self.close()

    def adjust_color(self, color, amount):
        color = color.lstrip('#')
        lv = len(color)
        rgb = tuple(int(color[i:i+lv//3], 16) for i in range(0, lv, lv//3))
        return '#{:02x}{:02x}{:02x}'.format(
            max(0, min(255, rgb[0] + amount)),
            max(0, min(255, rgb[1] + amount)),
            max(0, min(255, rgb[2] + amount))
        )


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
        
        event_label = QLabel(self.event['name'])
        event_label.setAlignment(Qt.AlignCenter)
        event_label.setFont(QFont('Arial', 18))
        event_label.setStyleSheet(f"""
            QLabel {{
                background-color: {self.event['color']};
                color: white;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }}
        """)
        layout.addWidget(event_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Add spacer to push stars lower
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add label above stars
        enjoy_label = QLabel("Did you enjoy this event?")
        enjoy_label.setAlignment(Qt.AlignCenter)
        enjoy_label.setFont(QFont('Arial', 16))
        enjoy_label.setStyleSheet("color: white;")
        layout.addWidget(enjoy_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Add larger spacer to push stars lower
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        stars_layout = QHBoxLayout()
        self.stars = []
        self.rating = 0  # Initialize rating to 0
        for i in range(5):
            star_button = QPushButton()
            star_button.setIcon(QIcon("images/star_empty.png"))
            star_button.setIconSize(QSize(24, 24))
            star_button.setStyleSheet("background-color: transparent; border: none;")
            star_button.setProperty('rating', i + 1)
            star_button.clicked.connect(lambda _, s=star_button: self.toggle_star(s))
            self.stars.append(star_button)
            stars_layout.addWidget(star_button)
        layout.addLayout(stars_layout)

        # Add larger spacer to push comments field much lower
        layout.addSpacerItem(QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.feedback_area = QTextEdit()
        self.feedback_area.setPlaceholderText("Add comments (optional)")
        self.feedback_area.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #5C6BC0;")
        layout.addWidget(self.feedback_area)
        
        # Add spacer to push submit button lower
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

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
        layout.addStretch()  # Add another stretch to ensure it reaches near the bottom
        
        self.addContent(layout)

    def toggle_star(self, star_button):
        rating = star_button.property('rating')
        if self.rating == rating:  # If the same star is clicked, reset to 0
            self.rating = 0
        else:
            self.rating = rating
        for i, btn in enumerate(self.stars):
            if i < self.rating:
                btn.setIcon(QIcon("images/star_filled.png"))
            else:
                btn.setIcon(QIcon("images/star_empty.png"))

    def submit_rating(self):
        message_box = QMessageBox()
        message_box.setStyleSheet("QMessageBox { background-color: lightgrey; }")

        if self.rating == 0:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Please put a rating to proceed.")
            message_box.setWindowTitle("Input Error")
            message_box.exec_()
        else:
            message_box.setIcon(QMessageBox.Information)
            message_box.setText("You have successfully rated this event.")
            message_box.setWindowTitle("Rating Submitted")
            message_box.exec_()
            self.go_back_to_event_list()
            
    def go_back_to_event_list(self):
        self.event_list_window = EventListWindow()
        self.event_list_window.show()
        self.close()
       




if __name__ == "__main__":
    app = QApplication([])
    window = EventListWindow()
    window.show()
    app.exec_()
