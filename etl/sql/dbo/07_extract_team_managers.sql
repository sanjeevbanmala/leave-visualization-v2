insert into dbo.team_managers(team_manager_id) 
select distinct cast("teamManagerId" as INT)
from dbo.imported_leave_information ili
where cast("teamManagerId" as INT) is not null
on conflict (team_manager_id)
do nothing;
