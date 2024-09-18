INSERT INTO dbo.allocations
SELECT 
distinct
    (data->>'id')::INT AS allocation_id,
    data->>'name' AS name,
    data->>'type' AS type
FROM (
    select json_array_elements(allocations) AS data
    FROM dbo.imported_leave_information 
) AS allocations
on conflict (allocation_id)
do nothing;
