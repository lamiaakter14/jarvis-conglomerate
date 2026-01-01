"""core.utils

Utility functions for logging, config reading, and error handling.
Includes placeholders for future utilities.
"""

import json
import yaml
import traceback
from functools import wraps
from datetime import datetime
from typing import Callable, Any


def log(message: str, level: str = 'INFO') -> None:
    """
    Log messages to the console, categorized by level.
    
    Args:
        message (str): The message to log.
        level (str): The log level (INFO, ERROR, DEBUG, WARNING). Defaults to 'INFO'.
    
    Returns:
        None
    
    Notes:
        TODO: Add log file output for persistent logging.
        TODO: Add configuration for log format customization.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] [{level}] {message}"
    print(log_message)
    
    # TODO: Add file logging
    # Example: logging.getLogger().handlers[0].stream = open('jarvis.log', 'a')


def read_config(file_path: str) -> dict:
    """
    Load configuration data from YAML or JSON files.
    
    Args:
        file_path (str): Path to the configuration file (YAML or JSON).
    
    Returns:
        dict: Parsed configuration data.
    
    Raises:
        ValueError: If the file format is not supported (neither YAML nor JSON).
        FileNotFoundError: If the file does not exist.
        Exception: For other parsing errors.
    
    Notes:
        TODO: Add support for additional configuration formats (e.g., TOML, INI).
        TODO: Add configuration validation against a schema.
        TODO: Add environment variable interpolation in config files.
    """
    try:
        with open(file_path, 'r') as file:
            if file_path.endswith(('.yaml', '.yml')):
                config = yaml.safe_load(file)
                log(f"Successfully loaded YAML config from {file_path}", level='INFO')
                return config
            elif file_path.endswith('.json'):
                config = json.load(file)
                log(f"Successfully loaded JSON config from {file_path}", level='INFO')
                return config
            else:
                error_msg = f"Unsupported file format: {file_path}. Only YAML (.yaml, .yml) and JSON (.json) are supported."
                log(error_msg, level='ERROR')
                raise ValueError(error_msg)
    except FileNotFoundError:
        error_msg = f"Configuration file not found: {file_path}"
        log(error_msg, level='ERROR')
        raise
    except yaml.YAMLError as e:
        error_msg = f"Error parsing YAML file {file_path}: {str(e)}"
        log(error_msg, level='ERROR')
        raise
    except json.JSONDecodeError as e:
        error_msg = f"Error parsing JSON file {file_path}: {str(e)}"
        log(error_msg, level='ERROR')
        raise
    except Exception as e:
        error_msg = f"Unexpected error reading config from {file_path}: {str(e)}"
        log(error_msg, level='ERROR')
        raise


def handle_error(func: Callable) -> Callable:
    """
    Decorator for logging runtime exceptions with full traceback.
    
    Args:
        func (Callable): The function to wrap with error handling.
    
    Returns:
        Callable: The wrapped function with error handling.
    
    Notes:
        TODO: Add support for custom exception handlers.
        TODO: Add retry logic for transient errors.
        TODO: Add metrics collection for error tracking.
    
    Example:
        @handle_error
        def my_function():
            # Your code here
            pass
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = f"Exception in {func.__name__}: {str(e)}"
            log(error_msg, level='ERROR')
            log(f"Traceback:\n{traceback.format_exc()}", level='DEBUG')
            raise
    return wrapper