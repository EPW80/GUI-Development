#! /usr/bin/env python3

"""
This module provides the DataModel class for loading and processing
Nitinol material properties from CSV or Excel files. It also provides
a function for creating a sample CSV file with strain and stress data.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


class DataModel:
    """
    A class to represent the data model for Nitinol material properties.

    Attributes
    ----------
    data : pandas.DataFrame
        DataFrame to hold the loaded data
    plot_path : str
        Path to save the plot
    text_output_path : str
        Path to save the text output
    """

    def __init__(self):
        """Initialize the DataModel with default attributes."""
        self.data = None
        self.plot_path = None
        self.text_output_path = None

    def load_data(self, file_path):
        """
        Load data from a CSV or Excel file.

        Parameters
        ----------
        file_path : str
            The path to the file to load

        Returns
        -------
        pandas.DataFrame
            The loaded data
        """
        if file_path.endswith(".csv"):
            self.data = pd.read_csv(file_path)
        else:
            self.data = pd.read_excel(file_path)
        return self.data

    def process_data(self, file_path):
        """
        Process the loaded data to generate a plot and descriptive statistics.

        Parameters
        ----------
        file_path : str
            The path to the file to process

        Returns
        -------
        tuple
            Paths to the saved plot and text output files
        """
        if (
            "strain" not in self.data.columns or "stress" not in self.data.columns
        ):  # pylint: disable=no-member
            raise ValueError('The file must contain "strain" and "stress" columns.')

        plt.figure()
        plt.plot(self.data["strain"], self.data["stress"], label="Stress-Strain Curve")
        plt.xlabel("Strain")
        plt.ylabel("Stress")
        plt.title("Stress-Strain Curve")
        plt.legend()

        self.plot_path = os.path.splitext(file_path)[0] + "_plot.png"
        plt.savefig(self.plot_path)

        self.text_output_path = os.path.splitext(file_path)[0] + "_results.txt"
        with open(self.text_output_path, "w", encoding="utf-8") as file:
            file.write(f"Strain-Stress Data Analysis\n\nFile: {file_path}\n")
            file.write(self.data.describe().to_string())

        return self.plot_path, self.text_output_path


def create_sample_csv(file_path="strain_stress_data.csv"):
    """
    Create a sample CSV file with strain and stress data.

    Parameters
    ----------
    file_path : str
        The path to the file to save
    """
    # Create a dictionary with data
    data = {
        "strain": [0.01, 0.02, 0.03, 0.04, 0.05],
        "stress": [100, 200, 300, 400, 500],
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    print(f"CSV file created successfully at {file_path}.")
