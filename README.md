# Zomata - Food Delivery Data Insights Using Python and SQL

This project focuses on analyzing food delivery data to enhance operational efficiency and customer satisfaction. Using SQL, Python, and Streamlit, we develop an interactive tool for managing orders, customers, restaurants, and deliveries. The tool supports dynamic schema changes and robust database operations. By generating synthetic datasets with Python's Faker library, we build a relational database with normalized tables. Key use cases include order management, customer analytics, delivery optimization, and restaurant insights. The project emphasizes object-oriented programming (OOP) principles for modular, scalable code. SQL queries extract valuable insights, which are visualized in a user-friendly Streamlit app. Learners will gain practical experience in data engineering, database management, and data analysis. This project helps businesses optimize delivery operations and improve customer experience.
# Overview

This repository contains a comprehensive project for food delivery data analysis using Python, SQL, and Streamlit. The goal of this project is to enhance operational efficiency and customer satisfaction by analyzing food delivery data. It allows dynamic management of orders, customers, restaurants, and deliveries, and provides insightful visualizations.

## Project Structure:

- **/ZOMATA/CRUD.py**  
  Contains CRUD (Create, Read, Update, Delete) operations for managing the database.

- **/ZOMATA/dataset_creation.py**  
  Generates synthetic datasets using Faker and creates the necessary tables in a MySQL database.

- **/ZOMATA/HOME.py**  
  Introduction page that provides an overview of the project and its purpose.

- **/ZOMATA/image/Gemini_Generated_Image_txgo0ytxgo0ytxgo.jpeg**  
  Folder containing the image used in the HOME.py page for project visualization.

- **/ZOMATA/QUERY.py**  
  Contains SQL queries that interact with the database, fetching and displaying data based on specific analysis criteria.

- **/ZOMATA/TITLE.py**  
  Main page that serves as a navigation hub to access the Home, CRUD, and Query pages.

## Features:
- **Database Management:** Create and modify database tables using dynamic SQL operations.
- **Data Insights:** Visualize and analyze data trends in customer orders, delivery times, and restaurant popularity.
- **Streamlit Interface:** Interactive web interface for easy navigation and user engagement.

## Requirements:
- Python 3.x
- MySQL
- Required libraries: Faker, Streamlit, pymysql

## Steps to Run the Web Application
### Step 1: Creating the Database
- To analyze and perform CRUD operations and data analysis, the database must be created. You can generate the necessary datasets by running:
python /ZOMATA/dataset_creation.py
### Step 2: Running the Web Application
- To launch the web application, execute the following command:
streamlit run <path_to_/ZOMATA/TITLE.py>
- This will run the main file (TITLE.py), which calls other pages like Home, CRUD, and Query. The application is built using Streamlit.

### Step 3: Accessing the UI
Once the program is executed, your default web browser will open automatically, displaying the UI of the application. You will see three radio buttons:

- Home: Displays generic details about the product.
- CRUD: Allows CRUD operations on the dataset.
- Query: Provides answers to predefined questions based on the data.
