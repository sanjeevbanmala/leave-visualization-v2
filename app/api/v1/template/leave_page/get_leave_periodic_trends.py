LEAVE_PERIODIC_TRENDS="""
SELECT
    el.leave_days,
    lt.leave_type,
    TO_CHAR(created_at, 'YYYY') AS year,
    TO_CHAR(created_at, 'Mon') AS hmonth,
    TO_CHAR(created_at, 'DY') AS day
FROM dbo.employee_leaves AS el
INNER JOIN dbo.leave_types AS lt ON el.leave_type_id = lt.leave_type_id;
"""
