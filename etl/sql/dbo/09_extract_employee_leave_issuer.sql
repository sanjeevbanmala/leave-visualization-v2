insert  into dbo.employee_leave_issuer 
select distinct cast("empId" as INT),cast("currentLeaveIssuerId" as INT), true as is_current_leave_issuer 
from dbo.imported_leave_information ili 
where "leaveIssuerId" = "currentLeaveIssuerId"
union 
select distinct cast("empId" as INT),cast("leaveIssuerId" as INT), false as is_current_leave_issuer 
from dbo.imported_leave_information ili 
where "leaveIssuerId" <> "currentLeaveIssuerId"
union
select distinct cast("empId" as INT),cast("currentLeaveIssuerId" as INT), true as is_current_leave_issuer 
from dbo.imported_leave_information ili 
where "leaveIssuerId" <> "currentLeaveIssuerId"
on conflict (employee_id, leave_issuer_id)
do nothing;
