import unittest
from innovation.research import Research
from innovation.material_discovery import MaterialDiscovery

class TestInnovation(unittest.TestCase):

    def test_research_add_and_run(self):
        research = Research(name="Test Research")
        research.add_experiment({"name": "Exp1"})
        self.assertEqual(len(research.experiments), 1)

        result = research.run_experiment("Exp1")
        self.assertEqual(result["status"], "success")

    def test_material_discovery(self):
        discovery = MaterialDiscovery()

        target = {"strength": "high"}
        constraints = {"composition": "Fe-C"}
        result = discovery.discover_new_material(target, constraints)
        self.assertEqual(result["status"], "discovered")

        pred = discovery.predict_material_properties({"Fe": 2, "C": 1})
        self.assertEqual(pred["status"], "predicted")

        opt = discovery.optimize_material({"hardness": "medium"})
        self.assertEqual(opt["status"], "optimized")

if __name__ == "__main__":
    unittest.main()
