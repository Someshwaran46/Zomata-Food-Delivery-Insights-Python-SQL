import pymysql 
from faker import Faker 
import random
from datetime import timedelta 
 
# Initialize Faker 
fake = Faker("en_IN") 
 
# Connect to MySQL database 
db = pymysql.connect( 
    host="localhost", 
    user="root", 
    password="root", 
) 
cursor = db.cursor() 
cursor.execute("create database Zomata") 
cursor.execute("use Zomata") 
 
# Create tables 
cursor.execute("CREATE TABLE Customers (customer_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),email VARCHAR(255),phone VARCHAR(50),location TEXT,signup_date DATE,is_premium BOOLEAN,preferred_cuisine VARCHAR(50),total_orders INT,average_rating FLOAT)") 
 
cursor.execute("CREATE TABLE Restaurants (restaurant_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),cuisine_type VARCHAR(50),location TEXT,owner_name VARCHAR(255),average_delivery_time INT,contact_number VARCHAR(50),rating FLOAT,total_orders INT,is_active BOOLEAN)") 
 
cursor.execute("CREATE TABLE Orders (order_id INT AUTO_INCREMENT PRIMARY KEY,customer_id INT,restaurant_id INT,order_date DATETIME,delivery_time DATETIME,status VARCHAR(50),total_amount FLOAT,payment_mode VARCHAR(50),discount_applied FLOAT,feedback_rating FLOAT,FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id))") 
 
cursor.execute("CREATE TABLE Deliveries (delivery_id INT AUTO_INCREMENT PRIMARY KEY,order_id INT,delivery_person_id INT,delivery_status VARCHAR(50),distance FLOAT,delivery_time INT,estimated_time INT,delivery_fee FLOAT,vehicle_type VARCHAR(50),FOREIGN KEY (order_id) REFERENCES Orders(order_id))") 
 
cursor.execute("CREATE TABLE Delivery_Persons (delivery_person_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),contact_number VARCHAR(50),vehicle_type VARCHAR(50),total_deliveries INT,average_rating FLOAT,location TEXT)") 
 
   
# Generate and insert data for Customers 
customers = [ 
    ( 
        fake.name(), 
        fake.email(), 
        fake.phone_number(), 
        fake.address(), 
        fake.date_this_decade(), 
        random.choice([True, False]), 
        random.choice(['Indian', 'Chinese', 'Italian', 'Mexican', 'Thai']), 
        random.randint(1, 50), 
        round(random.uniform(3.0, 5.0), 1) 
    ) 
    for _ in range(100) 
] 
 
cursor.executemany(''' 
INSERT INTO Customers (name, email, phone, location, signup_date, is_premium, 
preferred_cuisine, total_orders, average_rating) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
''', customers) 
 
# Generate and insert data for Restaurants 
restaurants = [ 
    ( 
        fake.company(), 
        random.choice(['Indian', 'Chinese', 'Italian', 'Mexican', 'Thai']), 
        fake.address(), 
        fake.name(), 
        random.randint(20, 60), 
        fake.phone_number(), 
        round(random.uniform(3.0, 5.0), 1), 
        random.randint(100, 1000), 
        random.choice([True, False]) 
    ) 
    for _ in range(50) 
] 
 
cursor.executemany(''' 
INSERT INTO Restaurants (name, cuisine_type, location, owner_name,average_delivery_time, contact_number, rating, total_orders, is_active) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
''', restaurants) 
 
# Generate and insert data for Orders 
orders = [ 
    ( 
        random.randint(1, 100),  # customer_id
        random.randint(1, 20),   # restaurant_id
        (order_date := fake.date_time_this_year()).strftime('%Y-%m-%d %H:%M:%S'),  # order_date
        (order_date + timedelta(hours=random.randint(1, 5), minutes=random.randint(1, 59))).strftime('%Y-%m-%d %H:%M:%S'),  # delivery_time (always after order_date)
        random.choice(['Pending', 'Delivered', 'Cancelled']),  # status
        round(random.uniform(100, 1000), 2),  # total_amount
        random.choice(['Credit Card', 'Cash', 'UPI']),  # payment_mode
        round(random.uniform(0, 30), 2),  # discount_applied
        round(random.uniform(1.0, 5.0), 1)  # feedback_rating
    ) 
    for _ in range(200) 
] 
 
cursor.executemany(''' 
INSERT INTO Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
''', orders)
 
# Generate and insert data for Deliveries 
deliveries = [ 
    ( 
        random.randint(1, 100), 
        random.randint(1, 50), 
        random.choice(['On the way', 'Delivered']), 
        round(random.uniform(1, 20), 2), 
        random.randint(10, 60), 
        random.randint(10, 60), 
        round(random.uniform(20, 100), 2), 
        random.choice(['Bike', 'Car']) 
    ) 
    for _ in range(200) 
] 
 
cursor.executemany(''' 
INSERT INTO Deliveries (order_id, delivery_person_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
''', deliveries) 
 
# Generate and insert data for DeliveryPersons 
delivery_persons = [ 
    ( 
        fake.name(), 
        fake.phone_number(), 
        random.choice(['Bike', 'Car']), 
        random.randint(50, 500), 
        round(random.uniform(3.0, 5.0), 1), 
        fake.address() 
) 
for _ in range(50) 
] 
cursor.executemany(''' 
INSERT INTO Delivery_Persons (name, contact_number, vehicle_type, total_deliveries, average_rating, location) 
VALUES (%s, %s, %s, %s, %s, %s) 
''', delivery_persons) 

# Commit changes and close connection 
db.commit() 
cursor.close() 
db.close() 