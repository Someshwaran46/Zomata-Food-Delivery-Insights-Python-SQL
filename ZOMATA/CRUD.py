import pymysql
import streamlit as st
from datetime import datetime 

# Connect to MySQL database
class DatabaseConnection:
    def get_connection():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="Zomata"
        )

# General CRUD Operations Class
class CRUDOperations:
    def __init__(self, table_name, columns, id_column):
        self.table_name = table_name
        self.columns = columns
        self.id_column = id_column

    def view_records(self):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM {self.table_name}"
        cursor.execute(query)
        conn.close()
        return cursor

    def create_record(self, values):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {self.table_name} ({', '.join(self.columns)}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def update_record(self, values, record_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        set_clause = ', '.join([f"{col} = %s" for col in self.columns])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {self.id_column} = %s"
        cursor.execute(query, (*values, record_id))
        conn.commit()
        conn.close()

    def delete_record(self, record_id,table_name,id_value):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        
        try: 
            if table_name == "Customers":
            # Set foreign key to NULL in the child tables (Orders)
                cursor.execute("UPDATE Orders SET customer_id = NULL WHERE customer_id = %s", (record_id,))  
        
            elif table_name == "Restaurants":
            # Set foreign key to NULL in the child tables (Orders)
                cursor.execute("UPDATE Orders SET restaurant_id = NULL WHERE restaurant_id = %s", (record_id,))
           
            elif table_name == "Orders":
            # Set foreign key to NULL in the child tables (Deliveries)
                cursor.execute("UPDATE Deliveries SET order_id = NULL WHERE order_id = %s", (record_id,))

            elif table_name == "Deliveries":
            # Set foreign key to NULL in the child tables (Deliveries)
                cursor.execute("UPDATE Deliveries SET delivery_person_id = NULL WHERE delivery_person_id = %s", (record_id,))
        
            elif table_name == "DeliveryPersons":
            # Set foreign key to NULL in the child tables (Deliveries)
                cursor.execute("UPDATE Deliveries SET delivery_person_id = NULL WHERE delivery_person_id = %s", (record_id,))
            
        finally:
            cursor.execute(f"DELETE FROM {table_name} WHERE {id_value} = %s", (record_id,))
        conn.commit()
        conn.close()
def main():
    st.write("""# Zomata Food Delivery Management System""")
    # Choose a table for CRUD operation
    table_choice = st.sidebar.selectbox("Select Table", ("Customers", "Restaurants", "Orders", "Deliveries", "Delivery_Persons"))

    # Table definitions for each table
    table_columns = {
        "Customers": ["name", "email", "phone", "location", "signup_date", "is_premium", "preferred_cuisine", "total_orders", "average_rating"],
        "Restaurants": ["name", "cuisine_type", "location", "owner_name", "average_delivery_time", "contact_number", "rating", "total_orders", "is_active"],
        "Orders": ["customer_id", "restaurant_id", "order_date", "delivery_time", "status", "total_amount", "payment_mode", "discount_applied", "feedback_rating"],
        "Deliveries": ["order_id", "delivery_person_id", "delivery_status", "distance", "delivery_time", "estimated_time", "delivery_fee", "vehicle_type"],
        "Delivery_Persons": ["name", "contact_number", "vehicle_type", "total_deliveries", "average_rating", "location"]
    }

    # Set ID column names for each table (Primary Key)
    id_columns = {
        "Customers": "customer_id",
        "Restaurants": "restaurant_id",
        "Orders": "order_id",
        "Deliveries": "delivery_id",
        "Delivery_Persons": "delivery_person_id"
    }

    # CRUD operation based on table choice
    if table_choice:
        # Create, View, Update, Delete for the chosen table
        option = st.sidebar.radio("Choose operation", ("View", "Create", "Update", "Delete"))
        # Create CRUDOperations object for selected table
        crud = CRUDOperations(table_choice, table_columns[table_choice], id_columns[table_choice])

        # View Records
        if option == "View":
                st.write(f"""### {table_choice} Records are Viewed.""")
                records = crud.view_records()
                st.write(records)
                st.success("Records Fetched Successfully!")

        # Create Record
        elif option == "Create":
            st.write(f"""### Create New Records for {table_choice}""")
            values = []
            for column in table_columns[table_choice]:
                if column in ["signup_date"]:
                    value = st.date_input(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
                elif column == "is_premium" or column == "is_active":
                    value = st.checkbox(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
                elif column in ["rating", "feedback_rating", "average_rating"]:
                    value = st.slider("Enter the rating", min_value=1.0, max_value=5.0,step=0.5,)
                    values.append(value)
                elif table_choice == 'Orders' and column in ["delivery_time","order_date"]:
                    v1=st.date_input(f"Enter {column.replace('_', ' ').title()}")
                    v2=st.time_input(f"Enter {column.replace('_', ' ').title()}",step=1800)
                    v=datetime.combine(v1,v2)
                    values.append(v)
                else:
                    value = st.text_input(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
            if st.button(f"Add {table_choice}"):
                crud.create_record(values)
                st.success(f"{table_choice} added successfully!")

        # Update Record
        elif option == "Update":
            st.write(f"""### Update Records for {table_choice}""")
            record_id = st.number_input(f"Enter {id_columns[table_choice]} to Update", min_value=1)
            values = []
            for column in table_columns[table_choice]:
                if column in ["signup_date"]:
                    value = st.date_input(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
                elif column == "is_premium" or column == "is_active":
                    value = st.checkbox(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
                elif column in ["rating", "feedback_rating", "average_rating"]:
                    value = st.slider("Enter the rating", min_value=1.0, max_value=5.0,step=0.5)
                    values.append(value)
                elif table_choice == 'Orders' and column in ["delivery_time","order_date"]:
                    v1=st.date_input(f"Enter {column.replace('_', ' ').title()}")
                    v2=st.time_input(f"Enter {column.replace('_', ' ').title()}",step=1800)
                    v=datetime.combine(v1,v2)
                    values.append(v)
                else:
                    value = st.text_input(f"Enter {column.replace('_', ' ').title()}")
                    values.append(value)
            if st.button(f"Update {table_choice}"):
                crud.update_record(values, record_id)
                st.success(f"{table_choice} updated successfully!")

        # Delete Record
        elif option == "Delete":
            st.write(f"""### Deleting records under {table_choice}""")
            record_id = st.number_input(f"Enter {id_columns[table_choice]} to Delete", min_value=1)
            if st.button(f"Delete {table_choice}"):
                id_value=(f"{id_columns[table_choice]}")
                crud.delete_record(record_id,table_choice,id_value)
                st.success(f"{table_choice} deleted successfully!")
if __name__ == "__main__":
    main()


