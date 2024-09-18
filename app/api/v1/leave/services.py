from psycopg2 import DatabaseError
from database import get_conn, put_conn
from api.sql_utils import read_sql_query
from psycopg2.extras import RealDictCursor

def execute_sql_query(query, **kwargs):
    #For get request in future use
    # leave_type = kwargs.get('leave_type')
    # department = kwargs.get('department')
    # start_date = kwargs.get('start_date')
    # end_date = kwargs.get('end_date')
    fiscal_year = kwargs.get('fiscal_year')
    query, bind_params = read_sql_query(query,
                                        # For get request in future use
                                        # leave_type=leave_type,
                                        # department=department,
                                        # start_date=start_date,
                                        # end_date=end_date,
                                        # fiscal_year=fiscal_year
                                        )
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor(cursor_factory = RealDictCursor)
        cursor.execute(query, bind_params)
        leaves_per_week_day = cursor.fetchall()
        return leaves_per_week_day
    except DatabaseError as e:
        print(f"Database error occurred: {e}")
        raise
    finally:
        if conn:
            put_conn(conn)
