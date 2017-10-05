import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import numpy as np
from q05_create_bowler_filter.build import create_bowler_filter
<<<<<<< HEAD
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
=======
from greyatomlib.pandas.q01_read_csv_data_to_df.build import read_csv_data_to_df
>>>>>>> eed8c8c156e5093efb39cedf06b4c16d588a311f
from unittest import TestCase


class TestCreate_bowler_filter(TestCase):
    def test_create_bowler_filter(self):
        path = "./data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        bowler = 'I Sharma'
        expected = 1599
        actual = create_bowler_filter(bowler).sum()
        self.assertTrue(np.all(expected == actual))