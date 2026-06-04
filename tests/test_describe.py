import unittest
import pandas as pd

from descripstats import Describe


class TestDescribe(unittest.TestCase):
    def test_describe_basic(self):
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})
        stats = Describe(df)

        self.assertIsInstance(stats, pd.DataFrame)

        # required additional rows
        for row in ["mad", "variance", "sem", "sum", "skewness", "kurtosis"]:
            self.assertIn(row, stats.index)

        # columns
        self.assertIn("A", stats.columns)
        self.assertIn("B", stats.columns)

        # numeric checks
        self.assertAlmostEqual(stats.loc["mean", "A"], 3.0, places=6)
        self.assertAlmostEqual(stats.loc["sum", "B"], 150.0, places=6)


if __name__ == "__main__":
    unittest.main()
