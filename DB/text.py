# import random
# import numpy


# def day():
#     x=random.randint(1, 28)
#     return (x)

# def month():
#     x=random.randint(1, 12)
#     return x

# def choice():
#     x = numpy.random.choice(numpy.arange(1, 4), p=[0.75, 0.15, 0.1])
#     return x
# for i in range (100):
#     print(choice())


# import random
# from datetime import datetime, timedelta

# def random_date(year):
#     # Set start and end dates for the given year
#     start_date = datetime(year, 1, 1)
#     end_date = datetime(year, 12, 31)

#     # Generate a random date between the start and end dates
#     random_date = start_date + (end_date - start_date) * random.random()

#     return random_date.date()

# Test the function
# for i in range (10):
#     print(random_date(2023))


from datetime import datetime
def age(dob):
    birthdate = datetime.strptime(dob, '%Y-%m-%d')
    now = datetime.now()
    ag = now.year - birthdate.year - ((now.month, now.day) < (birthdate.month, birthdate.day))
    return ag

print(age('1930-12-16'))
