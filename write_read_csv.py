from faker import Faker
import csv


def write_read_csv():
    fake = Faker()
    fakedata = []

    for details in range(1000):
        fakedata.append([fake.name(), fake.random_int(min=20, max=65, step=1), fake.street_address(),
        fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])
    
    #write csv
    with open('fakedata.csv','w', newline='') as f:
        nameswriter = csv.writer(f)
        header = ['name', 'age', 'street', 'city', 'city','zip', 'lng', 'lat']
        nameswriter.writerow(header)
        nameswriter.writerows(fakedata)

    #read csv
    with open('fakedata.csv', 'r') as file:
        namesreader = csv.reader(file)
        next(namesreader) # Skip the header row
        for row in namesreader:
            print(row)

write_read_csv()
