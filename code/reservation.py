from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QApplication, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from backroundWin import BaseWindow

class ReservationWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #363636;")
        self.add_content_to_main_layout()

    def add_content_to_main_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Align content to the top

        # Notification message right under the logo
        notification_label = QLabel("Υπάρχει διαθεσιμότητα, προχωρήστε στα στοιχεία κράτησης.")
        notification_label.setWordWrap(True)
        notification_label.setAlignment(Qt.AlignCenter)
        notification_label.setFont(QFont('Arial', 14))
        notification_label.setStyleSheet("""
            QLabel {
                background-color: white; 
                color: black; 
                padding: 10px; 
                border-radius: 10px; 
                margin: 20px; 
                border: 2px solid #FFFFFF;
            }
        """)
        layout.addWidget(notification_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Table selection
        table_selection_layout = QHBoxLayout()
        table_selection_layout.setAlignment(Qt.AlignLeft)
        table_selection_label = QLabel("Επιλογή τραπεζιού")
        table_selection_label.setFont(QFont('Arial', 14))
        table_selection_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF; 
                padding: 5px; 
                border: 2px solid #FFFFFF; 
                border-radius: 10px;
            }
        """)
        table_selection_combo = QComboBox()
        table_selection_combo.addItems(["Table 1", "Table 2", "Table 3"])  # Example items
        table_selection_combo.setStyleSheet("padding: 5px;")
        table_selection_layout.addWidget(table_selection_label)
        table_selection_layout.addWidget(table_selection_combo)
        layout.addLayout(table_selection_layout)

        # Number of people selection
        people_selection_layout = QHBoxLayout()
        people_selection_layout.setAlignment(Qt.AlignLeft)
        people_selection_label = QLabel("Επιλογή αριθμού ατόμων")
        people_selection_label.setFont(QFont('Arial', 14))
        people_selection_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF; 
                padding: 5px; 
                border: 2px solid #FFFFFF; 
                border-radius: 10px;
            }
        """)
        people_spinbox = QSpinBox()
        people_spinbox.setValue(1)
        people_spinbox.setStyleSheet("padding: 5px;")

        people_selection_layout.addWidget(people_selection_label)
        people_selection_layout.addWidget(people_spinbox)
        layout.addLayout(people_selection_layout)

        # Search button
        search_button = QPushButton("search")
        search_button.setFont(QFont('Arial', 14))
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #5C6BC0;
                color: white;
                font-size: 14px;
                padding: 10px 20px;
                border-radius: 20px;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #7986CB;
            }
            QPushButton:pressed {
                background-color: #3F51B5;
            }
        """)
        layout.addWidget(search_button, alignment=Qt.AlignCenter)

        

        # Add the content layout to the main layout in BaseWindow
        self.addContent(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = ReservationWindow()
    window.show()
    app.exec_()
