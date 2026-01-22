
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

# fetch 5 rows
# films = csr.fetchmany(5)

# # loop over rows listing each out
# for film in films:

#     print("{0} was made in {1}".format(film.Title,film.Released))

while True:

    film_row = csr.fetchone()

    # did this return anything?
    if not film_row:
        break

    # stop at Pirates film
    film_title = film_row.Title

    print(film_title)

    if "pirates" in str(film_title).lower():
        break




cn.close()