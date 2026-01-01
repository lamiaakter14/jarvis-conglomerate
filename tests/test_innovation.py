"""
Test cases for the innovation module.

This file includes tests to ensure the innovation module's Research and 
MaterialDiscovery classes work as expected.
"""

from innovation.research import Research
from innovation.material_discovery import MaterialDiscovery


def test_research_initialization():
    """Test Research class initialization."""
    research = Research(name="Test Research")
    assert research.name == "Test Research"
    assert research.experiments == []
    assert research.simulation_data == []
    assert research.material_discoveries == []


def test_research_add_experiment():
    """Test adding experiments to Research."""
    research = Research()
    experiment = {"name": "Test Experiment", "type": "simulation"}
    research.add_experiment(experiment)
    assert len(research.experiments) == 1
    assert research.experiments[0]["name"] == "Test Experiment"


def test_research_run_experiment():
    """Test running a specific experiment."""
    research = Research()
    experiment = {"name": "Test Experiment", "type": "simulation"}
    research.add_experiment(experiment)
    result = research.run_experiment("Test Experiment")
    assert result["status"] == "success"
    assert result["experiment"] == "Test Experiment"


def test_research_integrate_simulation_data():
    """Test integrating simulation data."""
    research = Research()
    simulation_output = {"physics": "data", "results": [1, 2, 3]}
    research.integrate_simulation_data(simulation_output)
    assert len(research.simulation_data) == 1


def test_research_integrate_material_discovery():
    """Test integrating material discovery results."""
    research = Research()
    discovery_results = {"material": "Fe2O3", "properties": {}}
    research.integrate_material_discovery_results(discovery_results)
    assert len(research.material_discoveries) == 1


def test_research_analyze_data():
    """Test research data analysis."""
    research = Research()
    analysis = research.analyze_research_data()
    assert analysis["status"] == "success"
    assert "total_experiments" in analysis


def test_research_generate_report():
    """Test research report generation."""
    research = Research()
    report = research.generate_research_report()
    assert "Research Report" in report
    assert "Jarvis Research" in report


def test_material_discovery_initialization():
    """Test MaterialDiscovery class initialization."""
    discovery = MaterialDiscovery(name="Test Discovery")
    assert discovery.name == "Test Discovery"
    assert discovery.materials_data == []
    assert discovery.discovered_materials == []


def test_material_discovery_discover_new_material():
    """Test discovering new materials."""
    discovery = MaterialDiscovery()
    target_properties = {"strength": "high", "conductivity": "medium"}
    result = discovery.discover_new_material(target_properties)
    assert result["status"] == "success"
    assert "material_id" in result


def test_material_discovery_predict_properties():
    """Test predicting material properties."""
    discovery = MaterialDiscovery()
    composition = {"elements": ["Fe", "O"], "ratio": [2, 3]}
    result = discovery.predict_material_properties(composition)
    assert result["status"] == "success"
    assert "predicted_properties" in result


def test_material_discovery_simulate_material():
    """Test material simulation."""
    discovery = MaterialDiscovery()
    properties = {"density": 7.8, "melting_point": 1500}
    result = discovery.simulate_material(properties)
    assert result["status"] == "success"
    assert "predictions" in result


def test_material_discovery_optimize_materials():
    """Test material optimization."""
    discovery = MaterialDiscovery()
    result = discovery.optimize_materials(optimization_target="performance")
    assert result["status"] == "success"
    assert result["target"] == "performance"


def test_material_discovery_integrate_simulations():
    """Test integration with simulations."""
    discovery = MaterialDiscovery()
    simulation_output = {"physics_data": [1, 2, 3], "environment": "test"}
    discovery.integrate_with_simulations(simulation_output)
    assert len(discovery.materials_data) == 1


def test_material_discovery_train_ml_model():
    """Test ML model training."""
    discovery = MaterialDiscovery()
    training_data = [
        {"composition": {"Fe": 2, "O": 3}, "strength": 100},
        {"composition": {"Al": 2, "O": 3}, "strength": 80}
    ]
    result = discovery.train_ml_model(training_data, model_type="property_prediction")
    assert result["status"] == "success"
    assert result["training_samples"] == 2


def test_material_discovery_analyze_chemistry():
    """Test chemistry analysis."""
    discovery = MaterialDiscovery()
    result = discovery.analyze_material_chemistry("Fe2O3")
    assert result["status"] == "success"
    assert result["formula"] == "Fe2O3"