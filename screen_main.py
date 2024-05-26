from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backroundWin import BaseWindow

class ScreenMain(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Ready for your next Therapy?\nBook your Appointment here!")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        layout.addWidget(subtitle, alignment=Qt.AlignTop | Qt.AlignCenter)

        pick_therapist_btn = QPushButton("Pick a Therapist")
        pick_therapist_btn.setStyleSheet("""
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

        your_progress_btn = QPushButton("Your Progress")
        your_progress_btn.setStyleSheet("""
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

        layout.addStretch()
        layout.addWidget(subtitle)
        layout.addStretch()
        layout.addWidget(pick_therapist_btn)
        layout.addWidget(your_progress_btn)
        layout.addStretch()

        self.addContent(layout)

        # Connect buttons to methods for opening other screens
        # pick_therapist_btn.clicked.connect(self.open_pick_therapist)
        # your_progress_btn.clicked.connect(self.open_progress)

    # def open_pick_therapist(self):
    #     from screen_therapist import ScreenTherapist
    #     self.screen_therapist = ScreenTherapist()
    #     self.screen_therapist.show()
    #     self.close()

    # def open_progress(self):
    #     from screen_progress import ScreenProgress
    #     self.screen_progress = ScreenProgress()
    #     self.screen_progress.show()
    #     self.close()

if __name__ == "__main__":
    app = QApplication([])
    main_screen = ScreenMain()
    main_screen.show()
    app.exec_()
