
import pandas as pd

# create a dictionary of films
films = {
    "Id": [ 1,2,3,5,6 ],    
	"Title": [ "Jurassic Park", "Spider-Man", "King Kong", "Superman Returns", "Titanic"],
	"Release Date": [ "1993-06-11", "2002-05-03", "2005-12-14", "2006-07-14", "1998-01-23" ],
	"Run Time": [ 126, 121, 187, 154, 194 ],
	"Genre": [ "Adventure", "Action","Adventure", "Action","Romance"]
}

# create a Pandas dataframe based upon this
Films = pd.DataFrame(films)

