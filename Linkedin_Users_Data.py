import csv
from linkedin_api import Linkedin

api = Linkedin('blabla@gmail.com', 'blabla')
#print(api.get_profile('ibrahima-dieng-2870a811a'))

#School informations
school = 'your-school'
max_results = 10

kwargs = {
     "keywords": "school:\"" + school +"\"",
     "network_depth": "O",
     #"max_results": max_results
    #"start": None,
    #"count": 20
 }

for i in range(1):
    magic_search = api.search_people(**kwargs,)

    for item in magic_search:
        profile_urn = item['urn_id']
        profile_name = item['name']
        location = item['location']
        jobtitle = item['jobtitle']
        School = item['schools']
        print("Name =", profile_name)

        file = 'linkedin_profiles_O_CPC.csv'
        with open(file, mode='a', newline="", encoding="utf-8") as f:

            write_csv = csv.writer(f)
            if f.tell() == 0:
                write_csv.writerow(["Name", "Current_Location", "JobTitle"])
            write_csv.writerow([profile_name, location, jobtitle])
