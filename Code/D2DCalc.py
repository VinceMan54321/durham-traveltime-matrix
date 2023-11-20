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
matrix = {'Hollows A': {'Alspaugh': 21, 'Bassett': 20, 'Bell Tower': 23, 'Blackwell Dorm': 20, 'Brown Dorm': 21, 'East House': 19, 'Epworth Dorm': 21, 'Gilbert-Addoms': 21, 'Giles Dorm': 20, 'Pegram': 18, 'Randolph Dorm': 22, 'Southgate Dorm': 22, 'Trinity': 23, 'West House': 18, 'Wilson Dorm': 20, '300 Swift': 18, 'Craven Quad': 5, 'Crowell Quad': 5, 'Decker Tower': 9, 'Edens Quad': 8, 'Few Quad': 9, 'Hollows B': 10, 'Keohane 4E': 6, 'Keohane Quad': 5, 'Kilgo Quad': 9, 'Wannamaker Quad': 4, 'Baldwin Auditorium': 24, "Bishop's House": 23, 'Bivins Building': 25, 'Branson Hall': 24, 'Brodie Recreation Center': 22, 'Classroom Building': 19, 'Crowell Building': 20, 'East Duke Building': 21, 'Friedl Building': 19, 'Lilly Library': 21, 'Mary Duke Biddle Music Building': 23, 'West Duke Building': 20, 'White Lecture Hall': 19, 'Allen Building': 10, 'Biosciences Building': 13, 'Brodhead Center': 9, 'Bryan Center': 13, 'Card Gymnasium': 8, 'Duke Chapel': 12, 'Fitzpatrick': 15, 'Fuqua School of Business': 18, 'Gross Hall': 12, 'Health and Wellness Center': 7, 'Languages Building': 11, 'LSRC': 16, 'Old Chemistry Building': 12, 'Penn Pavillion ': 9, 'Bostock Library': 12, 'Rubenstein Library': 12, 'Reuben-Cooke Building': 12, 'Sanford Building': 10, 'Social Sciences Building': 11, 'Wilson Recreation ': 8, 'Chipotle ': 26, 'Sushi Love': 28, "Devil's Pizzeria ": 26, 'Wholefoods': 22, 'Smash Burger': 26, 'Exxon': 22, 'The University Inn': 16, 'Berkshire MainStreet': 22, 'Burger Bach': 28, 'Moge Tea': 27, 'Nanaline Duke': 19, 'Duke University Hospital': 17, 'Trent Hall': 14, 'Guasaca': 26, 'Alpaca': 25, 'JB Duke Hotel': 19, 'Bluezone Parking': 8, 'Nasher Museum of Art': 13, 'Duke Garden': 18, 'Karsh Alumni Center': 12, 'Pascal Field House': 15, 'Washington Duke Inn': 21}}


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
                    merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 5
                else: 
                    merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 2
            else: 
                if time_of_day == "Night":
                    merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 11

                else: 
                    merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 5.5
        if start_type == "dorm": 
            merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 3
        if dest_type == "dorm":
            merged_df.at[ind, "Time"] = merged_df.at[ind, "Time"] + 3

    ret_df = merged_df 
    return ret_df
        




dict = matrix["Hollows A"]
travel_time_df = pd.DataFrame(list(dict.items()), columns = ['Name', 'Time'])
baseline_df = travel_time_df.merge(locations_df, how = "outer", on = "Name")




updated_df = door_to_door_updates("Hollows A", matrix, True, "Day")



#calc descriptive stats 
def calculate_mean_travel_time(times_df): 
    time = times_df["Time"].mean()
    return time

# -----------Baseline------------------#
#average time to get to other places on West campus with GMaps
GMap_west = baseline_df.loc[baseline_df['Campus'] == "West"]
baseline_west_time = calculate_mean_travel_time(GMap_west)
print(baseline_west_time)

#average time to get to other places on east campus with Gmaps
GMap_east = baseline_df.loc[baseline_df['Campus'] == "East"]
baseline_east_time = calculate_mean_travel_time(GMap_east)
print(baseline_east_time)




#-------------D2D Model-----------------#
#average time to get to other places on West campus with D2D calc
D2D_west = updated_df.loc[updated_df['Campus'] == "West"]
updated_west_time = calculate_mean_travel_time(D2D_west)
print(updated_west_time)

#average time to get to other places on east campus with D2D calc
D2D_east = updated_df.loc[updated_df['Campus'] == "East"]
updated_east_time = calculate_mean_travel_time(D2D_east)
print(updated_east_time)


#compare travel times with real dataset 

        
    



