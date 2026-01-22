
import WOL_functions as wol # type: ignore

# test it out
# print(wol.get_age("09/12/2012"))

import glob

for file in glob.glob(r"C:\__work\Videos\Python tutorial\120 - Functions\Files\\*.csv"):
    
    # split file into path and file name
    file_path, _, file_name = file.rpartition("\\")

    # read in this file
    lines = wol.film_lines(file_path + "\\",file_name)

    # loop over these lines
    for line in lines:

        # ID,Title,Release Date,Run Time,Genre
        id, title, release_date, run_time, genre = line.split(",")

        # get a nice run time
        nice_time = wol.get_duration(int(run_time))

        # get the age of the film
        age = wol.get_age(release_date)

        # print this out
        print(title,nice_time,age,genre)