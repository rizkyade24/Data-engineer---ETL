# ETL Process Documentation
This project implements an ETL (Extract, Transform, Load) process using Astro Airflow CLI to build a dimensional data model. Below is a detailed explanation of the flow:

## Overview
The ETL process automates data extraction, transformation, and loading into a MySQL database. The primary goal is to prepare dimensional tables and a fact table for analytics.

### 1. Data Sources (Extract Phase)
Data is extracted from the following MySQL tables:

- **stocks**: Contains stock data.
- **master_materials**: Details about materials.
- **entities**: Information on entities.
- **batches**: Batch production details.
- **provinces and regencies**: Location hierarchy data.
- **material_entity**: Material-entity mapping.
- **entity_has_master_materials**: Entity-material relationships.
  
  
### 2. Transformations (Transform Phase)
During the transformation phase, raw data is processed into dimensional tables and a fact table:

#### Dimensional Tables
- **dim_date**: Extracts date components (year, month, quarter) from created_at timestamps.
- **dim_location**: Merges provinces and regencies to form a location hierarchy.
- **dim_materials**: Contains material details such as name, unit, and specifications.
- **dim_entities**: Includes entity-specific details such as name, type, and location.
- **dim_batches**: Stores batch details, including production and expiry dates.
  
#### Fact Table
- **fact_stock**: Central table combining all dimensions and stock data. It includes:
fact_id, batch_id, material_id, entity_id, location_id, date_id
Stock quantity (qty) and price (price).
Transformations include merging, renaming columns, and mapping relationships between tables.


## 3. Destination Tables (Load Phase)
The transformed data is loaded into the following tables in the MySQL database:

- dim_date
- dim_location
- dim_materials
- dim_entities
- dim_batches
- fact_stock
The tables are created or replaced in the database for each DAG run.

## Airflow DAG
The ETL process is orchestrated by an Airflow DAG with three tasks:

- **extract_data**: Connects to the database and extracts raw data.
- **transform_data**: Processes the data into dimensional and fact tables.
- **load_data**: Loads the processed data into the destination tables.
