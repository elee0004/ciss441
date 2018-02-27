import sqlite3
    
dbfile = 'payroll_dc_small.db' #db file 
conn = sqlite3.connect(dbfile) #connect db

print("Opened Succesfully Yayy!!!")



row_format_string = "{0:<25} {1:<15} {2:<10} {3:<10}"
print(row_format_string.format("Education Level", "Type","salmax","salmin"))
	
cursor = conn.execute(
		"""
		select edlvl.edlvltypt, edlvl.edlvlt, max(f.salary) salmax,min(f.salary) salmin
		from factdata_mar2016 f, edlvl
		where f.edlvl=edlvl.edlvl
		group by edlvl.edlvltypt, edlvl.edlvlt
		order by salmax desc
		limit 20;
	    """)
	
for row in cursor:
	Education_level, Type, salmax, salmin = row 
	print(row_format_string.format(Education_level, Type[0:14], salmax, salmin))
	
	
print("\nThis is the report of min and max salries.")
conn.close()
	
