#! /usr/bin/env python3

"""
Main module for the Nitinol Material Properties Extractor application.

This module initializes the application by creating instances of the model,
view, and controller, and starts the main event loop.
"""

import sys
from PyQt5.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from model import DataModel, create_sample_csv
from view import DataView
from controller import DataController

if __name__ == "__main__":
    # Create the sample CSV file
    create_sample_csv()

    # Initialize the application
    app = QApplication(sys.argv)
    model = DataModel()
    view = DataView()
    controller = DataController(model, view)
    view.show()
    sys.exit(app.exec_())
