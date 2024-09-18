-- Case 1: selecting distinct leave issuers whose default leave issuer id and current leave issuer id are same
insert into dbo.leave_issuer 
select distinct
cast("currentLeaveIssuerId" as INT), 
"issuerFirstName", 
"issuerLastName", 
"currentLeaveIssuerEmail" 
from dbo.imported_leave_information ili
where cast("currentLeaveIssuerId" as INT)= cast("leaveIssuerId"  as INT)
on conflict (leave_issuer_id)
do nothing;
-- CASE 2: Selecting distinct default leave issuers who are not the current leave issuers
insert into dbo.leave_issuer 
select distinct
cast(ili."leaveIssuerId" as int), 
ili."issuerFirstName", 
ili."issuerLastName", 
ili2."currentLeaveIssuerEmail" 
from dbo.imported_leave_information ili
left join raw.imported_leave_information ili2 
on ili."leaveIssuerId"= ili2."currentLeaveIssuerId" 
where ili."leaveIssuerId" <> ili."currentLeaveIssuerId"
on conflict (leave_issuer_id)
do nothing;
-- CASE 3 : Selecting distinct current leave issuers who are not the default leave issuers 
insert into dbo.leave_issuer(leave_issuer_id,email)
select distinct
cast(ili."currentLeaveIssuerId" as int),
ili."currentLeaveIssuerEmail" 
from dbo.imported_leave_information ili
where ili."leaveIssuerId" <> ili."currentLeaveIssuerId"
on conflict (leave_issuer_id)
do nothing;

insert into dbo.leave_issuer
values(000,null, null,null)
on conflict (leave_issuer_id)
do nothing; 
