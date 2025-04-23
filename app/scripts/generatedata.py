from faker import Faker
import pandas as pd
import os
import random

# Initialize Faker
fake = Faker()

# Set the directory to save the data
save_dir = './app/datas'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# List of services
services_list = [
    "General Cleaning",
    "Residential Cleaning",
    "Deep Cleaning",
    "Garage Cleaning",
    "Bathroom Cleaning",
    "Window Cleaning",
    "Carpet Cleaning",
    "Office Cleaning",
    "End of Lease Cleaning",
    "Post Construction Cleaning"
]

# Function to generate User Admin Data
def generate_user_admin_data(num_records=100):
    user_admin_data = []
    for _ in range(num_records):
        user_admin_data.append({
            "Username": fake.user_name(),
            "Email": fake.email(),
            "Password": fake.password(),
            "Role": "User Admin"
        })
    return user_admin_data

# Function to generate Homeowner Data
def generate_homeowner_data(num_records=100):
    homeowner_data = []
    for _ in range(num_records):
        homeowner_data.append({
            "Username": fake.user_name(),
            "Email": fake.email(),
            "Password": fake.password(),
            "Address": fake.address(),
            "Role": "Homeowner"
        })
    return homeowner_data

# Function to generate Platform Management Data
def generate_platform_management_data(num_records=100):
    platform_management_data = []
    for _ in range(num_records):
        platform_management_data.append({
            "Username": fake.user_name(),
            "Email": fake.email(),
            "Password": fake.password(),
            "Role": "Platform Management"
        })
    return platform_management_data

# Function to generate Cleaner Data
def generate_cleaner_data(num_records=100):
    cleaner_data = []
    for _ in range(num_records):
        # Randomly choose 2-4 services for each cleaner
        services = random.sample(services_list, k=random.randint(2, 4))
        cleaner_data.append({
            "Username": fake.user_name(),
            "Email": fake.email(),
            "Password": fake.password(),
            "Role": "Cleaner",
            "Services": ", ".join(services),  # Join selected services into a string
            "Pricing": fake.random_number(digits=2),  # Random price for services
            "Number_of_Views": fake.random_int(min=0, max=1000),  # Sensitive Data: number of views
            "Number_of_Shortlists": fake.random_int(min=0, max=500),  # Sensitive Data: number of times shortlisted
        })
    return cleaner_data

# Save Data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(save_dir, filename), index=False)

# Generate and Save Data for each stakeholder
user_admin_data = generate_user_admin_data()
homeowner_data = generate_homeowner_data()
platform_management_data = generate_platform_management_data()
cleaner_data = generate_cleaner_data()

save_to_csv(user_admin_data, 'user_admin_data.csv')
save_to_csv(homeowner_data, 'homeowner_data.csv')
save_to_csv(platform_management_data, 'platform_management_data.csv')
save_to_csv(cleaner_data, 'cleaner_data.csv')

print("Data has been generated and saved to CSV files.")
