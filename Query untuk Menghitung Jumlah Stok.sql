SELECT 
    SUM(fs.qty) AS total_stock
FROM 
    fact_stock fs
JOIN 
    dim_material dm ON fs.material_id = dm.material_id;
