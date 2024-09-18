import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.environ.get("FLASK_API_ENDPOINT")
LEAVE_TRENDS_ENDPOINT = f"{API_BASE_URL}/leave/leave-trends"
LEAVE_PERIODIC_TRENDS_ENDPOINT = f"{API_BASE_URL}/leave/leave-periodic-trends"
LEAVE_ALLOCATION_DETAILS_ENDPOINT = f"{API_BASE_URL}/leave/allocation-details"
LEAVE_EMPLOYEE_DETAILS_ENDPOINT = f"{API_BASE_URL}/leave/employee-details"
LEAVE_BALANCE_ENDPOINT = f"{API_BASE_URL}/leave/leave-balance"
