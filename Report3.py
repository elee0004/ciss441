import sqlite3

dbfile = 'payroll_dc_small.db' #database file
conn = sqlite3.connect(dbfile) # connect to db

# give me a new line
print("Heather is a beast")


def main():
	#this is my header now
	print("{0:<25} {1:<10} {2:10}".format(
		"work_schedule", "salmax", "salmin"))

	cursor = conn.execute("""
		select wrksch.wstypt, max(f.salary) salmax, min(f.salary) salmin
		from factdata_mar2016 f, wrksch
		where f.worksch=wrksch.worksch
		group by wrksch.wstypt
		order by salmax desc
		limit 20;
	""")
	
	for row in cursor:
		work_schedule, salmax, salmin = row
		print("{0:<25} {1:<10} {2:<10}".format(
			work_schedule,
			salmax,
			salmin
			))


	print("\nThis is my report of min and max salaries by work schedule.")
	conn.close()



if __name__ == "__main__":
	main()
