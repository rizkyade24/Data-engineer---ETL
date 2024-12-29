## Design Datamart
link: https://drive.google.com/file/d/1g_PkzG_xIb1B7gGzv5HyEyem0kU_0aah/view?usp=sharing

![Dashboard2 drawio](https://github.com/user-attachments/assets/7388977c-ae61-4c70-917e-07ce8f7e1697)

# ETL Process Documentation
This project implements an ETL (Extract, Transform, Load) process using Astro Airflow CLI to build a dimensional data model.

### 1. Data Sources (Extract Phase)
Data is extracted from the following MySQL tables:

- stocks: Contains stock data.
- master_materials: Details about materials.
- entities: Information on entities.
- batches: Batch production details.
- provinces and regencies: Location hierarchy data.
- material_entity: Material-entity mapping.
- entity_has_master_materials: Entity-material relationships.


