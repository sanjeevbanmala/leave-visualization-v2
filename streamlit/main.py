from api_call import fetch_data
from constants import LEAVE_EMPLOYEE_DETAILS_ENDPOINT, LEAVE_ALLOCATION_DETAILS_ENDPOINT, LEAVE_BALANCE_ENDPOINT
import pandas as pd

alloc_data=fetch_data(LEAVE_ALLOCATION_DETAILS_ENDPOINT)
alloc_data = pd.DataFrame(alloc_data['allocation_details'])

print(alloc_data)