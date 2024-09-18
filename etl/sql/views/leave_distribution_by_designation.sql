create or replace view dwh.leave_distribution_by_designation as
	select
	  	sum(fl.leave_days) as total_leaves,
	  	d.name as designation,
		to_char(fy.start_date, 'Mon DD, YYYY') as fiscal_year_start
	from dwh.fact_leaves fl
	join dwh.dim_designations d
	  	on fl.designation_id = d.id
	join dwh.dim_fiscal_years fy
		on fl.fiscal_id = fy.id
	group by d.name, fy.start_date;
