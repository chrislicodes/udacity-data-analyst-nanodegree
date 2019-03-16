import requests

#define years to gather
year_data = [x for x in range(201801, 201813)] + [x for x in range(201901, 201903)]

#loop over all files
for year in year_data:
    
    #set the url dependend on the url
    url = f"https://s3.amazonaws.com/fordgobike-data/{year}-fordgobike-tripdata.csv.zip"
    
    #request the url
    response = requests.get(url)
   
    #open a file with the same name as the downloaded one and write to content to the file
    with open(f"{year}-fordgobike-tripdata.csv.zip", mode = "wb") as file:
        file.write(response.content)
