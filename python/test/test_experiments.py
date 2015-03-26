import unittest
from experiments import SyntheticExperiment, count_pairwise_class_balance
from database import SyntheticDatabase
__author__ = 'mbarnes1'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Create synthetic database, run ER on it
        # a entities, b records per entity, c train records, d validation records, e train class balance, f thresholds
        self.experiment = SyntheticExperiment(10, 10, 30, 30, 0.5, 5)

    def test_get_pairwise_class_balance(self):
        synthetic_database = SyntheticDatabase(10, 10, number_features=2)
        class_balance = count_pairwise_class_balance(synthetic_database.labels)
        self.assertEqual(class_balance, 9.0/99.0)



if __name__ == '__main__':
    unittest.main()