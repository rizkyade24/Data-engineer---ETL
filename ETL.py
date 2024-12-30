from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to database
def get_db_connection():
    return mysql.connector.connect(
        host="10.10.0.30",
        port=3306,
        user="devel",
        password="recruitment2024",
        database="recruitment_dev"
    )

# Extract Data
def extract_data(**kwargs):
    try:
        conn = get_db_connection()
        queries = {
            "stocks": "SELECT * FROM stocks",
            "materials": "SELECT * FROM master_materials",
            "entities": "SELECT * FROM entities",
            "batches": "SELECT * FROM batches",
            "provinces": "SELECT * FROM provinces",
            "regencies": "SELECT * FROM regencies",
            "material_entity": "SELECT * FROM material_entity",
            "entity_has_master_materials": "SELECT * FROM entity_has_master_materials"
            ""
        }
        extracted_data = {key: pd.read_sql(query, conn) for key, query in queries.items()}
        conn.close()
        logger.info("Data extracted successfully.")
        return extracted_data
    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        raise

# Transform Data
def transform_data(ti, **kwargs):
    extracted_data = ti.xcom_pull(task_ids="extract_data")
    stocks = extracted_data['stocks']
    materials = extracted_data['materials']
    entities = extracted_data['entities']
    batches = extracted_data['batches']
    provinces = extracted_data['provinces']
    regencies = extracted_data['regencies']
    material_entity = extracted_data['material_entity']
    entity_has_master_materials = extracted_data['entity_has_master_materials']


    if not extracted_data or not isinstance(extracted_data, dict):
        raise ValueError("Extracted data is missing or malformed.")


    # Dimensional Tables Rename
    
    ## Dimensional Date
    dim_date = stocks[['created_at']].drop_duplicates()
    dim_date['date_id'] = range(1, len(dim_date) + 1)
    dim_date['year'] = dim_date['created_at'].dt.year
    dim_date['month'] = dim_date['created_at'].dt.month
    dim_date['quarter'] = dim_date['created_at'].dt.quarter

    ## Dimensional Location
    dim_location = provinces.merge(regencies, 
        left_on="id", 
        right_on="province_id", 
        how="left"
    )

    ## Dimensional materials
    dim_materials = materials[['id', 'name', 'unit_of_distribution', 'pieces_per_unit', 'temperature_sensitive', 'temperature_min', 'temperature_max', 'is_vaccine', 'bpom_code', 'description']].rename(columns={
        "id": "material_id",
        "name": "material_name"
    })

    ## Dimensional entities
    dim_entities = entities[['id', 'name', 'type', 'address', 'province_id', 'regency_id', 'status']].rename(columns={ 
        "id": "entity_id",
        "name": "entity_name",
        "type": "entity_type"
    })

    ## Dimensional batch
    dim_batches = batches[['id', 'batch_code', 'expiry_date', 'production_date', 'manufacture_id', 'status']].rename(columns={
        "id": "batch_id"
    })

    # Fact Table
    # Dim master material
    fact_stock = stocks.merge(material_entity, left_on="material_entity_id", right_on="id", how="left")
    fact_stock = fact_stock.merge(dim_materials, left_on="material_id", right_on="material_id", how="left")

    # Dim entities
    fact_stock = fact_stock.merge(entity_has_master_materials, left_on="entity_has_material_id", right_on="id", how="left")
    fact_stock = fact_stock.merge(dim_entities, left_on="entity_id", right_on="entity_id", how="left")

    # Dim Location
    fact_stock = fact_stock.merge(dim_location, left_on="regency_id", right_on="regency_id", how="left")

    # Dim Date
    fact_stock = fact_stock.merge(dim_date, left_on="created_at", right_on="date", how="left")

    # Dim batch
    fact_stock = fact_stock.merge(dim_batches, left_on="batch_id", right_on="batch_id", how="left")

    fact_stock = fact_stock[[
        'id', 'batch_id', 'material_id', 'entity_id', 'location_id', 'date_id', 'qty', 'price'
    ]].rename(columns={'id': 'fact_id'})

    return dim_date, dim_location, dim_materials, dim_entities, dim_batch, fact_stock

# Load Data
def load_data(**kwargs):
    conn = get_db_connection()
    cursor = conn.cursor()
        
    # Start transaction
    cursor.execute("START TRANSACTION")

    # Get transformed data
    dim_date, dim_location, dim_materials, dim_entities, dim_batches, fact_stock = ti.xcom_pull(task_ids="transform_data")
    
    engine = create_engine("mysql+mysqlconnector://devel:recruitment2024@10.10.0.30:3306/recruitment_dev")

    # Load dimensional tables
    dim_date.to_sql('dim_date', engine, if_exists='replace', index=False)
    dim_location.to_sql('dim_location', engine, if_exists='replace', index=False)
    dim_materials.to_sql('dim_materials', engine, if_exists='replace', index=False)
    dim_entities.to_sql('dim_entities', engine, if_exists='replace', index=False)
    dim_batches.to_sql('dim_batches', engine, if_exists='replace', index=False)

    # Load fact table
    fact_stock.to_sql('fact_stock', engine, if_exists='replace', index=False)

    conn.close()

# Define DAG
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email_on_retry": False,
    "depends_on_past": False
}

with DAG(
    dag_id="etl_dimensional_modeling",
    default_args=default_args,
    start_date=datetime(2023, 12, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
        provide_context=True,
    )

    extract_task >> transform_task >> load_task
