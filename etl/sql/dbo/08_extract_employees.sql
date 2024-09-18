insert into dbo.employees 
select distinct cast(ili."empId" as INT), ili."firstName", ili."middleName", ili."lastName", ili.email, cast(ili."isHr" as boolean), cast(ili."isSupervisor" as boolean),cast(ili."designationId" as INT), cast(ili."teamManagerId" as INT), d.department_id  
from dbo.imported_leave_information ili 
inner join dbo.departments d  on d.department_name= ili."departmentDescription"
on conflict (employee_id)
do nothing;
