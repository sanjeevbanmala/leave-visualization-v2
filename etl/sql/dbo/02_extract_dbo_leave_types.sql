INSERT INTO dbo.leave_types 
select 
distinct cast("leaveTypeId" as INT), 
"leaveType",
cast("defaultDays" as INT), 
cast("transferableDays" as INT)  
from dbo.imported_leave_information ili
on conflict (leave_type_id)
do nothing;
