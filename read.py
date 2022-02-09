import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path, "r")
    l = []
    for row in csv.reader(file):
        l.append(row)