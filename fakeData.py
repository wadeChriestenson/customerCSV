# Dependencies
from faker import Faker
import csv
import pandas as pd

# Create a Faker instance
fake = Faker()

# Create a csv file
fileName = 'cust.csv'

# Set the headers
fields = ['Name', 'Email', 'Address', 'Country', 'Company']

# Open file and write the csv
with open(fileName, 'w') as csvFile:
    csvwriter = csv.writer(csvFile)
    csvwriter.writerow(fields)
    x = 0
    # Loop through the fake data to create all the entries
    #  While is number of rows you want in you csv file.
    while x <= 100000:
        csvwriter.writerows([[fake.name(),
                             fake.email(),
                             fake.address(),
                             fake.country(),
                             fake.company()]])
        x += 1

# Open the CSV and removes all the empty rows and makes a new output CSV call Customer.csv
df = pd.read_csv(fileName)
df.to_csv('Customer.csv', index=False)