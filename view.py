#! /usr/bin/env python3

"""
View module for the Nitinol Material Properties Extractor application.

This module contains the DataView class which defines the GUI.
"""

# pylint: disable=no-name-in-module

from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class DataView(QMainWindow):
    """
    The DataView class defines the graphical user interface for the application.
    """

    def __init__(self):
        """
        Initialize the DataView with a window, layout, and widgets.
        """
        super().__init__()
        self.setWindowTitle("Nitinol Material Properties Extractor")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel("Load your CSV or Excel file")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Load File")
        self.layout.addWidget(self.button)

        self.plot_label = QLabel()
        self.plot_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.plot_label)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def set_plot(self, plot_path):
        """
        Set the plot image in the label.

        Parameters
        ----------
        plot_path : str
            The path to the plot image file
        """
        self.plot_label.setPixmap(
            QPixmap(plot_path).scaled(600, 400, Qt.KeepAspectRatio)
        )

    def show_message(self, title, message):
        """
        Display an informational message box.

        Parameters
        ----------
        title : str
            The title of the message box
        message : str
            The message to display
        """
        QMessageBox.information(self, title, message)

    def show_error(self, message):
        """
        Display an error message box.

        Parameters
        ----------
        message : str
            The error message to display
        """
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("An error occurred")
        error_dialog.setInformativeText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
