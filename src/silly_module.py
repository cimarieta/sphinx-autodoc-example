# coding: utf-8
import pandas as pd


class PandasInput():
    """Class responsible for dealing with input pandas objects
    (docstring written using Google style)

    Attributes:
        csv_file (str): filename of the csv file

    """
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load_df(self, sep=','):
        """Load dataframe

        Args:
            `sep` (str, optional): separator (default: comma)

        Returns:
            dataframe

        """
        return pd.read_csv(self.csv_file)


def fun_to_test(number):
    """Triple power `number`
    (docstring written using Numpy style)

    Parameters
    ----------
    number : int
        número

    Returns
    -------
    int

    """
    return number*number*number
