from datetime import datetime

def calculate_time_difference(start_time, end_time):
    # Define the format of the input dates (e.g., 'YYYY-MM-DD HH:MM:SS')
    time_format = "%Y-%m-%d %H:%M:%S"
    
    # Convert the string inputs to datetime objects
    start = datetime.strptime(start_time, time_format)
    end = datetime.strptime(end_time, time_format)
    
    # Calculate the difference between the two datetime objects
    time_diff = end - start
    
    # Get the days, hours, minutes, and seconds from the time difference
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Print the result
    print(f"Time Difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Example Usage
if __name__ == "__main__":
    # Sample input dates and times
    start_time = "2025-01-01 10:30:00"
    end_time = "2025-01-03 14:45:20"
    
    calculate_time_difference(start_time, end_time)
