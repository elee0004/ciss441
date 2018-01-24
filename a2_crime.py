import json
import csv

"""
Emily Lee 
1.23.2018
converting from csv to json files
"""

row_count = 0
crime_data = []

with open('crime.csv', 'r') as csvfile:
	crime_stream = csv.DictReader(csvfile, delimiter=',', quotechar='=')
	for crime_row_dict in crime_stream:
		row_count += 1
		crime_date = crime_row_dict['CrimeDate']
		crime_time = crime_row_dict['CrimeTime']
		crime_code = crime_row_dict['CrimeCode']
		crime_location = crime_row_dict['Location']
		crime_description = crime_row_dict['Description']
		crime_IO = crime_row_dict['Inside/Outside']
		crime_weapon = crime_row_dict['Weapon']
		crime_post = crime_row_dict['Post']
		crime_district = crime_row_dict['District']
		crime_neighborhood = crime_row_dict['Neighborhood']
		crime_incidents = crime_row_dict['Total Incidents']
		if (row_count < 10):
			crime_data.append(crime_row_dict)
			print(row_count, crime_date, crime_time, crime_code, crime_location, crime_description, crime_IO, crime_weapon, crime_post, crime_district, crime_neighborhood, crime_incidents)
			
	print('I found this many crimes', row_count)
	with open('crimedata.json', 'w') as fp:
		for crime_row_dict in crime_stream:
			print(json.dumps(list(crime_stream)))	
	print ('The Csv has been converted to json')	 
			
		#print(json.dump(crime_data, fp, sort_keys=True, indent=4, seperators=(',',':')))