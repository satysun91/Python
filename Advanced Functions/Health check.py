
# See more about pros and cons of BMI as a measurement of health at https://www.bbc.co.uk/news/health-43895508

def bmi(height:float,weight:float) -> float:

    body_mass_index = weight / ( height ** 2)
    return body_mass_index

# test this out
my_stats = bmi(weight=82, height=1.8)
print(my_stats)

# Churchill's BMI
churchill_bmi = bmi(1.68, weight=95)
