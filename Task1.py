from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Parsing the date
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Getting the current date
        today = datetime.today().date()
        
        # Calculating the dates difference
        delta = today - input_date

        return delta.days
    
    except ValueError:
        return "The date format is not correct. Please pass the date in the 'YYYY-MM-DD' format."
    
print(get_days_from_today("2020-10-09"))