create or replace view dwh.total_leaves_per_fiscal_year_by_status as
	select
		sum(leave_days) as total_leaves,
		status,
		fy.start_date::date,
		fy.end_date::date
	from dwh.fact_leaves fl
	join dwh.dim_fiscal_years fy
		on fl.fiscal_id = fy.id
	group by fiscal_id, status, fy.start_date, fy.end_date;
