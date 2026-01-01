"""Test cases for the scripts module."""

import os
import json
import tempfile
import pytest
from scripts.preprocessing import load_data, clean_data, transform_features
from scripts.automation import run_pipeline, schedule_task


class TestPreprocessing:
    """Test cases for scripts.preprocessing module."""

    def test_load_data_json(self):
        """Test loading JSON data."""
        # Create a temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            test_data = {"key": "value", "number": 42}
            json.dump(test_data, f)
            temp_path = f.name

        try:
            data = load_data(temp_path)
            assert data == test_data
        finally:
            os.unlink(temp_path)

    def test_load_data_csv(self):
        """Test loading CSV data."""
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("name,age,city\n")
            f.write("Alice,30,NYC\n")
            f.write("Bob,25,LA\n")
            temp_path = f.name

        try:
            data = load_data(temp_path)
            assert isinstance(data, list)
            assert len(data) == 2
            assert data[0]['name'] == 'Alice'
            assert data[0]['age'] == '30'
        finally:
            os.unlink(temp_path)

    def test_load_data_file_not_found(self):
        """Test loading data from non-existent file."""
        with pytest.raises(FileNotFoundError):
            load_data('/nonexistent/path/file.json')

    def test_load_data_unsupported_format(self):
        """Test loading data from unsupported file format."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("test data")
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Unsupported file format"):
                load_data(temp_path)
        finally:
            os.unlink(temp_path)

    def test_clean_data_list(self):
        """Test cleaning list data."""
        input_data = [
            {'name': 'Alice', 'age': '30', 'score': '95.5'},
            {'name': 'Bob', 'age': '', 'score': '87.3'},
            {'name': '', 'age': '25', 'score': None}
        ]
        cleaned = clean_data(input_data)
        assert isinstance(cleaned, list)
        assert len(cleaned) == 3
        # Check numerical conversion
        assert cleaned[0]['age'] == 30.0
        assert cleaned[0]['score'] == 95.5

    def test_clean_data_dict(self):
        """Test cleaning dictionary data."""
        input_data = {'name': 'Alice', 'age': 30, 'city': ''}
        cleaned = clean_data(input_data)
        assert isinstance(cleaned, dict)
        assert cleaned['name'] == 'Alice'
        assert cleaned['age'] == 30
        assert cleaned['city'] is None

    def test_transform_features(self):
        """Test feature transformation (placeholder)."""
        input_data = [{'feature1': 1, 'feature2': 2}]
        transformed = transform_features(input_data)
        # Placeholder should return data as-is
        assert transformed == input_data


class TestAutomation:
    """Test cases for scripts.automation module."""

    def test_run_pipeline(self):
        """Test pipeline execution."""
        result = run_pipeline()
        assert isinstance(result, dict)
        assert 'status' in result
        assert result['status'] == 'success'
        assert 'preprocessing' in result
        assert 'simulation' in result
        assert 'innovation' in result

    def test_schedule_task_valid(self):
        """Test task scheduling with valid parameters."""
        def sample_task():
            return "Task executed"

        schedule_info = schedule_task(sample_task, interval=60)
        assert isinstance(schedule_info, dict)
        assert schedule_info['task_name'] == 'sample_task'
        assert schedule_info['interval'] == 60
        assert 'status' in schedule_info

    def test_schedule_task_invalid_task(self):
        """Test task scheduling with non-callable task."""
        with pytest.raises(ValueError, match="Task must be a callable"):
            schedule_task("not a function", interval=60)

    def test_schedule_task_invalid_interval(self):
        """Test task scheduling with invalid interval."""
        def sample_task():
            return "Task executed"

        with pytest.raises(ValueError, match="Interval must be a positive integer"):
            schedule_task(sample_task, interval=-10)

        with pytest.raises(ValueError, match="Interval must be a positive integer"):
            schedule_task(sample_task, interval=0)


def test_scripts_placeholder():
    """Placeholder test for the scripts module."""
    assert True
