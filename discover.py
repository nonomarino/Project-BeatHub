import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QCheckBox, QScrollArea, QGridLayout
)
from PyQt5.QtGui import QFont, QPixmap , QDesktopServices
from PyQt5.QtCore import Qt, QUrl

class DiscoverEvents(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Discovery App")
        self.setGeometry(100, 100, 800, 600)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.layout = QVBoxLayout(self.centralwidget)

        self.discover_button = QLabel("Discover upcoming artists and events", self)
        
        self.layout.addWidget(self.discover_button)

        self.use_profile_preferences = QCheckBox("Use existing profile preferences", self)
        self.layout.addWidget(self.use_profile_preferences)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        self.load_resources()
        self.update_resources()

    def load_resources(self):
        with open('resources.json', 'r') as file:
            self.resources = json.load(file)

    def update_resources(self):
        if self.use_profile_preferences.isChecked():
            events = self.get_events_based_on_preferences()
        else:
            events = self.get_sample_events()

        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        row, col = 0, 0
        for event in events:
            event_widget = self.create_event_widget(event)
            self.scroll_layout.addWidget(event_widget, row, col)

            col += 1
            if col > 1:
                col = 0
                row += 1

        self.scroll_layout.setRowStretch(row + 1, 1)

    def create_event_widget(self, event):
        event_widget = QWidget()
        event_layout = QVBoxLayout(event_widget)
        event_layout.setAlignment(Qt.AlignTop)

        img_label = QLabel()
        pixmap = QPixmap(self.get_image_path(event['type']))
        img_label.setPixmap(pixmap)
        img_label.setScaledContents(True)
        img_label.setFixedSize(200, 150)
        img_label.mousePressEvent = lambda event, url=event['link']: self.open_link(url)
        event_layout.addWidget(img_label, alignment=Qt.AlignCenter)

        title_label = QLabel(event['title'])
        title_label.setFont(QFont('Arial', 12, QFont.Bold))
        title_label.setStyleSheet("color: black;")
        title_label.setWordWrap(True)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFixedHeight(150)
        title_label.mousePressEvent = lambda event, url=event['link']: self.open_link(url)
        event_layout.addWidget(title_label)

        return event_widget

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def get_image_path(self, event_type):
        if event_type == "Concert":
            return "images/concert.png"
        elif event_type == "Festival":
            return "images/festival.png"
        elif event_type == "Club":
            return "images/club.png"
        return ""

    def discover_events(self):
        self.update_resources()

    def get_events_based_on_preferences(self):
        # Fetch and return events based on user preferences
        # This is a placeholder for actual implementation
        return [
            {'title': 'Concert A', 'type': 'Concert', 'link': 'http://example.com/a'},
            {'title': 'Festival B', 'type': 'Festival', 'link': 'http://example.com/b'}
        ]

    def get_sample_events(self):
        # Return a sample list of events
        return [
            {'title': 'Sample Concert', 'type': 'Concert', 'link': 'http://example.com/sample1'},
            {'title': 'Sample Festival', 'type': 'Festival', 'link': 'http://example.com/sample2'},
            {'title': 'Sample Club Event', 'type': 'Club', 'link': 'http://example.com/sample3'}
        ]

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = DiscoverEvents()
    window.show()
    sys.exit(app.exec_())
