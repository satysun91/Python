USE Movies
GO

-- create stored procedure to list selected films
CREATE PROC ListFilms(
	@FilmPrefix varchar(100) = '',
	@MinOscars int = 0
)
AS

-- list these films
SELECT
	f.Title,
	f.Released,
	f.Oscars
FROM
	tblFilm AS f
WHERE
	f.Title like '%' + @FilmPrefix + '%' and
	f.Oscars >= @MinOscars
GO

-- this should list all the films
EXEC ListFilms 

-- this should list all films winning at least 1 Oscar
EXEC ListFilms @MinOscars=1

-- this should list all films starting with T
EXEC ListFilms 't', 0

