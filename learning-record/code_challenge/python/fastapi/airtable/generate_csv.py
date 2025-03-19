import pandas as pd
from datetime import datetime, timedelta

def generate_datetime_ranges():
    # Set start and end dates
    start_date = datetime(2025, 3, 16)  # March 16, 2025
    end_date = datetime(2025, 6, 30)   # June 30, 2025
    
    dates = []
    tutors_list = []
    tutors = [
        "tutor A",
        "tutor B"
    ]
    
    current_date = start_date
    while current_date <= end_date:
        # Check if it's weekend (5 = Saturday, 6 = Sunday)
        is_weekend = current_date.weekday() >= 5
        
        # Set time ranges based on weekday/weekend
        if is_weekend:
            start_hour = 10  # 10am
            end_hour = 19    # 7pm
        else:
            start_hour = 12  # 12pm
            end_hour = 21    # 9pm
            
        # Generate times for each day
        for hour in range(start_hour, end_hour + 1):
            for tutor in tutors:
                date_obj = current_date.replace(hour=hour)
                formatted_date = date_obj.strftime("%B %d, %Y %I:%M%p").replace(" 0", " ")
                dates.append(formatted_date)
                tutors_list.append(tutor)
            
        current_date += timedelta(days=1)
    
    # Create DataFrame and save to CSV
    # Create a list for separated dates and times
    sg_dates = []
    sg_times = []
    for date_str in dates:
        date_parts = date_str.rsplit(' ', 1)  # Split at last space to separate date and time
        sg_dates.append(date_parts[0])
        sg_times.append(date_parts[1])

    csv_data = {
        'SG Date & Time': dates,
        'SG Date': sg_dates,
        'SG Time': sg_times,
        'Tutor': tutors_list
    }
    df = pd.DataFrame(csv_data)
    df.to_csv('calendar.csv', index=False)

if __name__ == "__main__":
    generate_datetime_ranges()