"""

Task: Given a specific starting location, calculate the updated travel times with the following factors 
- East vs west
- Weekend or weekday (CSwift vs C1) 
- Time of day 
- Average time to wait for bus 


Output: a start location, and a list with each row containing a location, travel time, and grid number
"""

#read csv 
import pandas as pd
locations_df = pd.read_csv ('Location_Dataset.csv')
campus = locations_df[locations_df["Name"] == "Hollows A"]['Campus']


west_to_east = "WestEast"
east_to_west = "EastWest"

def door_to_door_updates(start, matrix, weekday, time_of_day): 
    dict = matrix[start]
    travel_time_df = pd.DataFrame(list(dict.items()), columns = ['Name', 'Time'])
    merged_df = travel_time_df.merge(locations_df, how = "outer", on = "Name")
    merged_df["Campus"] =  merged_df["Campus"].astype("string")
    merged_df["Location Type"] =  merged_df["Location Type"].astype("string")
    start_campus = locations_df[locations_df["Name"] == start]['Campus'].values[0]
    start_type = locations_df[locations_df["Name"] == start]['Location Type'].values[0]
    

    for ind, row in merged_df.iterrows():
        dest_campus = row["Campus"]
        dest_type = row["Location Type"]
        travel = start_campus + dest_campus
        if travel == west_to_east or travel == east_to_west: 
            if weekday: 
                if time_of_day == "Night":
                    merged_df.at[ind, "Time"] =  merged_df.at[ind, "Time"] + 5
                else: 
                    merged_df.iloc[ind]["Time"] =  merged_df.at[ind, "Time"] + 2
            else: 
                if time_of_day == "Night":
                    merged_df.iloc[ind]["Time"] =  merged_df.at[ind, "Time"] + 11

                else: 
                    merged_df.iloc[ind]["Time"] =  merged_df.at[ind, "Time"] + 5.5
        if start_type == "dorm" or dest_type == "dorm": 
            merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 3
            

    ret_df = merged_df 
    return ret_df
        
     
        
    



