import requests

year_data = [x for x in range(201801, 201813)] + [x for x in range(201901, 201903)]

for year in year_data[:3]:

    url = f"https://s3.amazonaws.com/fordgobike-data/{year}-fordgobike-tripdata.csv.zip"
        
    response = requests.get(url)
   
    with open(f"{year}-fordgobike-tripdata.csv.zip", mode = "wb") as file:
        file.write(response.content)