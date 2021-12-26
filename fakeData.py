# Dependencies
from faker import Faker
import csv
import pandas as pd

# Create a Faker instance
fake = Faker()
# print(fake.uuid4())
# print(fake.date_time())
# print(fake.first_name())
# print(fake.last_name())
# print(fake.phone_number())
# print(fake.company_email())
# print(fake.job())
# print(fake.company())
# print(fake.country())
# print(fake.timezone())
# print(fake.currency_code())


# Set the headers
fields = ['User Key', 'First Contract', 'First Name', 'Last Name', 'Phone Number', 'Company Email', 'Job', 'Company', 'Companies Location', 'Timezone', 'Type of Currency']
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
            fake.uuid4(),
            fake.date_time(),
            fake.first_name(),
            fake.last_name(),
            fake.phone_number(),
            fake.company_email(),
            fake.job(),
            fake.company(),
            fake.country(),
            fake.timezone(),
            fake.currency_code()
        ]])
        x += 1

# # Open the CSV and removes all the empty rows and makes a new output CSV call Customer.csv
df = pd.read_csv(fileName)
df.to_csv('Customer.csv', index=False)
