#! /usr/bin/env python3

"""
Controller module for the Nitinol Material Properties Extractor application.

This module contains the DataController class which mediates between the model
(DataModel) and the view (DataView).
"""

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
)  # pylint: disable=no-name-in-module
from model import DataModel
from view import DataView


class DataController:
    """
    The DataController class connects the user input from the view and updates
    the model accordingly.
    """

    def __init__(self, data_model_instance, data_view_instance):
        """
        Initialize the controller with a model and a view.

        Parameters
        ----------
        data_model_instance : DataModel
            The data model instance
        data_view_instance : DataView
            The data view instance
        """
        self.model = data_model_instance
        self.view = data_view_instance
        self.view.button.clicked.connect(self.load_file)

    def load_file(self):
        """
        Load a file and process the data.

        Opens a file dialog to select a CSV or Excel file, loads the data into
        the model, processes it, and updates the view with the results.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self.view,
            "Open File",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx)",
            options=options,
        )
        if file_name:
            try:
                self.model.load_data(file_name)
                plot_path, text_output_path = self.model.process_data(file_name)
                self.view.set_plot(plot_path)
                self.view.show_message(
                    "Success",
                    f"Plot saved to {plot_path}\nResults saved to {text_output_path}",
                )
            except ValueError as error:
                self.view.show_error(str(error))
            except Exception as error:  # pylint: disable=broad-except
                self.view.show_error(str(error))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = DataModel()
    view = DataView()
    controller = DataController(model, view)
    view.show()
    sys.exit(app.exec_())
