# Nitinol Material Properties Extractor

This project provides a GUI application for extracting material properties from Nitinol stress-strain data. The application allows users to load CSV or Excel files containing strain and stress data, process the data, and visualize the results.

## Features

- Load data from CSV or Excel files.
- Plot stress-strain curves.
- Save plots and descriptive statistics to files.
- Simple and intuitive GUI built with PyQt5.

## Requirements

- Python 3.10 or higher
- Virtual environment (venv)
- Required Python packages listed in `requirements.txt`

## Setup

### 1. Clone the Repository

```
git clone https://github.com/epw/nitinol-extractor
cd nitinol-extractor
```

### 2. Create and Activate a Virtual Environment

```
python3 -m venv venv
```

```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Directory Permissions (If Required)

Ensure the runtime directory permissions are correct:

```
sudo chmod 0700 /run/user/1000
```

### Usage

1. Create Sample Data (Optional)
To generate a sample CSV file with strain and stress data:

```
python3 -c "from model import create_sample_csv; create_sample_csv()"
```

2. Run the Application

```
python3 main.py
```

3. Debugging (Optional)
To run the application with detailed Qt plugin debugging information:

```
export QT_DEBUG_PLUGINS=1
python3 main.py
```

### Project Structure

- main.py: Initializes the application by creating instances of the model, view, and controller.
- model.py: Contains the DataModel class for loading and processing data, and a function to create sample CSV data.
- view.py: Defines the DataView class which provides the GUI.
- controller.py: Contains the DataController class which mediates between the model and the view.
- requirements.txt: Lists the required Python packages.

### Demo

[loom](https://www.loom.com/share/159a28684c764c09a790f1d7cfbfe3d9?sid=3bc822d0-e612-49c5-9a34-7a9408810655)

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
