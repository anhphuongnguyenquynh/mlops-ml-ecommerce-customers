from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
import pandas as pd
# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 7),
}

# Function to read the CSV and generate insert queries
def generate_insert_queries():
    CSV_FILE_PATH = 'sample_files/olist_customers_dataset.csv'
    # Read the CSV file
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Create a list of SQL insert queries
    insert_queries = []
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO olist_customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state) VALUES ({row['customer_id']}, '{row['customer_unique_id']}', {row['customer_zip_code_prefix']}, {row['customer_city']}, {row['customer_state']} );"
        insert_queries.append(insert_query)
    
    # Save queries to a file for the PostgresOperator to execute
    with open('./dags/sql/insert_queries.sql', 'w') as f:
        for query in insert_queries:
            f.write(f"{query}\n")


# Define the DAG
with DAG('csv_to_postgres_dag',
         default_args=default_args,
         schedule_interval='@once',
         catchup=False) as dag:

    # Task to create a PostgreSQL table
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='write_to_psql',  # Replace with your connection ID
        sql="""
        DROP TABLE IF EXISTS olist_customers;
        CREATE TABLE olist_customers (
            id SERIAL PRIMARY KEY,
            customer_id VARCHAR(100),
            customer_unique_id VARCHAR(100),
            customer_zip_code_prefix VARCHAR(100),
            customer_city VARCHAR(100),
            customer_state CHAR(2)
        );
        """
    )
    generate_queries = PythonOperator(
    task_id='generate_insert_queries',
    python_callable=generate_insert_queries
    )

    # Task to run the generated SQL queries using PostgresOperator
    run_insert_queries = PostgresOperator(
        task_id='run_insert_queries',
        postgres_conn_id='write_to_psql',  # Define this connection in Airflow UI
        sql='sql/insert_queries.sql'
    )
    create_table>>generate_queries>>run_insert_queries
    # Other tasks can follow here