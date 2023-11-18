"""
Change output list from step 1 to a dictionary where the keys 
are all locations and the values include all of the 
other locations + travel times for a given location 
- For example: {perkins: {wu : 2, sanford : 9, Trinity Dorm : 23 …} 
- This is an example of the output for the specific key of perkins. It is 
saying perkins to wu is 2 mins, perkins to sanford is 9 mins and perkins to 
trinity is 23 mins 

Task: Given a specific starting location, calculate the updated travel times with the following factors 
- East vs west
- Weekend or weekday (CSwift vs C1) 
- Time of day 
- Average time to wait for bus 
- Think of more

Output: a start location, and a list with each row containing a location, travel time, and grid number
"""

#read csv 
import pandas as pd
#df = pd.read_csv ('location_dataset')




def door_to_door_updates(start, matrix): 
    dict = matrix[start]
    travel_time_df = pd.dataframe(list(dict.items()), Columns = ['Name', 'Time'])
    

