# Dependencies
from faker import Faker
import csv
import pandas as pd

# Create a Faker instance
fake = Faker()
# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.phone_number())
# print(fake.address())
# print(fake.job())
# print(fake.company())
# print(fake.country())
# print(fake.text())
# Set the headers
fields = ['First Name', 'Last Name', 'Email', 'Phone Number', 'Address', 'Country', 'Job', 'Company Location', 'Bio']
# # # Create a csv file
fileName = 'cust.csv'

with open(fileName, 'w') as csvFile:
    csvwriter = csv.writer(csvFile)
    csvwriter.writerow(fields)
    x = 0
    # Loop through the fake data to create all the entries
    #  While is number of rows you want in you csv file.
    while x <= 100000:
        csvwriter.writerows([[
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.phone_number(),
            fake.address(),
            fake.country(),
            fake.job(),
            fake.company(),
            fake.text()
        ]])
        x += 1

# # Open the CSV and removes all the empty rows and makes a new output CSV call Customer.csv
df = pd.read_csv(fileName)
df.to_csv('Customer.csv', index=False)
