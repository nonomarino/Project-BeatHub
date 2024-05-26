from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

class BeatHubApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BeatHub")
        self.setGeometry(100, 100, 400, 600)
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_download_finished)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("Discover upcoming events and artists")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px;")
        layout.addWidget(title)

        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        event_urls = [
            "https://www.patrasevents.gr/imgsrv/f/full/3870693.jpg",
            "https://www.patrasevents.gr/imgsrv/f/full/3876181.jpg",
            "https://www.patrasevents.gr/imgsrv/f/full/3875045.jpg"
        ]

        for url in event_urls:
            request = QNetworkRequest(QUrl(url))
            self.network_manager.get(request)

        self.scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)

    def on_download_finished(self, reply):
        url = reply.url().toString()
        img_data = reply.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)
        
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.mousePressEvent = lambda event, u=url: self.show_event_details(u)
        self.scroll_layout.addWidget(image_label)
        self.scroll_layout.addSpacing(20)

    def show_event_details(self, url):
        print(f"Details for event with image URL: {url}")

if __name__ == "__main__":
    app = QApplication([])
    window = BeatHubApp()
    window.show()
    app.exec_()
