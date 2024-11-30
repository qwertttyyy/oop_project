import csv
import os

class CSVManager:
    
    def __init__(self, path):
        self.path = path

    def read_data(self):
        if not os.path.exists(self.path):
            return []
        
        with open(self.path, 'r' , encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        return data
    
    def overwrite_file(self, initial_data):
        with open(self.path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(initial_data)

    def add_row(self, row):
        with open(self.path, 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)