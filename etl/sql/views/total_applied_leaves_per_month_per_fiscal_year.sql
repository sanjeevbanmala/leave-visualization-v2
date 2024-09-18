create or replace view dwh.total_applied_leaves_per_month_per_fiscal_year as
	with applied_leaves as (
		select
			leave_days,
			to_char(start_date, 'Month') as start_month,
			fiscal_id
		from dwh.fact_leaves
	)
	select
		sum(leave_days) as total_applied_leaves,
		start_month,
		to_char(start_date, 'Mon DD, YYYY') as fiscal_year_start
	from applied_leaves al
	join dwh.dim_fiscal_years fy
		on fy.id = al.fiscal_id
	group by start_month, fy.start_date
	order by total_applied_leaves desc;
