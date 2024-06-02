import json
import sys
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget, QScrollArea, QHBoxLayout, QComboBox, QSizePolicy, QPushButton)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from backroundWin import BaseWindow  # Import the BaseWindow class

class DiscoverWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discover Events")
        self.setStyleSheet("background-color: #363636; color: white;")
        self.add_content_to_main_layout()
        self.load_events()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        title_label = QLabel("Discover Events")
        title_label.setFont(QFont('Arial', 18, QFont.Bold))
        title_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(title_label, alignment=Qt.AlignCenter)

        filter_layout = QHBoxLayout()
        filter_layout.setAlignment(Qt.AlignCenter)

        # ComboBox for genre selection
        self.genre_combo = QComboBox()
        self.genre_combo.setFont(QFont('Arial', 14))
        self.genre_combo.setStyleSheet("color: black; background-color: #f5f5dc; padding: 10px; border-radius: 5px;")
        filter_layout.addWidget(self.genre_combo)

        # Search button
        search_button = QPushButton("Search")
        search_button.setFont(QFont('Arial', 14))
        search_button.setStyleSheet("""
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
        search_button.clicked.connect(self.search_events)
        filter_layout.addWidget(search_button)

        layout.addLayout(filter_layout)

        # Scroll area to display events
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 10px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            QScrollBar:horizontal {
                background: transparent;
                height: 10px;
            }
            QScrollBar::handle:horizontal {
                background: #888;
                min-width: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;
            }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)
        layout.addWidget(self.scroll_area)

        self.addContent(layout)

    def load_events(self):
        with open('events.json', 'r') as f:
            self.events = json.load(f)

        genres = set()
        for event in self.events:
            genres.update(event['genres'])
        self.genre_combo.addItems(sorted(genres))

        self.display_events(self.events)

    def display_events(self, events):
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        for event in events:
            event_box = self.create_event_box(event)
            scroll_layout.addWidget(event_box)

        scroll_content.setLayout(scroll_layout)
        self.scroll_area.setWidget(scroll_content)

    def search_events(self):
        selected_genre = self.genre_combo.currentText()
        filtered_events = [event for event in self.events if selected_genre in event['genres']]
        self.display_events(filtered_events)

    def create_event_box(self, event):
        event_box = QWidget()
        event_layout = QVBoxLayout(event_box)

        # Set the background image directly from the file path provided in the JSON
        image_path = event['background_photo']
        pixmap = QPixmap(image_path)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(300, 150)  # Adjust size as needed

        title = QLabel(event['title'])
        title.setFont(QFont('Arial', 14, QFont.Bold))
        title.setStyleSheet("color: white; padding: 5px;")

        date_location = QLabel(f"{event['date']}, {event['location']}")
        date_location.setFont(QFont('Arial', 12))
        date_location.setStyleSheet("color: white; padding: 5px;")

        event_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        event_layout.addWidget(title, alignment=Qt.AlignCenter)
        event_layout.addWidget(date_location, alignment=Qt.AlignCenter)

        event_box.setLayout(event_layout)
        event_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        return event_box


if __name__ == "__main__":
    app = QApplication([])
    window = DiscoverWindow()
    window.show()
    sys.exit(app.exec_())
