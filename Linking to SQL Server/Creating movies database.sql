USE [master]
GO

-- create a database
CREATE DATABASE Movies
GO

USE Movies
GO

-- create table of films
CREATE TABLE [dbo].[tblFilm](
	[FilmId] [int] IDENTITY(1,1) PRIMARY KEY,
	[Title] [nvarchar](255) NULL,
	[Certificate] [nvarchar](255) NULL,
	[Director] [nvarchar](255) NULL,
	[Oscars] [float] NULL,
	[Minutes] [int] NULL,
	[Released] [int] NULL
)
GO

-- add some films
SET IDENTITY_INSERT [dbo].[tblFilm] ON 

INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (1, N'Evan Almighty', N'PG', N'Tom Shadyac', 0, 95, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (2, N'Transformers', N'12A', N'Michael Bay', 0, 144, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (3, N'Harry Potter and the Order of the Phoenix', N'12A', N'David Yates', 0, 138, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (4, N'Beowulf', N'12A', N'Robert Zemeckis', 0, 113, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (5, N'Bee Movie', N'U', N'Steve Hickner', 0, 90, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (6, N'Pirates of the Caribbean: At World''s End', N'12A', N'Gore Verbinski', 0, 168, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (7, N'I am Legend', N'15', N'Francis Lawrence', 0, 101, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (8, N'Ratatouille', N'U', N'Brad Bird', 1, 106, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (9, N'Spider-Man 3', N'12A', N'Sam Raimi', 0, 139, 2007)
INSERT [dbo].[tblFilm] ([FilmId], [Title], [Certificate], [Director], [Oscars], [Minutes], [Released]) VALUES (10, N'The Bourne Ultimatum', N'12A', N'Paul Greengrass', 3, 115, 2007)

SET IDENTITY_INSERT [dbo].[tblFilm] OFF

GO

-- show the results
SELECT * FROM tblFilm