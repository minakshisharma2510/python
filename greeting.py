# '#import time
# if time < 12:00
#     print("Good morning!")
# elif 12:00 < time > 17:00:
#     print("Good afternoon!")
# elif 17:00 < time > 20:00:
#     print("Good evening!")  
# else:
#  print("Good night!")'
    
import time
# print(time.strftime("%H:%M:%S"))  # Prints current time in HH:MM:SS format
print("its" , time.strftime("%H:%M:%S"))  # Prints current time in HH:MM:SS format
# The time module provides various time-related functions.  
current_hour = time.localtime().tm_hour  # Gets current hour (0–23)
if 0 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 17:
    print("Good afternoon!")
elif 17 <= current_hour < 20:
    print("Good evening!")
else:
    print("Good night!")
# Note: The time module's localtime() function is used to get the current local time.
# The tm_hour attribute gives the current hour in 24-hour format.