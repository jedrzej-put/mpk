import csv
class ReadFile():
    def __init__(self,filename):
        self.filename = filename
    def get_data_row(self):
        with open(self.filename, newline='',encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader) # skip header lines
            for row in reader:
                yield row