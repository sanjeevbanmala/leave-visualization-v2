insert into dbo.departments(department_name)  
select distinct "departmentDescription"
from dbo.imported_leave_information ili
on conflict (department_name)
do nothing;
