FISCAL_YEAR_OPTIONS = """
                select distinct
    LEFT(CAST(fy.start_date AS VARCHAR), 7)
    || '/'
    || LEFT(CAST(fy.end_date AS VARCHAR), 7) AS fiscal_date
FROM dbo.employee_leaves AS el
INNER JOIN dbo.fiscal_year AS fy ON el.fiscal_id = fy.fiscal_id;
            """

DEPARTMENT_OPTIONS="""
select 
distinct department_name 
from dbo.departments;
"""

DESIGNATION_OPTIONS="""
select 
distinct designation_name
from dbo.designations;
"""

LEAVE_TYPE_OPTIONS="""
select 
distinct leave_type
from dbo.leave_types lt; 
"""