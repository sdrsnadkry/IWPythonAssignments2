import csv


def writing_csv(filename, data):
    with open(filename, 'w') as store:
        csv_write = csv.writer(store)

        csv_write.writerow(['name', 'address', 'age'])  # adds heading to top

        for row in data:
            csv_write.writerow(row)  # adds data in loop


filename = 'store.csv'
data = [('sudarshan', 'Koteshwor', 24),
        ('adhikari', 'baneshwor', 25), ('om', 'mulpani', 25)]
writing_csv(filename, data)
