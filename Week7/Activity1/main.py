  
from Services import UserService, OrderService
from database import create_database_tables
from Services import UserService_singleton, OrderService_singleton
import time

def main():
    print("Starting application...")

    create_database_tables()
    user_service = UserService()
    order_service = OrderService()

    # Insert sample data
    user_service.insert_user(1, 'Alice')
    order_service.insert_order(101, 1, 'Laptop')
    user_service.insert_user(2, 'Bob')
    order_service.insert_order(102, 2, 'Smartphone')
    user_service.insert_user(3, 'Charlie')
    order_service.insert_order(103, 3, 'Tablet')
    user_service.insert_user(4, 'Diana')
    order_service.insert_order(104, 4, 'Monitor')   
    user_service.insert_user(5, 'Eve')
    order_service.insert_order(105, 5, 'Keyboard')
    print("Sample data inserted.")

    # Fetch and display data
    print("\nFetching data using non-singleton services...")
    user_id = 1
    start_time = time.time_ns()
    user = user_service.get_user(user_id)
    orders = order_service.get_orders(user_id)
    end_time = time.time_ns()
    print(f"Data fetched in {(end_time - start_time) / 1_000_000} milliseconds")

    print("User:", user)
    print("Orders:", orders)


    ## Using singleton services

    print("\nFetching data using singleton services...")

    user_service_singleton = UserService_singleton()
    order_service_singleton = OrderService_singleton()
    user_id = 1
    start_time = time.time_ns()

    user = user_service_singleton.get_user(user_id)
    orders = order_service_singleton.get_orders(user_id)
    end_time = time.time_ns()
    print(f"Data fetched in {(end_time - start_time) / 1_000_000} milliseconds")

    print("User:", user)
    print("Orders:", orders)

if __name__ == "__main__":
    main()
