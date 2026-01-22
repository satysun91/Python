
def get_duration(minutes:int) -> str:

    if not isinstance(minutes,int):
        return "NO SUCH NUMBER"

    # get the number of minutes
    mins = minutes % 60

    # get the number of hours
    hours = int((minutes - mins) / 60)

    # the hours as text
    hour_text = " hours" if hours >= 2 else " hour"
    
    # the minutes as text
    if mins == 0:
        minute_text = ""
    elif mins == 1:
        minute_text = " and 1 minute"
    else:
        minute_text = " and {0} minutes".format(mins)

    # return the final string of text
    return str(hours) + hour_text + minute_text

# test function with 3 films
print("\nNo Time To Die lasted " + get_duration("163"))
print("\nSome Like it Hot lasted " + get_duration(121))
print("\nDances with Wolves lasted " + get_duration(180))