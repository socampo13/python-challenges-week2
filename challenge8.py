### 📝 **Challenge 8: Datetime**

##* Write a function to calculate the difference in days between two given dates in the format `YYYY-MM-DD`. The function should handle invalid date formats and provide a clear error message when the format is incorrect.
##* Expected function: `date_difference(date1: str, date2: str) -> int`.

from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        difference = (d2 - d1).days
        return abs(difference)
    except ValueError:
        raise ValueError("Invalid format. Use 'YYYY-MM-DD'")
    

## Test
try:
    print(date_difference("2025-01-15", "2025-01-20"))
except ValueError as e:
    print(e)