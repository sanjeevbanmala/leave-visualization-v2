INSERT INTO dbo.employee_allocations(employee_id, allocation_id)
SELECT 
distinct
    cast("empId" as INT),
    (data->>'id')::INT AS allocation_id
FROM (
    select "empId",json_array_elements(allocations) AS data
    FROM dbo.imported_leave_information 
) AS allocations
on conflict (employee_id, allocation_id)
do nothing;
