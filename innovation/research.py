import unittest
from innovation.research import Research
from innovation.material_discovery import MaterialDiscovery

class TestInnovation(unittest.TestCase):

    def test_research_add_and_run(self):
        research = Research(name="Test Research")
        research.add_experiment({"name": "Exp1"})
        self.assertEqual(len(research.experiments), 1)
        research.run_experiment("Exp1")
        research.run_all_experiments()

    def test_material_discovery_methods(self):
        discovery = MaterialDiscovery()
        props = {"composition": "Fe-C"}
        target = {"strength": "high"}
        result = discovery.discover_new_material(target_properties=target, constraints=props)
        self.assertEqual(result["status"], "discovered")
        pred = discovery.predict_material_properties(props)
        self.assertEqual(pred["status"], "predicted")
        opt = discovery.optimize_material(target)
        self.assertEqual(opt["status"], "optimized")

if __name__ == "__main__":
    unittest.main()

