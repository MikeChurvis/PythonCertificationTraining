import csv

with open('contacts.csv', newline='') as csvfile:
    # reader = csv.reader(csvfile, delimiter=',')
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(",".join(row))
        print(row['Name'], ':', row['Phone'])

