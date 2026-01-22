
def print_info(what:str, **extras) -> None:

    bits = what.split(",")

    link_text = extras["link_text"]
    column_number = extras["column_number"]

    print(bits[1] + link_text + bits[column_number])


# open CSV file
with open(r"C:\__work\Videos\Python tutorial\120b - Advanced functions\Files\Musical.csv") as csv_file:

    for line in csv_file.read().splitlines()[1:]:

        # use my function to print this out
        print_info(line,column_number=3,link_text=" lasted for this many minutes: ")


