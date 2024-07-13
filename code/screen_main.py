from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QApplication, QMessageBox, QWidget, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow  # Import the BaseWindow class from the second code
from rate import EventListWindow  # Import the EventListWindow class
from discover import DiscoverWindow # Import the DiscoverWindow class

class ScreenMain(BaseWindow):  # Extend BaseWindow
    def __init__(self, username="User"):
        super().__init__()
        self.setWindowTitle("Screen Main")
        self.username = username
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        welcome_label = QLabel(f"Welcome back {self.username}")
        welcome_label.setFont(QFont('Arial', 18, QFont.Bold))
        welcome_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(welcome_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        self.addContent(layout)

        pick_Reservations_btn = QPushButton("Reservations")
        pick_Reservations_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 20px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        pick_Reservations_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        your_Rate_btn = QPushButton("Rate")
        your_Rate_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 20px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        your_Rate_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        your_Rate_btn.clicked.connect(self.open_event_list)

        discover_events_btn = QPushButton("Discover Upcoming Events")
        discover_events_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 20px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        discover_events_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        discover_events_btn.clicked.connect(self.open_discover_window)

        technical_support_btn = QPushButton("Technical Support")
        technical_support_btn.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 18px;
                padding: 20px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        technical_support_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        technical_support_btn.clicked.connect(self.show_technical_support)

        layout.addStretch()
        layout.addWidget(pick_Reservations_btn)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Space between buttons
        layout.addWidget(your_Rate_btn)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Space between buttons
        layout.addWidget(discover_events_btn)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Space between buttons
        layout.addWidget(technical_support_btn)
        layout.addStretch()

        self.addContent(layout)

    def show_upcoming_events(self):
        QMessageBox.information(self, "Upcoming Events", "Here are the upcoming events...")

    
    def show_technical_support(self):
        QMessageBox.information(self, "Technical Support", "For technical support, please contact support@example.com")


    def open_event_list(self):
        self.event_list_window = EventListWindow()
        self.event_list_window.show()
        self.close()

    def open_discover_window(self):
        self.discover_window = DiscoverWindow()
        self.discover_window.show()
        self.close()  

if __name__ == "__main__":
    app = QApplication([])
    main_screen = ScreenMain()
    main_screen.show()
    app.exec_()
