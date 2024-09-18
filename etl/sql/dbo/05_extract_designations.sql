insert into dbo.designations 
select distinct cast("designationId" as INT),"designationName"  
from dbo.imported_leave_information ili
on conflict (designation_id)
do nothing;
