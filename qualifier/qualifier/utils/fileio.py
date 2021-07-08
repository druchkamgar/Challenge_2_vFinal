# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data




def save_csv(csvpath, qualifying_loans):
    """Writes to a CSV file 

    Args:
        csvpath (Path): the file path name is provided in save_qualifying_loans

    Returns:
        A csv file with rows of data from save_qualifying_loans

    """
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header = []
        csvwriter.writerow(header)
        csvwriter.writerow(qualifying_loans)
