insert into dbo.employee_leaves 
select cast(id as int),
case 
	when ("leaveIssuerId" is null and "currentLeaveIssuerId" is null)
	then 000
	when "leaveIssuerId" <> "currentLeaveIssuerId"
	then cast("currentLeaveIssuerId" as INT)
	when "leaveIssuerId" is null
	then "currentLeaveIssuerId"
	else cast("leaveIssuerId" as INt)
end,
cast("leaveTypeId" as int),
cast("empId" as InT),
cast("fiscalId" as int),
cast("leaveDays" as int),
reason,
status,
"responseRemarks",
cast ("isConsecutive" as boolean),
cast("startDate" as date),
cast("endDate" as date),
cast("createdAt" as timestamp),
cast("updatedAt" as timestamp) 
from dbo.imported_leave_information ili
on conflict (leave_id)
do nothing;
