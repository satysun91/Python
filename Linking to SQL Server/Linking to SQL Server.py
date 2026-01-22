
import pyodbc

# create a connection to SQL Server database
cn = pyodbc.connect(
	r"Driver=SQL Server;"
	r"Server=.\sql2019;"
	r"Database=Movies;"
	r"Trusted_Connection=yes;"
)

# set up my SQL query
qry = "SELECT * FROM tblFilm ORDER BY Title"

# create a cursor
csr = cn.cursor()

# execute a cursor
csr.execute(qry)

# fetch all rows
films = csr.fetchall()

# test worked
print(films)

# close the connection
cn.close()