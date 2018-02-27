import sqlite3
    
dbfile = 'payroll_dc_small.db' #db file 
conn = sqlite3.connect(dbfile) #connect db

print("Opened Succesfully Yayy!!!")



row_format_string = "{0:<25} {1:<15} {2:<10} {3:<10}"
print(row_format_string.format("location type", "location","salmax","salmin"))
	
cursor = conn.execute(
		"""
		select loc.loctypt, loc.loct, max(f.salary) salmax,min(f.salary) salmin
		from factdata_mar2016 f, loc
		where f.loc=loc.loc
		group by loc.loctypt, loc.loct
		order by salmax desc
		limit 20;
	    """)
	
for row in cursor:
	location_type, location, salmax, salmin = row 
	print(row_format_string.format(location_type, location[0:14], salmax, salmin))
	
	
print("\nThis is the report of min and max salries.")
conn.close()
	


		

 
