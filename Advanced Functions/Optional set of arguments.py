
file_path = r"C:\__work\Videos\Python tutorial\120b - Advanced functions\Files\\"

# empty list
lines = []

def read_file(*genres:str) -> None:

    # looping over all the genres
    for genre in genres:

        # read the file
        with open(file_path + genre + ".csv") as genre_file:

            genre_lines = genre_file.read().splitlines()[1:]

            # add these lines to my list
            lines.extend(genre_lines)

# read lines from one file
read_file("animation","comedy","musical")

# print the lines
for line in lines:
    print(line)