LEAVE_TRENDS="""
SELECT
    e.employee_id,
    e.first_name AS employee_first_name,
    d.designation_name AS employee_designation,
    d2.department_name AS employee_department,
    el.leave_days,
    lt.leave_type,
    LEFT(CAST(fy.start_date AS VARCHAR), 4)
    || '/'
    || LEFT(CAST(fy.end_date AS VARCHAR), 4) AS fiscal_date,
    TO_CHAR(created_at, 'MonDD') AS month,
    TO_CHAR(created_at, 'MM') AS month_number
FROM dbo.employee_leaves AS el
INNER JOIN dbo.employees AS e ON el.employee_id = e.employee_id
INNER JOIN dbo.designations AS d ON e.designation_id = d.designation_id
INNER JOIN dbo.leave_types AS lt ON el.leave_type_id = lt.leave_type_id
INNER JOIN dbo.departments AS d2 ON e.department_id = d2.department_id
INNER JOIN dbo.fiscal_year AS fy ON el.fiscal_id = fy.fiscal_id;
"""
