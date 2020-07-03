import csv


def reading_csv(filename):
    with open(filename, 'r') as store:
        csv_reader = csv.DictReader(store)

        for line in csv_reader:
            print(line)


filename = 'store.csv'
reading_csv(filename)
