
# See more about pros and cons of BMI as a measurement of health at https://www.bbc.co.uk/news/health-43895508

# You can force positional or named arguments:

# - anything before the /, if used, must be positional
# - anything after the *, if used, must be keyword
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# 	pass

def bmi(height:float,*,weight:float) -> float:

    body_mass_index = weight / ( height ** 2)
    return body_mass_index

# Churchill's BMI
churchill_bmi = bmi(height=1.68, weight=95)
print(churchill_bmi)

# Stalin's BMI (estimates)
# churchill_bmi = bmi(1.65, 65)
# print(churchill_bmi)

[1,2,3].sort()