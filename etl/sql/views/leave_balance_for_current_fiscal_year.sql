create or replace view dwh.leave_balance_for_current_fiscal_year as
    with taken_leaves as (
        select
            employee_id, 
            sum(leave_days) as total_taken_leaves,
            fl.leave_type_id
        from dwh.fact_leaves fl
        join dwh.dim_fiscal_years fy
            on fl.fiscal_id = fy.id
            and fl.status = 'APPROVED'
            and fy.is_current is true
        group by employee_id, fl.leave_type_id
    ), remaining_leaves as (
        select
            employee_id,
            total_taken_leaves, 
            lt.name as leave_type,
            case default_days
                when 0 then 0
                else default_days - total_taken_leaves
            end as remaining_leaves
        from taken_leaves tl
        join dwh.dim_leave_types lt
            on tl.leave_type_id = lt.id
    )
    select
        e.email,
        rl.*
    from remaining_leaves rl
    join dwh.dim_employees e 
        on rl.employee_id = e.user_id;
