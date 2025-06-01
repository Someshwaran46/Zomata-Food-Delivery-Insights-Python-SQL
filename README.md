# 🍽️ ZOMATA – Food Delivery Data Insights with Python & SQL

Deliver smarter with **ZOMATA** – a fully interactive data analytics platform for the food delivery ecosystem. This project helps you analyze, optimize, and visualize restaurant, customer, order, and delivery data using **Python**, **SQL**, and **Streamlit**.

Whether you're an aspiring data engineer or a business looking to boost delivery performance, this tool lets you manage and analyze everything — from fake data generation to real-time interactive insights.

---

## 🚀 What This Project Does

- ✅ Generate realistic food delivery datasets using `Faker`
- ✅ Normalize and store data in a MySQL database
- ✅ Perform full **CRUD** operations
- ✅ Run insightful SQL queries for real-world KPIs
- ✅ Visualize results with an interactive **Streamlit UI**
- ✅ Build a modular and scalable Python backend using **OOP principles**

---

## 📂 Project Structure

```bash
ZOMATA/
├── CRUD.py                  # All database Create, Read, Update, Delete operations
├── dataset_creation.py     # Generates synthetic data & builds MySQL tables
├── HOME.py                 # Streamlit landing page with project overview
├── QUERY.py                # Executes SQL queries and displays visual insights
├── TITLE.py                # Main navigation hub to access all Streamlit pages
└── /image
    └── Gemini_Generated_Image.jpeg  # Used on the homepage
```
---
## 🌟 Features

-  🔄 Dynamic CRUD operations across multiple entities
-  📊 Analytical SQL queries to understand trends in orders, delivery times & customer behavior
-  🧱 Modular OOP-based Python code
-  ⚡ Streamlit Web App – responsive, intuitive, and beginner-friendly
-  🔧 Schema-flexible database design
  
---
## 🛠️ Technologies Used

- Python 3.x
- MySQL
- Faker – to generate realistic data
- Streamlit – for the UI
- pymysql – to connect Python with MySQL
  
---
## Install all required libraries:

```bash
pip install streamlit faker pymysql
```
### 🧑‍💻 Clone and Run the Project

#### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/Someshwaran46/Zomata-Food-Delivery-Insights-Python-SQL.git
cd Zomata-Food-Delivery-Insights-Python-SQL
```
#### Step 2: Set Up the Database
Create synthetic data and build the MySQL tables:

```bash
python ZOMATA/dataset_creation.py
```
Make sure your MySQL server is running and credentials in the script are updated (default: root/root).

#### Step 3: Launch the Web App
Run the Streamlit dashboard:

```bash
streamlit run ZOMATA/TITLE.py
```

#### Step 4: Use the App
Once running, your default browser opens automatically with 3 navigation buttons:

- 🏠 Home: Overview of the project
- 🧾 CRUD: Perform Create, Read, Update, Delete operations
- 🔍 Query: Get answers to predefined business questions

---
### 💼 Use Cases

- Track & manage food delivery logistics
- Identify top-performing restaurants
- Optimize delivery efficiency
- Improve customer satisfaction
- Learn key data engineering & visualization concepts hands-on

---
### 🎓 Perfect For

- Data Science & Engineering Learners
- Analytics Enthusiasts
- Product & Ops Teams
- SQL + Python Developers

---

## 📬 Feedback

- Feel free to open issues or submit pull requests! Improvements, and suggestions are always welcome 🙌
- For clarifications drop an email to somesh4602@gmail.com.

---
