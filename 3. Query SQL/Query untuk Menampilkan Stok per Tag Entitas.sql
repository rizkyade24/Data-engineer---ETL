SELECT 
    et.tag_name,
    SUM(fs.qty) AS total_stock
FROM 
    fact_stock fs
JOIN 
    dim_entity de ON fs.entity_id = de.entity_id
JOIN 
    entity_has_master_material ehmm ON de.entity_id = ehmm.entity_id
JOIN 
    entity_tags et ON ehmm.tag_id = et.tag_id
GROUP BY 
    et.tag_name;
