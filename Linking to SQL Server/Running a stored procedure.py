import pyodbc

# create a connection to SQL Server database
cn = pyodbc.connect(
    r"Driver=SQL Server;"
    r"Server=.\sql2019;"
    r"Database=Movies;"
    r"Trusted_Connection=yes;"
)

# create a cursor
csr = cn.cursor()

# create SQL statement
sql_command = 'EXEC ListFilms ?, ?'
values = ('t',1)

# run stored procedure
csr.execute(sql_command,values)

# action query
# csr.commit()

films = csr.fetchall()

print(films)

# close connection
cn.close()