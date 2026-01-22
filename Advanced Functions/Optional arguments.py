
# See more about pros and cons of BMI as a measurement of health at https://www.bbc.co.uk/news/health-43895508

def bmi(height:float,weight:float,if_metric:bool=True) -> float:

    # if imperial, change calcs
    if not if_metric:
        height = (height * 2.54) / 100
        weight = weight / 2.2

    body_mass_index = weight / ( height ** 2)
    return body_mass_index

# test this
print("\nMy BMI (metric units) is {0:.2f}".format(bmi(1.8, 82)))

print("\nMy BMI (metric units) is {0:.2f}".format(bmi(70, 178, False)))

