import csv

def read_csv(filename):
    """
    Reads a CSV file and returns its content as a list of lists.
    Each inner list represents a row in the CSV file.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def write_to_csv(data, filename):
    """
    Writes data to a CSV file.
    data is a list of lists, where each inner list represents a row in the CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
