Insert into dbo.fiscal_year 
SELECT 
DISTINCT cast("fiscalId" as INT), 
cast("fiscalStartDate" as date),
cast("fiscalEndDate" as date)  
from dbo.imported_leave_information ili
on conflict (fiscal_id)
do nothing;
