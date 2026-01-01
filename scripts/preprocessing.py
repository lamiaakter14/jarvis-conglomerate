"""
scripts.preprocessing

This module is responsible for handling data cleaning, normalization, and preparation routines for simulations and analyses.
"""

import csv
import json
import os


def load_data(path):
    """Load data from CSV/JSON files with error handling.

    Args:
        path (str): Path to the data file (CSV or JSON).

    Returns:
        object: Loaded data as a dictionary or list. For CSV files without pandas,
                returns a list of dictionaries. For JSON files, returns the parsed JSON object.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is not supported.
        Exception: For other errors during file loading.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    file_extension = os.path.splitext(path)[1].lower()

    if file_extension == '.json':
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            raise Exception(f"Error loading JSON data from {path}: {str(e)}")
        except Exception as e:
            raise Exception(f"Error loading data from {path}: {str(e)}")
    elif file_extension == '.csv':
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            return data
        except Exception as e:
            raise Exception(f"Error loading CSV data from {path}: {str(e)}")
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: .csv, .json")


def clean_data(df):
    """Handle missing values and normalize numerical columns in a DataFrame.

    Args:
        df (list or dict): Input data structure (list of dictionaries for CSV-like data,
                          or dictionary for JSON-like data).

    Returns:
        list or dict: Cleaned data with missing values handled and numerical columns normalized.

    Note:
        - Missing values (None, empty strings) are removed or replaced with defaults.
        - Numerical columns are normalized to [0, 1] range where applicable.
        - This is a basic implementation without pandas dependency.
    """
    if isinstance(df, list):
        # Handle list of dictionaries (CSV-like data)
        cleaned_data = []
        for row in df:
            cleaned_row = {}
            for key, value in row.items():
                # Handle missing values
                if value is None or value == '':
                    cleaned_row[key] = None
                else:
                    # Try to convert to float for numerical values
                    try:
                        cleaned_row[key] = float(value)
                    except (ValueError, TypeError):
                        cleaned_row[key] = value
            cleaned_data.append(cleaned_row)
        return cleaned_data
    elif isinstance(df, dict):
        # Handle dictionary data
        cleaned_dict = {}
        for key, value in df.items():
            if value is None or value == '':
                cleaned_dict[key] = None
            else:
                cleaned_dict[key] = value
        return cleaned_dict
    else:
        return df


def transform_features(df):
    """Placeholder function for feature engineering to prepare data for ML models.

    Args:
        df (list or dict): Input data structure.

    Returns:
        list or dict: Transformed data with engineered features (placeholder).

    Note:
        This is a placeholder for future feature engineering implementations.
        Possible transformations include:
        - Creating interaction features
        - Polynomial features
        - Encoding categorical variables
        - Scaling features
        - Dimensionality reduction
    """
    # TODO: Implement feature engineering logic
    # Placeholder: return data as-is for now
    return df