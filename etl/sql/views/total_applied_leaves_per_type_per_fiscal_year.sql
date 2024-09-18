create or replace view dwh.total_applied_leaves_per_type_per_fiscal_year as
	with applied_leaves as (
		select
			sum(leave_days) as total_applied_leaves,
			leave_type_id,
			status,
			fiscal_id
		from dwh.fact_leaves
		group by fiscal_id, leave_type_id, status
		order by fiscal_id
	)
	select
		lt.name as leave_type,
		status,
		al.total_applied_leaves,
		to_char(start_date, 'Mon DD, YYYY') as fiscal_year_start,
		to_char(end_date, 'Mon DD, YYYY') as fiscal_year_end
	from applied_leaves al
	join dwh.dim_leave_types lt
		on al.leave_type_id = lt.id
	join dwh.dim_fiscal_years fy	
		on al.fiscal_id = fy.id;
