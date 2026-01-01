"""core.utils

Utility functions for logging, config reading, and error handling.
Includes placeholders for future utilities.
"""

import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("Jarvis")

def read_config(file_path):
    """Read configuration from a file (placeholder)."""
    print(f"Reading config from {file_path} (placeholder).")

def handle_error(error_message):
    """Handle errors gracefully (placeholder)."""
    print(f"Error: {error_message}")