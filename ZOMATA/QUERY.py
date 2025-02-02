import streamlit as st
import pymysql

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='Zomata',
        cursorclass=pymysql.cursors.DictCursor
    )
   
def main():
    # Query execution function
    def execute_query(query):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                st.write(cursor)
        finally:
            connection.close()

    # Streamlit UI
    st.title("Food Delivery Platform Insights")

    # Dropdown to select queries
    query_options = ["Top 5 Customers by Orders",
"Customers with Premium Membership",
"Customer who Gave the Highest Ratings",
"List of Active Restaurants",
"Top 5 Highest Rated Restaurants",
"Restaurants with Over 100 Orders",
"Restaurants Offering the Fastest Delivery",
"Total Revenue Per Restaurant",
"Total Revenue from Orders",
"Total Number of Orders Delivered",
"Total Number of Canceled Orders",
"Most Popular Cuisine",
"Total Orders per Cuisine Type",
"Top 3 Locations with the Most Orders",
"Orders above 20 % Discounts Applied",
"Orders Taking Longer Than Estimated Time",
"Percentage of Orders Paid by Credit Card",
"Most Used Payment Mode",
"Delivery Persons with the Best Ratings",
"Delivery Persons Who Completed Over 50 Deliveries"]

    query_selection = st.selectbox("Select a Query", query_options)

    # Query mapping
    database_queries = {"Top 5 Customers by Orders": "SELECT name, total_orders FROM Customers ORDER BY total_orders DESC LIMIT 5;",
    "Customers with Premium Membership": "SELECT name FROM Customers WHERE is_premium = 1;",
    "Customer who Gave the Highest Ratings": "SELECT name FROM Customers ORDER BY average_rating DESC LIMIT 1;",
    "List of Active Restaurants": "SELECT name FROM Restaurants WHERE is_active = 1;",
    "Top 5 Highest Rated Restaurants": "SELECT name, rating FROM Restaurants ORDER BY rating DESC LIMIT 5;",
    "Restaurants with Over 100 Orders": "SELECT name FROM Restaurants WHERE total_orders > 100;",
    "Total Revenue Per Restaurant":"SELECT Restaurants.name, SUM(Orders.total_amount) AS total_revenue FROM Orders JOIN Restaurants ON Orders.restaurant_id = Restaurants.restaurant_id GROUP BY Restaurants.restaurant_id; ",
    "Total Revenue from Orders": "SELECT SUM(total_amount) AS total_revenue FROM Orders;",
    "Total Number of Orders Delivered": "SELECT COUNT(*) AS total_deliveries FROM Deliveries WHERE delivery_status = 'Delivered';",
    "Total Number of Canceled Orders": "SELECT COUNT(*) AS canceled_orders FROM Orders WHERE status = 'Cancelled';",
    "Most Popular Cuisine": "SELECT cuisine_type, COUNT(*) AS order_count FROM Restaurants JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id GROUP BY cuisine_type ORDER BY order_count DESC LIMIT 1;",
    "Total Orders per Cuisine Type":"SELECT cuisine_type, COUNT(*) AS total_orders FROM Restaurants JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id GROUP BY cuisine_type; ",
    "Top 3 Location with the Most Orders":"SELECT location, COUNT(*) AS total_orders FROM Orders JOIN Restaurants ON Orders.restaurant_id = Restaurants.restaurant_id GROUP BY location ORDER BY total_orders DESC LIMIT 3; ",
    "Delivery Persons Who Completed Over 50 Deliveries": "SELECT name FROM Delivery_Persons WHERE total_deliveries > 50;",
    "Orders above 20 % Discounts Applied":"SELECT * FROM Orders WHERE discount_applied > 20;",
    "Restaurants Offering the Fastest Delivery": "SELECT name, average_delivery_time FROM Restaurants ORDER BY average_delivery_time ASC LIMIT 5;",
    "Percentage of Orders Paid by Credit Card": "SELECT (COUNT(*) / (SELECT COUNT(*) FROM Orders) * 100) AS credit_card_percentage FROM Orders WHERE payment_mode = 'Credit Card';",
    "Delivery Persons with the Best Ratings": "SELECT name, average_rating FROM Delivery_Persons ORDER BY average_rating DESC LIMIT 5;",
    "Most Used Payment Mode": "SELECT payment_mode, COUNT(*) AS usage_count FROM Orders GROUP BY payment_mode ORDER BY usage_count DESC LIMIT 1;",
    "Orders Taking Longer Than Estimated Time": "SELECT * FROM Deliveries WHERE delivery_time > estimated_time;",
    "Restaurants with Below Average Ratings": "SELECT name, rating FROM Restaurants WHERE rating < (SELECT AVG(rating) FROM Restaurants);"}

    if query_selection in database_queries:
        Show=st.button("Proceed")
        if Show:
            query_result = execute_query(database_queries[query_selection])
        

if __name__ == "__main__":
    main()