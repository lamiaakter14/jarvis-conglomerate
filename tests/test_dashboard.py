"""
Test cases for the dashboard module.

This file includes tests to ensure the dashboard module's Flask application 
and features work as expected.
"""

import pytest
from dashboard.app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_dashboard_placeholder():
    """Basic placeholder test for dashboard functionality."""
    assert True


def test_flask_app_exists():
    """Test that the Flask app is properly initialized."""
    assert app is not None
    assert app.config['DASHBOARD_TITLE'] == "JARVIS 2.0 Dashboard"


def test_index_route(client):
    """Test the main index route returns 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'JARVIS 2.0 Dashboard' in response.data


def test_simulation_route(client):
    """Test the simulation view route."""
    response = client.get('/simulation')
    assert response.status_code == 200
    assert b'simulation' in response.data.lower()


def test_innovation_route(client):
    """Test the innovation view route."""
    response = client.get('/innovation')
    assert response.status_code == 200
    assert b'innovation' in response.data.lower()


def test_core_route(client):
    """Test the core API route."""
    response = client.get('/core')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'


def test_health_api(client):
    """Test the health check API endpoint."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data
    assert 'modules' in data


def test_metrics_api(client):
    """Test the metrics API endpoint."""
    response = client.get('/api/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'metrics' in data
