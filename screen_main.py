from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QApplication, QMessageBox, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow  # Import the BaseWindow class from the second code

class ScreenMain(BaseWindow):  # Use BaseWindow as the base class
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Welcome, (Username)")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

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
        discover_events_btn.clicked.connect(self.show_upcoming_events)
        
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
        technical_support_btn.clicked.connect(self.show_technical_support)

        layout.addStretch()
        layout.addWidget(subtitle)
        layout.addStretch()
        layout.addWidget(pick_Reservations_btn)
        layout.addWidget(your_Rate_btn)
        layout.addWidget(discover_events_btn)
        layout.addWidget(technical_support_btn)
        
        layout.addStretch()

        self.addContent(layout)

    def show_upcoming_events(self):
        QMessageBox.information(self, "Upcoming Events", "Here are the upcoming events...")

    def show_technical_support(self):
        QMessageBox.information(self, "Technical Support", "For technical support, please contact support@example.com")

if __name__ == "__main__":
    app = QApplication([])
    main_screen = ScreenMain()
    main_screen.show()
    app.exec_()
