from datetime import datetime, timedelta

# Defining a function to display current date and time

def display_current_datetime():
    
    current_date = datetime.now()
    print("current date and time: ", current_date.strftime(("%Y-%m-%d %H:%M:%S"))) 
    

# Defining a funtion to diplay future date based on user input

def calculate_future_date():

    
    while True:
        try:
            number_of_days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.\n")
            

    current_date  = datetime.now()
    future_date = current_date + timedelta(days = number_of_days)
    
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
    

# Calling all functions

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
